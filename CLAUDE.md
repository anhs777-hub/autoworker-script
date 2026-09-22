# autoworker-script

유튜브 영상 대본 자동 제작 파이프라인. "대본 만들어줘" 한마디로 레퍼런스 수집 → 분석 → 전략 → 대본 집필 → 검수 → 완성본 문서(대본·썸네일제목·업로드정보)까지 진행된다.

## 스킬 라우팅

아래 요청이 오면 **반드시 해당 SKILL.md를 먼저 읽고 그대로 따를 것.**

| 사용자가 말하면 | 읽을 파일 | 하는 일 |
|----------------|-----------|---------|
| "대본 만들어줘" · "봉봉빙빙" · "이어서 해줘" · "대본 다시 써줘" | `.claude/skills/script-pd/SKILL.md` | 대본 제작 전체 파이프라인 (상태 감지 → 자동 진행) |
| "이 대본 영어로 만들어줘" · "영어판 뽑아줘" | `.claude/skills/script-pd/SKILL.md` | 완성 대본의 영어 현지화 (LOCALIZE → `_EN` 산출물, 한국어 원본 보존) |
| "채널 만들어줘" | `.claude/skills/channel-setup/SKILL.md` | 대화형 채널 생성 |
| "세팅해줘" | `.claude/skills/setup/SKILL.md` | 최초 환경 설정 (폴더 점검 → 가상환경 → yt-dlp → 테스트) |
| "점검해줘" | `.claude/skills/doctor/SKILL.md` | 설치 상태 진단 — ✅❌ 리포트 (아무것도 수정하지 않음) |
| "업데이트해줘" | `.claude/skills/update/SKILL.md` | 새 버전 zip 적용 (channels/ 보존) |
| "초기화해줘" | `.claude/skills/reset/SKILL.md` | 도구 파일 원본 복구 (channels/ 보존) |
| "타임스탬프 채워줘" (완성 영상과 함께) | `.claude/skills/timestamp/SKILL.md` | 영상 전사 → `03_업로드정보.md` 설명글과 `04_타임스탬프.txt`를 실측값으로 교체 |

- 대본/스크립트 관련 요청은 표현이 달라도 script-pd로
- script-pd는 시작 시 ✅ 배너를 반드시 첫 출력으로 낸다. 배너를 낼 수 없는 상태(`CLAUDE.md`·`VERSION` 없음)면 잘못된 폴더 안내

## 크로스 플랫폼 규칙 (필수)

이 프로젝트는 macOS와 Windows 사용자가 함께 사용한다. **모든 명령어 실행 시 OS를 자동 감지하여 그에 맞는 명령어를 사용할 것.**

모든 문서에서 아래 표기를 쓴다:

- `{VENV_PYTHON}` = macOS/Linux: `.venv/bin/python` | Windows: `.venv\Scripts\python`
- `{VENV_PIP}` = macOS/Linux: `.venv/bin/pip` | Windows: `.venv\Scripts\pip`

### Python 실행

```bash
# macOS/Linux
.venv/bin/python scripts/collect.py --project {project} --channel "{channel}" URL1 URL2

# Windows (cmd/PowerShell)
.venv\Scripts\python scripts/collect.py --project {project} --channel "{channel}" URL1 URL2
```

### pip 실행

- macOS/Linux: `.venv/bin/pip install -U yt-dlp`
- Windows: `.venv\Scripts\pip install -U yt-dlp`

### 파일/디렉토리 조작 — 셸 명령 대신 Python 사용

OS별 셸 명령(`mv`, `rm -r`, `mkdir -p` 등)은 크로스 플랫폼 호환이 안 되므로 **Python으로 대체**한다 (`.venv`가 아직 없으면 시스템 python 사용):

```bash
# mkdir -p 대신
{VENV_PYTHON} -c "import os; os.makedirs('path/to/dir', exist_ok=True)"

# mv 대신
{VENV_PYTHON} -c "import shutil; shutil.move('src', 'dst')"

# rm -r 대신
{VENV_PYTHON} -c "import shutil; shutil.rmtree('path/to/dir')"
```

> **프롬프트/스킬 안의 셸 명령은 예시일 뿐이다.** 실행 시 반드시 현재 OS에 맞는 명령어를 사용할 것.



## 구조 요약

- `channels/{채널}/config/` — 채널 설정 (`profile.md`가 채널 성격의 정본, `style-ban.json`이 문체 검사 규칙의 정본)
- `channels/{채널}/projects/{프로젝트}/` — 작업 폴더 (`_refs/` 수집 · `_script/` 대본 · `output/` 최종)
- `prompts/` — 파이프라인 프롬프트 · `scripts/` — Python 도구 · `.claude/` — 스킬·에이전트 정의
- 상세 구조와 사용법은 `README.md` 참조

## 산출물

완성본은 `output/` 폴더 하나에 모인다 (번호 순서대로 사용):
`01_대본.txt` (영상 제작 사이트에 업로드 — TTS → 영상 제작 진행. 정본은 `_script/script.txt`) · `02_썸네일제목.md` (제목 후보 + 썸네일 문구·이미지 프롬프트) · `03_업로드정보.md` (제목/설명글/태그/고정 댓글 + 주요 출처) · `04_타임스탬프.txt` (챕터 목록만 — 복사용. 시각은 추정치, 영상 완성 후 실측 교체).
부가: `_script/review.md` (검수 리포트), 이미지 자동 생성을 켠 채널은 `output/썸네일/` (이미지).

**완성본 아티팩트**: 파이프라인이 끝나면 위 4종을 한 페이지로 묶은 아티팩트를 **항상 발행한다** (섹션별 복사 버튼 포함 — 업로드 작업용 화면). 규격은 `prompts/output-artifact.md`, URL은 `_script/artifact-url.txt`에 저장되어 재실행 시 같은 주소로 갱신된다. 정본은 어디까지나 `output/`의 파일이다.
