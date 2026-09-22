---
name: doctor
description: 설치 상태 진단 스킬. 폴더·버전·가상환경·yt-dlp·파일 무결성(manifest 대조)·채널 설정을 검사해 ✅❌ 리포트를 출력한다. 진단 전용 — 어떤 파일도 수정하지 않음. 트리거: "점검해줘", "진단해줘", "상태 확인해줘", "doctor".
---

# Doctor Skill

설치·환경 문제를 한 번에 진단한다. 리포트 캡처 → 조교 전달이 CS의 1차 프로토콜이다.

## 원칙

- **진단만 한다. 파일을 만들거나 고치거나 지우지 않는다.** 고치는 것은 "세팅해줘"(환경) / "초기화해줘"(파일 원복) / "업데이트해줘"(새 버전)의 몫
- 검사 중간에 ❌가 나와도 **끝까지 전부 검사**하고 종합 리포트를 낸다
- 검사는 Python 한 줄 명령으로 (CLAUDE.md 크로스 플랫폼 규칙). `.venv`가 없거나 깨진 상태면 시스템 python으로 검사

## 검사 항목 (6종, 순서대로)

### 1. 폴더
- `CLAUDE.md`·`VERSION` 존재 확인. 없으면 ❌ 잘못된 폴더:
  - 하위에 `autoworker-script/CLAUDE.md`가 있으면 → 비고: "이중 폴더 — VS Code에서 안쪽 폴더를 여세요"
- 현재 경로에 비ASCII(한글) 또는 OneDrive 포함 → ⚠️ 비고: "'세팅해줘'가 이동을 도와줍니다"

### 2. 버전
- `VERSION` 값 읽기
- `CHANGELOG.md` 최상단 `## v…` 섹션의 버전과 일치하는지 (불일치 → ⚠️ 파일 오염 의심)

### 3. Python·가상환경
- `.venv` 존재 + `{VENV_PYTHON} --version` 실행 성공 + 3.10 이상
- 실패 시 원인을 구분해 ❌ 비고에 표기:
  - `.venv`는 있는데 현재 OS용 실행 파일이 없으면(Windows인데 `Scripts\` 없이 `bin/`만 있음, 또는 그 반대) → "다른 OS에서 만든 .venv가 복사된 상태 — '세팅해줘' 또는 '대본 만들어줘'가 자동으로 다시 만듭니다"
  - 그 외 → "'세팅해줘'를 실행하세요"

### 4. yt-dlp
- `{VENV_PYTHON} -m yt_dlp --version`
- 실패 → ❌ 비고: "'세팅해줘'를 실행하세요"

### 5. 파일 무결성 (manifest 대조)
- 아래 Manifest 블록의 경로 전부를 Python으로 일괄 존재 확인:
```
{VENV_PYTHON} -c "import os; paths=['CLAUDE.md','README.md', ...manifest 전체...]; miss=[p for p in paths if not os.path.exists(p)]; print('OK' if not miss else 'MISSING: '+', '.join(miss))"
```
- `channels/cclue-economy/…` 5개는 **예시 채널** — 없으면 ⚠️(지웠어도 문제없음), 그 외 누락은 ❌
- ❌ 비고: "'초기화해줘'로 원복 가능 (채널·작업물은 보존됩니다)"

### Manifest (정본 — 배포 규격 검사 packager도 이 블록을 파싱한다)

```manifest
CLAUDE.md
README.md
CHANGELOG.md
VERSION
requirements.txt
.claude/skills/script-pd/SKILL.md
.claude/skills/channel-setup/SKILL.md
.claude/skills/setup/SKILL.md
.claude/skills/doctor/SKILL.md
.claude/skills/update/SKILL.md
.claude/skills/reset/SKILL.md
.claude/skills/timestamp/SKILL.md
.claude/agents/video-analyst.md
.claude/agents/data-researcher.md
.claude/agents/script-writer.md
.claude/agents/script-reviewer.md
prompts/pd-script.md
prompts/pd-agents.md
prompts/pd-templates.md
prompts/creative-strategy.md
prompts/ctr-reference.md
prompts/reference-analyze.md
prompts/reference-patterns.md
prompts/data-research.md
prompts/script-review-checklist.md
prompts/tts-rules.md
prompts/thumbnail-design.md
prompts/youtube-meta.md
prompts/localization.md
prompts/output-artifact.md
scripts/collect.py
scripts/finalize.py
scripts/timestamp.py
scripts/src/project_resolver.py
scripts/src/merge_draft.py
scripts/src/validate_draft.py
scripts/src/thumbnail/generate_thumbnails.py
channels/_template.json
channels/cclue-economy/config/settings.json
channels/cclue-economy/config/profile.md
channels/cclue-economy/config/workflow.json
channels/cclue-economy/config/thumbnail-strategy.json
channels/cclue-economy/config/pd-guide.md
```

### 6. 채널
- `channels/` 하위 실제 채널 폴더 목록 (`_`로 시작하는 항목 제외)
  - 0개 → ⚠️ 비고: "채널 없음 — '채널 만들어줘'부터 하세요"
- 각 채널: `config/` 4파일(settings.json·profile.md·workflow.json·thumbnail-strategy.json) 존재 + settings.json JSON 파싱 성공
- settings.json의 `thumbnail.generate_images`가 `true`인데 루트 `.env`에 `GEMINI_API_KEY`가 없으면 → ⚠️ 비고: "썸네일 이미지 생성이 켜져 있는데 API 키가 없습니다 (README '썸네일' 참고)"

## 리포트 (고정 양식)

```
🩺 점검 결과 — autoworker-script v2.0.0

| 항목 | 상태 | 비고 |
|------|------|------|
| 폴더 위치 | ✅ | C:\autoworker-script |
| 버전 | ✅ | v2.0.0 (CHANGELOG 일치) |
| Python 가상환경 | ✅ | Python 3.12.4 |
| yt-dlp | ✅ | 2026.8.6 |
| 파일 무결성 | ✅ | 38/38 |
| 채널 | ✅ | my-channel (+ 예시 cclue-economy) |
```

- 전부 ✅ → 마지막 줄: "모든 항목 정상입니다. 바로 '대본 만들어줘' 하시면 됩니다."
- ❌/⚠️ 있음 → 마지막 줄 고정 (생략 금지 — CS 1차 프로토콜):
  > **이 결과 화면을 캡처해서 조교에게 보내주세요.** 가장 빠른 해결 방법입니다.
