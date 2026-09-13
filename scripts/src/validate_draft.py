"""draft.md 분량 검증 — 전체 합계 밴드 + 파트별 느슨한 하한.

사용법:
    .venv/bin/python scripts/src/validate_draft.py <outline_path> <draft_path> \
        [--band-low 0.9] [--band-high 1.15] [--part-floor 0.7]

검사 기준 (게이트는 이 2개뿐 — 파트별 고정 쿼터는 검사하지 않는다):
    1. 전체 합계: 타겟 글자수의 90~115% 밴드
       - 타겟 글자수: outline `기획 뼈대`의 "타겟 러닝타임 ... 목표 N자" 우선 (전체 대본 기준),
         없으면 파트 배정(범위는 중앙값)의 합 (이 경우 목표가 없는 섹션은 합산에서 제외)
    2. 파트별 하한: 배정 하한(범위면 하한값, 고정값이면 그 값)의 70% 미만 = 파트 스킵으로 간주

종료 코드:
    0 — 밴드 + 전 파트 하한 통과
    1 — FAIL (밴드 이탈 또는 하한 미달 파트)
    2 — 파싱 에러 (목표/섹션 추출 불가)
"""

import argparse
import re
import sys
from pathlib import Path

# ── outline.md 파트 목표 추출 ──────────────────────────────────
# 지원: "### 파트 1: 제목 (~4분, 2,000~3,500자 — 핵심 파트)"  (범위)
#       "### 파트 1: 제목 (~4분, ~2,000자)"                    (고정값, 레거시)
_OUTLINE_PART_RE = re.compile(
    r"^###\s+(.+?)\s*\("        # 파트 제목
    r"[^,)]*,\s*"               # 시간 부분 (~N분 등)
    r"~?([\d,]+)\s*(?:~\s*([\d,]+))?\s*자"  # 글자수: 하한(~상한)
    r"[^)]*\)",                 # 중요도 주석 등
    re.MULTILINE,
)

# outline `기획 뼈대`의 전체 목표 글자수: "- 타겟 러닝타임: 25~35분 (목표 12,900자, ...)"
_TARGET_CHARS_RE = re.compile(r"타겟\s*러닝타임[^\n]*?목표\s*([\d,]+)\s*자")

# ── draft.md 섹션 파싱 (finalize.py 동일 로직) ────────────────
_SECTION_HEADER_RE = re.compile(r"^#{2}\s+(.*)$")
_ANY_HEADER_RE = re.compile(r"^#{1,6}\s+")
_HR_RE = re.compile(r"^-{3,}$")
_BLOCKQUOTE_RE = re.compile(r"^>.*$")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", flags=re.DOTALL)

# 첫 `##` 이전 본문(h3 Hook/Intro)에 붙일 섹션 라벨
_PREAMBLE_LABEL = "Hook & Intro"


def _to_int(s: str) -> int:
    return int(s.replace(",", ""))


def parse_outline_targets(text: str) -> list[dict]:
    """outline.md에서 파트별 배정(하한~상한)을 추출한다. 고정값은 하한=상한."""
    targets = []
    for m in _OUTLINE_PART_RE.finditer(text):
        low = _to_int(m.group(2))
        high = _to_int(m.group(3)) if m.group(3) else low
        if high < low:
            low, high = high, low
        targets.append({
            "title": m.group(1).strip(),
            "low": low,
            "high": high,
            "mid": (low + high) / 2,
        })
    return targets


def parse_target_chars(text: str) -> int | None:
    """outline `기획 뼈대`의 전체 목표 글자수 (없으면 None)."""
    m = _TARGET_CHARS_RE.search(text)
    return _to_int(m.group(1)) if m else None


def parse_draft_sections(text: str) -> list[dict]:
    """draft.md에서 ## 헤더 기준으로 섹션별 글자수를 측정한다.

    첫 `##` 앞의 본문(hook-intro.md는 `### Hook`/`### Intro` h3로 쓰도록 규정되어
    있어 h2 섹션으로 잡히지 않는다)은 `_PREAMBLE_LABEL` 섹션으로 묶는다.
    그래야 sections[0]이 실제 Hook이 되고 Hook 글자수도 합계에 포함된다.
    """
    text = _HTML_COMMENT_RE.sub("", text)

    sections: list[dict] = []
    current_label: str | None = None
    current_chars = 0
    prev_had_text = False

    def _flush():
        nonlocal current_label, current_chars, prev_had_text
        if current_label is not None:
            sections.append({"title": current_label, "chars": current_chars})
        elif current_chars > 0:
            # 첫 ## 이전의 h3 Hook/Intro 블록
            sections.append({"title": _PREAMBLE_LABEL, "chars": current_chars})
        current_label = None
        current_chars = 0
        prev_had_text = False

    for line in text.splitlines():
        stripped = line.strip()

        if _HR_RE.match(stripped):
            continue
        if _BLOCKQUOTE_RE.match(stripped):
            continue

        m = _SECTION_HEADER_RE.match(stripped)
        if m:
            _flush()
            current_label = m.group(1).strip()
            continue

        if _ANY_HEADER_RE.match(stripped):
            continue

        if stripped:
            if prev_had_text:
                current_chars += 1  # 줄 간 공백 구분자
            current_chars += len(stripped)
            prev_had_text = True

    _flush()
    return sections


def validate(
    outline_path: Path,
    draft_path: Path,
    band_low: float,
    band_high: float,
    part_floor: float,
) -> int:
    """검증 실행. 종료 코드 반환."""
    outline_text = outline_path.read_text(encoding="utf-8")
    draft_text = draft_path.read_text(encoding="utf-8")

    targets = parse_outline_targets(outline_text)
    if not targets:
        print(f"ERROR: outline.md에서 파트별 배정을 추출하지 못했습니다: {outline_path}", file=sys.stderr)
        return 2

    sections = parse_draft_sections(draft_text)
    # 전부 preamble = `##` 헤더가 하나도 없다 → 파트 게이트 불가
    if not sections or all(s["title"] == _PREAMBLE_LABEL for s in sections):
        print(f"ERROR: draft.md에서 ## 섹션을 감지하지 못했습니다: {draft_path}", file=sys.stderr)
        return 2

    # 첫 번째 섹션 = Hook & Intro (파트 배정 없음)
    hook = sections[0]
    body_sections = sections[1:]

    if len(body_sections) != len(targets):
        print(
            f"WARNING: outline 배정 {len(targets)}개 vs draft 섹션(Hook 제외) {len(body_sections)}개 — 매칭 가능한 만큼만 비교",
            file=sys.stderr,
        )

    # ── 파트별 하한 검사 ─────────────────────────────────────
    rows: list[dict] = []
    rows.append({
        "title": hook["title"],
        "band": "-",
        "floor": None,
        "actual": hook["chars"],
        "result": "SKIP",
    })

    fail_parts: list[str] = []
    match_count = min(len(body_sections), len(targets))
    for i in range(match_count):
        t = targets[i]
        s = body_sections[i]
        floor = round(t["low"] * part_floor)
        ok = s["chars"] >= floor
        if not ok:
            fail_parts.append(s["title"])
        band_str = f"{t['low']:,}~{t['high']:,}" if t["high"] > t["low"] else f"{t['low']:,}"
        rows.append({
            "title": s["title"],
            "band": band_str,
            "floor": floor,
            "actual": s["chars"],
            "result": "PASS" if ok else "FAIL",
        })

    for s in body_sections[match_count:]:
        rows.append({
            "title": s["title"],
            "band": "-",
            "floor": None,
            "actual": s["chars"],
            "result": "SKIP",
        })

    # ── 전체 합계 밴드 검사 ──────────────────────────────────
    target_chars = parse_target_chars(outline_text)
    if target_chars:
        total_actual = sum(s["chars"] for s in sections)  # Hook 포함 전체
        total_target = target_chars
        basis = "기획 뼈대 목표 글자수 (Hook 포함 전체)"
    else:
        total_actual = sum(body_sections[i]["chars"] for i in range(match_count))
        total_target = sum(t["mid"] for t in targets[:match_count])
        basis = "파트 배정 중앙값 합 (매칭 섹션만)"

    total_ratio = total_actual / total_target if total_target > 0 else 0
    band_ok = band_low <= total_ratio <= band_high

    # ── 출력 ─────────────────────────────────────────────────
    col_w = max(max(len(r["title"]) for r in rows), 10)
    header = f"{'섹션':<{col_w}} | {'배정':>12} | {'하한':>6} | {'실제':>6} | 결과"
    sep = "─" * len(header)

    print(header)
    print(sep)
    for r in rows:
        floor_str = f"{r['floor']:,}" if r["floor"] is not None else "-"
        print(f"{r['title']:<{col_w}} | {r['band']:>12} | {floor_str:>6} | {r['actual']:>6,} | {r['result']}")
    print(sep)
    print(
        f"전체 합계: {total_actual:,} / {total_target:,.0f} ({total_ratio:.0%}) — "
        f"허용 밴드 {band_low:.0%}~{band_high:.0%} [{'PASS' if band_ok else 'FAIL'}]"
    )
    print(f"  (기준: {basis})")

    if fail_parts:
        print(f"하한 미달 파트: {', '.join(fail_parts)} — 파트 스킵 의심, 미사용 사례·데이터로 보충")
    if not band_ok:
        direction = "부족 — 미사용 사례·데이터 추가" if total_ratio < band_low else "초과 — 중복·필러 제거 후 압축"
        print(f"전체 분량 {direction}")

    return 1 if (fail_parts or not band_ok) else 0


def main():
    parser = argparse.ArgumentParser(description="draft.md 분량 검증 (전체 밴드 + 파트 하한)")
    parser.add_argument("outline", type=Path, help="outline.md 경로")
    parser.add_argument("draft", type=Path, help="draft.md 경로")
    parser.add_argument("--band-low", type=float, default=0.9, help="전체 합계 하한 비율 (기본 0.9)")
    parser.add_argument("--band-high", type=float, default=1.15, help="전체 합계 상한 비율 (기본 1.15)")
    parser.add_argument("--part-floor", type=float, default=0.7, help="파트 하한 비율 — 배정 하한 대비 (기본 0.7)")
    args = parser.parse_args()

    if not args.outline.exists():
        print(f"ERROR: outline.md를 찾을 수 없습니다: {args.outline}", file=sys.stderr)
        sys.exit(2)
    if not args.draft.exists():
        print(f"ERROR: draft.md를 찾을 수 없습니다: {args.draft}", file=sys.stderr)
        sys.exit(2)

    sys.exit(validate(args.outline, args.draft, args.band_low, args.band_high, args.part_floor))


if __name__ == "__main__":
    main()
