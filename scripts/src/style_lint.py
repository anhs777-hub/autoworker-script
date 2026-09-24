# -*- coding: utf-8 -*-
"""대본 문체 린터 — 금지 표현 · 반복 상투구 · 지시대명사 선행 검사

사용법:
    python scripts/src/style_lint.py {script.txt} [--channel {채널}] [--json]

규칙은 channels/{채널}/config/style-ban.json에서 읽는다. 없으면 내장 기본값.
  ban    — 한 번이라도 나오면 오류 (exit 1)
  limit  — max회를 넘으면 오류. 정상 표현이지만 반복되면 상투구가 되는 것들
  warn   — 사람이 판단할 것 (exit code에 반영 안 함)
"""
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from console import setup_console
    setup_console()
except Exception:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

DEFAULT_RULES = {
    "ban": [
        {"p": "계산서",   "why": "AI 상투 은유", "fix": "실제로 일어난 일과 수치를 그대로"},
        {"p": "청구서",   "why": "AI 상투 은유", "fix": "실제로 일어난 일과 수치를 그대로"},
        {"p": "성적표",   "why": "AI 상투 은유", "fix": "무엇이 몇으로 바뀌었는지 직접"},
        {"p": "시한폭탄", "why": "AI 상투 은유", "fix": "언제 무엇이 닥치는지 날짜로"},
        {"p": "도미노",   "why": "AI 상투 은유", "fix": "무엇이 무엇을 건드렸는지 순서대로"},
        {"p": "양날의 검", "why": "AI 상투 은유", "fix": "이득과 손해를 각각 한 줄로"},
        {"p": "빙산의 일각", "why": "AI 상투 은유", "fix": "확인된 범위까지만"},
        {"p": "판도라의 상자", "why": "AI 상투 은유", "fix": "무엇이 열렸는지 직접"},
        {"p": "부메랑",   "why": "AI 상투 은유", "fix": "누구에게 어떻게 돌아왔는지"},
        {"p": "대가를 치르", "why": "AI 상투 은유", "fix": "무엇을 얼마나 잃었는지"},
        {"p": "나란히 두고", "why": "번역투 상투구", "fix": "두 숫자를 바로 제시"},
        {"p": "재어보",   "why": "번역투 상투구", "fix": "비교 결과를 직접"},
        {"p": "그 자리에 놓고", "why": "번역투 상투구", "fix": "무엇을 비교하는지 직접"},
        {"p": "되어지",   "why": "이중 피동", "fix": "능동으로"},
        {"p": "에 다름 아니", "why": "번역체", "fix": "~입니다"},
        {"p": "에 있어서", "why": "번역체", "fix": "~에서 / ~은"},
        {"p": "것으로 보여진", "why": "이중 피동", "fix": "~로 보입니다"},
    ],
    "limit": [
        {"p": "놓고 보", "max": 1, "why": "대본마다 반복되는 상투구"},
        {"p": "나란히",  "max": 1, "why": "대본마다 반복되는 상투구"},
        {"p": "셈이",    "max": 3, "why": "과다 사용 시 문어체로 들림"},
        {"p": "구조입니다", "max": 3, "why": "설명 상투구"},
        {"p": "인 겁니다", "max": 8, "why": "시그니처이지만 과하면 단조로움"},
    ],
    "warn": [
        {"p": r"(?m)^(이|그|저)\s?(회사|기업|나라|제품|앱|서비스|브랜드|시장|사업)",
         "regex": True, "why": "문단 첫머리 지시대명사 — 가리키는 대상이 앞에 없으면 음성으로 되짚을 수 없다",
         "fix": "첫 등장은 이름으로"},
    ],
}


def load_rules(channel):
    if channel:
        p = os.path.join(ROOT, "channels", channel, "config", "style-ban.json")
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                return json.load(f), p
    return DEFAULT_RULES, "(내장 기본값)"


def find(text, pat, is_regex=False):
    rx = re.compile(pat if is_regex else re.escape(pat))
    out = []
    for m in rx.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        s = text[max(0, m.start() - 35): m.start() + 45].replace("\n", " ").strip()
        out.append((line, s))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--channel", default=None)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    with open(a.script, encoding="utf-8") as f:
        text = f.read()
    rules, src = load_rules(a.channel)

    errors, warns = [], []

    for r in rules.get("ban", []):
        hits = find(text, r["p"], r.get("regex", False))
        if hits:
            errors.append({"kind": "금지", "p": r.get("label", r["p"]), "why": r["why"],
                           "fix": r.get("fix", ""), "n": len(hits), "hits": hits})

    for r in rules.get("limit", []):
        hits = find(text, r["p"], r.get("regex", False))
        if len(hits) > r["max"]:
            errors.append({"kind": "초과", "p": r.get("label", r["p"]), "why": r["why"],
                           "fix": "%d회까지. %d회 중 %d회를 다른 표현으로" % (r["max"], len(hits), len(hits) - r["max"]),
                           "n": len(hits), "max": r["max"], "hits": hits})

    for r in rules.get("warn", []):
        hits = find(text, r["p"], r.get("regex", False))
        if hits:
            warns.append({"kind": "확인", "p": r.get("label", r["p"]), "why": r["why"],
                          "fix": r.get("fix", ""), "n": len(hits), "hits": hits})

    if a.json:
        print(json.dumps({"errors": errors, "warns": warns}, ensure_ascii=False, indent=2))
        return 1 if errors else 0

    print("문체 린터 — %s" % os.path.basename(a.script))
    print("규칙: %s\n" % src)
    if not errors and not warns:
        print("통과. 걸린 표현 없습니다.")
        return 0

    for e in errors:
        head = "[금지] %s" % e["p"] if e["kind"] == "금지" else "[초과] %s — %d회 (상한 %d)" % (e["p"], e["n"], e["max"])
        print("%s\n   사유: %s\n   조치: %s" % (head, e["why"], e["fix"]))
        for ln, s in e["hits"][:3]:
            print("   L%-5d …%s…" % (ln, s))
        if len(e["hits"]) > 3:
            print("   (외 %d곳)" % (len(e["hits"]) - 3))
        print()

    for w in warns:
        print("[확인] %s — %d곳" % (w["p"], w["n"]))
        print("   사유: %s\n   조치: %s" % (w["why"], w["fix"]))
        for ln, s in w["hits"][:3]:
            print("   L%-5d …%s…" % (ln, s))
        print()

    print("─" * 50)
    print("오류 %d건 / 확인 %d건" % (len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
