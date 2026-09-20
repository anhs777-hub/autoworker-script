"""draft.md → script.txt 변환 + TTS-safe 기계 검증·자동 보정

1) 마크다운 메타(헤더, 구분선, 주석, 리스트 마커, 강조)를 제거하고
   문단 구조(빈 줄 구분)를 유지한 순수 대본 텍스트를 만든다.
2) "대본 작성 가이드" 6개조를 기계적으로 검증·자동 보정하고 리포트를 출력한다:
   ① 문장 끝 온점(.) 뒤 띄어쓰기
   ② 따옴표 금지
   ③ 문단 구분은 줄바꿈으로
   ④ 특수문자·이모지 금지
   ⑤ URL·이메일 금지
   ⑥ 단어 뒤 괄호 금지
   + 탭·보이지 않는 공백·[pause]류 태그 제거
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from console import enable_utf8_output
from project_resolver import resolve_project_dir

enable_utf8_output()

DEFAULT_CPM = 470  # 분당 글자수, 개행 제외 기준 (profile 실측치가 있으면 --cpm으로 전달)
# 완성 영상 3편 실측 평균 472자 — 노키아 482.7 / 홈플러스 464.6 / 세상의이유 007편 469.1.
# 예전 기본값 500은 개행을 포함해 세던 시절의 값이라, 개행 제외로 바꾼 지금은 분량을 짧게 잡는다.

# ---------- 마크다운 정리 ----------

_ANY_HEADER_RE = re.compile(r"^#{1,6}\s+")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", flags=re.DOTALL)
_HR_RE = re.compile(r"^-{3,}$")
_BLOCKQUOTE_RE = re.compile(r"^>.*$")
_LIST_MARKER_RE = re.compile(r"^(?:[-*•]|\d+\.)\s+")
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_EMPHASIS_RE = re.compile(r"(\*{1,3}|_{2,3}|`+)")

# ---------- 6개조 검증·보정 패턴 ----------

# ① 문장 끝 부호(+쉼표) 뒤 붙여쓰기 (소수점 3.5, 자릿수 1,000은 뒤가 숫자라 매치되지 않음)
_R1_SPACING_RE = re.compile(r"([.!?,])(?=[가-힣A-Za-z一-鿿])")

# ② 따옴표 (큰따옴표 전부 + 작은따옴표는 영단어 아포스트로피만 예외)
_R2_DQUOTE_RE = re.compile(r"[\"“”„«»]")
_R2_SQUOTE_RE = re.compile(r"[‘’](?![A-Za-z])|(?<![A-Za-z])[‘’']|'(?![A-Za-z])")

# ⑤ URL·이메일
_R5_URL_RE = re.compile(r"(?:https?://|www\.)\S+")
_R5_EMAIL_RE = re.compile(r"\S+@\S+\.\S+")

# ⑥ 단어 뒤 괄호: 클로드(Claude) → 클로드. 이후 남는 괄호(연출지시 등)는 통째 제거
_R6_WORD_PAREN_RE = re.compile(r"(?<=[가-힣A-Za-z0-9])\([^)]*\)")
_R6_ORPHAN_PAREN_RE = re.compile(r"\([^)]*\)")

# [pause]류 태그 + 보이지 않는 공백
_TAG_RE = re.compile(r"\[(?:pause|break|silence|music|sfx|쉼|멈춤|효과음|음악)[^\]]*\]", re.IGNORECASE)
_INVISIBLE_RE = re.compile(r"[​‌‍﻿]")

# ④ 특수문자: 개별 치환 후, 허용 문자 밖 전부 제거 (이모지·※·→ 등 일괄 커버)
_R4_REPLACEMENTS = [
    (re.compile(r"·|ㆍ"), ", "),        # 가운뎃점 → 쉼표 (미국·중국 → 미국, 중국)
    (re.compile(r"…|‥"), "..."),       # 말줄임표 → ...
    (re.compile(r"[–—―]"), " "),  # en/em 대시 → 공백
    (re.compile(r"。"), ". "),               # 。 → .
    (re.compile(r"、"), ", "),               # 、 → ,
    (re.compile(r"[〈-〛‹›\[\]{}<>]"), ""),  # 괄호류 기호 제거 (내용 유지)
]
_R4_ALLOWED_RE = re.compile(
    r"[^0-9A-Za-z"
    r"가-힣ᄀ-ᇿ㄰-㆏"  # 한글
    r"一-鿿"                             # 한자
    r"\s.,!?%~:'\-]"
)


def strip_markdown(raw: str) -> str:
    """draft.md에서 마크다운 메타를 제거하고 문단 구조(빈 줄)를 유지한 텍스트를 반환."""
    raw = _HTML_COMMENT_RE.sub("", raw)

    lines: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if _HR_RE.match(stripped) or _BLOCKQUOTE_RE.match(stripped) or _ANY_HEADER_RE.match(stripped):
            lines.append("")  # 구조 라인은 문단 경계로 취급
            continue
        stripped = _LIST_MARKER_RE.sub("", stripped)
        stripped = _MD_LINK_RE.sub(r"\1", stripped)
        stripped = _EMPHASIS_RE.sub("", stripped)
        lines.append(stripped)

    # 연속 비어있지 않은 줄 = 한 문단으로 병합, 빈 줄 = 문단 경계
    paragraphs: list[str] = []
    buf: list[str] = []
    for line in lines:
        if line:
            buf.append(line)
        elif buf:
            paragraphs.append(" ".join(buf))
            buf = []
    if buf:
        paragraphs.append(" ".join(buf))

    return "\n\n".join(paragraphs)


def _count_and_sub(pattern: re.Pattern, repl, text: str) -> tuple[str, int]:
    count = len(pattern.findall(text))
    return (pattern.sub(repl, text), count) if count else (text, 0)


def apply_tts_rules(text: str) -> tuple[str, dict]:
    """6개조 검증·자동 보정. (보정된 텍스트, 규칙별 보정 건수) 반환."""
    report: dict[str, int] = {}

    # 태그·보이지 않는 공백·탭 (기타 항목)
    text, n_tag = _count_and_sub(_TAG_RE, "", text)
    text, n_inv = _count_and_sub(_INVISIBLE_RE, "", text)
    text = text.replace(" ", " ").replace("　", " ").replace("\t", " ")
    report["extra"] = n_tag + n_inv

    # ⑤ URL·이메일 (특수문자 제거 전에 수행해야 패턴이 살아있음)
    text, n_url = _count_and_sub(_R5_URL_RE, "", text)
    text, n_email = _count_and_sub(_R5_EMAIL_RE, "", text)
    report["r5"] = n_url + n_email

    # ② 따옴표
    text, n_dq = _count_and_sub(_R2_DQUOTE_RE, "", text)
    text, n_sq = _count_and_sub(_R2_SQUOTE_RE, "", text)
    report["r2"] = n_dq + n_sq

    # ⑥ 단어 뒤 괄호 → 이후 남은 괄호(연출지시 등)도 통째 제거
    text, n_wp = _count_and_sub(_R6_WORD_PAREN_RE, "", text)
    text, n_op = _count_and_sub(_R6_ORPHAN_PAREN_RE, "", text)
    text = text.replace("(", "").replace(")", "")
    report["r6"] = n_wp + n_op

    # ④ 특수문자·이모지
    n_r4 = 0
    for pattern, repl in _R4_REPLACEMENTS:
        text, n = _count_and_sub(pattern, repl, text)
        n_r4 += n
    text, n_rest = _count_and_sub(_R4_ALLOWED_RE, "", text)
    report["r4"] = n_r4 + n_rest

    # ① 문장 끝 부호 뒤 띄어쓰기 (마지막에 수행)
    text, n_r1 = _count_and_sub(_R1_SPACING_RE, r"\1 ", text)
    report["r1"] = n_r1

    # 공백 정규화 (③ 문단 경계는 유지)
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n +", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()
    report["paragraphs"] = text.count("\n\n") + 1 if text else 0

    return text, report


def print_report(report: dict, char_count: int, cpm: int) -> None:
    def fmt(n):
        return f"{n}건 보정" if n else "0건"

    print("=== TTS-safe 검증 리포트 (대본 작성 가이드 6개조) ===")
    print(f"① 온점 뒤 띄어쓰기     : {fmt(report['r1'])}")
    print(f"② 따옴표 제거          : {fmt(report['r2'])}")
    print(f"③ 문단 구분            : {report['paragraphs']}개 문단 (빈 줄 구분 유지)")
    print(f"④ 특수문자·이모지 제거 : {fmt(report['r4'])}")
    print(f"⑤ URL·이메일 제거      : {fmt(report['r5'])}")
    print(f"⑥ 단어 뒤 괄호 제거    : {fmt(report['r6'])}")
    print(f"기타 (태그·공백 문자)  : {fmt(report['extra'])}")
    print("=" * 30)
    print(f"script.txt 생성 완료 ({char_count:,}자 — 개행 제외, ~{char_count // cpm}분 @ {cpm}자/분)")


def main():
    parser = argparse.ArgumentParser(description="draft.md → script.txt (+ TTS-safe 보정)")
    parser.add_argument("--project", required=True, help="프로젝트 폴더명")
    parser.add_argument("--channel", default=None, help="채널명 (미지정시 자동 탐색)")
    parser.add_argument("--cpm", type=int, default=DEFAULT_CPM,
                        help=f"분당 글자수 — profile 실측치 (기본 {DEFAULT_CPM})")
    args = parser.parse_args()

    base = resolve_project_dir(args.project, args.channel)
    script_dir = base / "_script"
    script_dir.mkdir(parents=True, exist_ok=True)
    draft = script_dir / "draft.md"

    if not draft.exists():
        print(f"draft.md가 없습니다: {draft}")
        sys.exit(1)

    text = strip_markdown(draft.read_text(encoding="utf-8"))
    text, report = apply_tts_rules(text)

    out = script_dir / "script.txt"
    out.write_text(text, encoding="utf-8")

    # 완성본 폴더 사본 — 학생이 여는 파일 (정본은 _script/script.txt)
    output_dir = base / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "01_대본.txt").write_text(text, encoding="utf-8")

    # 분량 계산은 개행을 뺀 글자수로 한다 — 줄바꿈은 낭독되지 않는데, 대본 포맷에 따라
    # 전체 글자의 2.5~7.4%까지 차지해서 포함하면 예상 분량이 3~7% 들쭉날쭉해진다.
    print_report(report, len(text.replace("\n", "")), args.cpm)
    print("완성본 사본: output/01_대본.txt (영상 제작 사이트 업로드용)")


if __name__ == "__main__":
    main()
