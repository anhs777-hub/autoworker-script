"""_draft_part*.md 조립 → draft.md + Hook 변형 diff 리포트.

writer가 Hook & Intro(_draft_part0.md)부터 클로징까지 전체를 집필하므로,
이 스크립트는 파트 파일을 순서대로 조립하고, draft 시작부가 확정된
hook-intro.md에서 얼마나 변형됐는지 리포트만 한다 (게이트 아님 — exit 0).
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from console import enable_utf8_output

enable_utf8_output()

_H2_RE = re.compile(r"^#{2,3}\s+(.+)$", re.MULTILINE)
_PART_NUM_RE = re.compile(r"_draft_part(\d+)\.md$")
_ANY_HEADER_RE = re.compile(r"^#{1,6}\s+")
_HR_RE = re.compile(r"^-{3,}$")
_BLOCKQUOTE_RE = re.compile(r"^>.*$")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", flags=re.DOTALL)
_SENT_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")

# 이 미만이면 "변형 큼" 경고 (게이트 아님)
_WARN_RATIO = 0.85


def extract_hook_intro(path: Path) -> str:
    """hook-intro.md에서 Hook/Intro 본문을 합쳐 반환."""
    text = path.read_text(encoding="utf-8")
    headers = [(m.start(), m.end(), m.group(1).strip()) for m in _H2_RE.finditer(text)]

    hook_text = None
    intro_text = None

    for i, (start, end, title) in enumerate(headers):
        next_start = headers[i + 1][0] if i + 1 < len(headers) else len(text)
        body = text[end:next_start].strip()

        if re.match(r"Hook(\s*\(|$)", title):
            hook_text = body
        elif re.match(r"Intro(\s*\(|$)", title):
            intro_text = body

    if hook_text is None or intro_text is None:
        raise ValueError(f"Hook/Intro 헤더를 찾을 수 없습니다: {path}")

    return f"{hook_text}\n{intro_text}"


def normalize_narration(text: str) -> str:
    """헤더·주석·구분선·블록인용을 제거하고 나레이션 텍스트만 한 줄로."""
    text = _HTML_COMMENT_RE.sub("", text)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if _HR_RE.match(stripped) or _BLOCKQUOTE_RE.match(stripped):
            continue
        if _ANY_HEADER_RE.match(stripped):
            continue
        lines.append(stripped)
    return " ".join(lines)


def first_section_body(draft_text: str) -> str:
    """조립된 draft에서 첫 번째 ## 섹션의 본문을 반환."""
    matches = list(re.finditer(r"^##\s+.+$", draft_text, re.MULTILINE))
    if not matches:
        return ""
    start = matches[0].end()
    end = matches[1].start() if len(matches) > 1 else len(draft_text)
    return draft_text[start:end]


def report_hook_diff(hook_intro_path: Path, draft_text: str) -> None:
    """draft 시작부 vs hook-intro.md 변형 리포트 (경고만, 게이트 아님)."""
    try:
        expected = normalize_narration(extract_hook_intro(hook_intro_path))
    except (ValueError, OSError) as e:
        print(f"WARNING: hook-intro.md 파싱 실패 — Hook 변형 리포트 생략 ({e})", file=sys.stderr)
        return

    actual = normalize_narration(first_section_body(draft_text))
    if not actual:
        print("WARNING: draft 첫 섹션이 비어 있어 Hook 변형 리포트를 생략합니다", file=sys.stderr)
        return

    ratio = difflib.SequenceMatcher(None, expected, actual).ratio()
    print(f"Hook 변형 리포트: hook-intro.md 대비 유사도 {ratio:.0%}")

    if ratio >= 0.98:
        print("  → 원문 유지")
        return

    if ratio < _WARN_RATIO:
        print(f"  ⚠ 변형이 큽니다 (유사도 {ratio:.0%} < {_WARN_RATIO:.0%}) — ask 모드에서는 사용자에게 diff를 표시하세요")

    expected_sents = _SENT_SPLIT_RE.split(expected)
    actual_sents = _SENT_SPLIT_RE.split(actual)
    diff = difflib.unified_diff(
        expected_sents, actual_sents,
        fromfile="hook-intro.md", tofile="draft.md", lineterm="",
    )
    for line in list(diff)[:40]:
        print(f"  {line}")


def collect_parts(parts_dir: Path) -> list[Path]:
    """_draft_part*.md를 숫자 순으로 정렬하여 반환 (part0 = Hook & Intro)."""
    parts = list(parts_dir.glob("_draft_part*.md"))
    if not parts:
        raise FileNotFoundError(f"_draft_part*.md 파일을 찾을 수 없습니다: {parts_dir}")

    def sort_key(p: Path) -> int:
        m = _PART_NUM_RE.search(p.name)
        return int(m.group(1)) if m else 999

    parts.sort(key=sort_key)
    return parts


def merge_draft(
    hook_intro_path: Path,
    parts_dir: Path,
    output_path: Path,
) -> int:
    """draft.md 조립 + Hook 변형 리포트. 0=성공, 1=오류."""
    try:
        parts = collect_parts(parts_dir)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    sections = [p.read_text(encoding="utf-8").strip() for p in parts]
    draft = "\n\n".join(sections) + "\n"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(draft, encoding="utf-8")

    print(f"draft.md 생성 완료: {output_path}")
    print(f"  {len(parts)}개 파트 조립 ({', '.join(p.name for p in parts)})")
    print(f"  총 {len(draft):,}자")

    report_hook_diff(hook_intro_path, draft)
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="_draft_part*.md 조립 → draft.md + Hook 변형 리포트",
    )
    parser.add_argument("--hook-intro", required=True, type=Path, help="hook-intro.md 경로 (변형 diff 비교용)")
    parser.add_argument("--parts-dir", required=True, type=Path, help="_draft_part*.md 디렉토리")
    parser.add_argument("--output", required=True, type=Path, help="출력 경로 (draft.md)")
    args = parser.parse_args()

    if not args.hook_intro.exists():
        print(f"ERROR: hook-intro.md를 찾을 수 없습니다: {args.hook_intro}", file=sys.stderr)
        sys.exit(1)
    if not args.parts_dir.is_dir():
        print(f"ERROR: parts 디렉토리를 찾을 수 없습니다: {args.parts_dir}", file=sys.stderr)
        sys.exit(1)

    sys.exit(merge_draft(args.hook_intro, args.parts_dir, args.output))


if __name__ == "__main__":
    main()
