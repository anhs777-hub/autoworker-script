# autoworker-script

**유튜브 영상 대본 자동 제작 파이프라인.**

"대본 만들어줘" 한마디로 레퍼런스 수집 → 분석 → 전략 → 대본 집필 → 검수 → 업로드 정보까지 자동으로 진행됩니다.

Claude Code가 PD 역할을 하며, 4개의 전문 에이전트를 오케스트레이션하여 유튜브 대본을 제작합니다.

---

## 어떻게 작동하나요?

```
사용자: "대본 만들어줘"
  ↓
Claude PD가 상태를 감지하고 자동으로 파이프라인을 실행:

1. COLLECT         — 레퍼런스 영상 수집 (yt-dlp)
2. ANALYZE         — 영상별 구조/기법 분석 (video-analyst 에이전트 ×N 병렬)
3. DATA_PREP       — 팩트체크·리서치 (data-researcher 에이전트) + 패턴 추출 (PD 직접)
4. STRATEGY        — 전략 3안 (컨셉/제목/Hook/핵심 메시지) + 썸네일 프롬프트 (PD 직접)
5. OUTLINE         — 통합 기획서 작성 (PD 직접, 셀프체크 10항목)
6. DRAFT           — 대본 집필 (script-writer 에이전트, 통짜 순차 집필) + 분량 검증
7. REVIEW_FINALIZE — 검수 (script-reviewer 에이전트) → script.txt 확정 (TTS-safe 자동 보정)
8. METADATA        — 완성본 문서 생성 (02_썸네일제목 · 03_업로드정보)
  ↓
최종 산출물: output/ 폴더 (01_대본.txt · 02_썸네일제목.md · 03_업로드정보.md)
```

중간에 멈춰도 **"이어서 해줘"** 하면 마지막 상태에서 자동 재개됩니다.

---

## 시작하기

### 1. 사전 준비

- **Python 3.10+**
- **Claude Code** (CLI 또는 IDE 확장)

### 2. 설치

VS Code에서 압축을 푼 `autoworker-script` **폴더 자체**를 열고, Claude Code에서:

```
"세팅해줘"
```

Claude가 폴더 위치 점검 → Python 가상환경 생성 → yt-dlp 설치 → 동작 테스트까지 자동으로 진행하고, 끝나면 ✅ 체크리스트를 보여줍니다.

<details>
<summary>수동으로 설치하려면 (참고)</summary>

```bash
# 압축을 푼 autoworker-script 폴더에서

# Python 가상환경 생성
python -m venv .venv

# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (cmd)
.venv\Scripts\activate.bat

pip install -r requirements.txt
```

</details>

### 3. 채널 만들기

채널이 없으면 대본을 만들 수 없습니다. 먼저 채널을 만들어야 합니다.

```
Claude에게: "채널 만들어줘"
```

Claude가 장르, 톤, 메시지 방향, 기본 러닝타임, 썸네일 전략 등을 대화형으로 물어보고, 채널 설정 파일을 자동 생성합니다.

### 4. 대본 만들기

```
Claude에게: "대본 만들어줘"
```

레퍼런스 영상 URL을 주면 수집부터 최종 대본까지 자동으로 진행됩니다.

시작하면 첫 줄에 ✅ 시작 배너가 출력됩니다:

```
✅ 대본 스킬 v2.0.0 | 채널: 끌루 경제TV | 모드: 풀·ask | 팩트체크 ON | 에이전트 4종 로드
```

**이 배너가 안 뜨면 잘못된 폴더입니다.** VS Code에서 `autoworker-script` 폴더 자체를 열었는지 확인하고, "점검해줘"를 실행하세요.

---

## 프로젝트 구조

```
autoworker-script/
├── .claude/
│   ├── skills/                        # Claude 스킬 정의
│   │   ├── script-pd/SKILL.md         #   대본 제작 PD (상태머신 오케스트레이터)
│   │   ├── channel-setup/SKILL.md     #   채널 생성 스킬
│   │   ├── setup/SKILL.md             #   "세팅해줘" — 최초 환경 설정
│   │   ├── doctor/SKILL.md            #   "점검해줘" — 설치 상태 진단
│   │   ├── update/SKILL.md            #   "업데이트해줘" — 새 버전 적용
│   │   └── reset/SKILL.md             #   "초기화해줘" — 도구 파일 원복
│   └── agents/                        # 역할별 에이전트 정의 (4종)
│       ├── video-analyst.md           #   레퍼런스 영상 분석
│       ├── data-researcher.md         #   팩트체크 + 리서치
│       ├── script-writer.md           #   대본 집필 (통짜 순차, 클린 컨텍스트)
│       └── script-reviewer.md         #   대본 검수 (verdict + 신규 주장 검증)
│
├── channels/                          # 채널별 설정 + 프로젝트
│   ├── _template.json                 #   settings.json 템플릿
│   └── cclue-economy/                 #   예시 채널 (경제) — 참고용
│       ├── config/
│       │   ├── settings.json          #     채널 식별 + 썸네일 이미지 생성 스위치
│       │   ├── profile.md             #     채널 성격 (톤, 서사, 관점, 메시지, 러닝타임)
│       │   ├── workflow.json          #     auto/ask 모드 설정
│       │   └── thumbnail-strategy.json #    썸네일 전략
│       └── projects/
│           └── {project-name}/        #     (예: samsung-crisis)
│               ├── _refs/             #       레퍼런스 수집 결과
│               ├── _script/           #       대본 단계별 산출물 (중간 작업물)
│               └── output/            #       완성본 폴더 (01_대본 · 02_썸네일제목 · 03_업로드정보)
│
├── prompts/                           # 파이프라인 프롬프트
│   ├── pd-script.md                   #   대본 제작 상세 절차
│   ├── pd-agents.md                   #   에이전트 호출 사양
│   ├── pd-templates.md                #   산출물 포맷 템플릿
│   ├── creative-strategy.md           #   크리에이티브 전략 (5-Phase)
│   ├── ctr-reference.md               #   제목/썸네일 CTR 이론
│   ├── thumbnail-design.md            #   썸네일 프롬프트 규칙
│   ├── reference-analyze.md           #   영상 분석 프레임워크
│   ├── reference-patterns.md          #   패턴 추출 규칙
│   ├── data-research.md               #   데이터 검증 워크플로우
│   ├── script-review-checklist.md     #   대본 검수 체크리스트 (5항목)
│   ├── tts-rules.md                   #   TTS 전처리 규칙
│   └── youtube-meta.md                #   완성본 문서(썸네일제목·업로드정보) 규칙
│
├── scripts/                           # Python 코드
│   ├── collect.py                     #   yt-dlp 레퍼런스 수집
│   ├── finalize.py                    #   draft → script.txt 변환 + TTS-safe 검증·보정
│   └── src/
│       ├── project_resolver.py        #   프로젝트 경로 해석
│       ├── merge_draft.py             #   파트 조립 + Hook 변형 리포트
│       ├── validate_draft.py          #   분량 밴드 검증
│       └── thumbnail/
│           └── generate_thumbnails.py #   썸네일 이미지 생성 (옵션 — 기본 꺼짐)
│
├── CLAUDE.md                          # Claude 지시사항 (자동으로 읽음)
├── CHANGELOG.md                       # 버전별 변경사항 ("업데이트해줘"가 읽고 보고)
├── VERSION                            # 배포 버전
├── requirements.txt                   # Python 의존성 (yt-dlp)
└── README.md                          # 이 파일
```

---

## 산출물

완성본은 전부 **`output/` 폴더 하나**에 모입니다. 번호 순서대로 쓰면 됩니다.

| 파일 | 설명 |
|------|------|
| `output/01_대본.txt` | **최종 대본** — 영상 제작 사이트에 업로드할 파일 |
| `output/02_썸네일제목.md` | 영상 방향 요약 + 제목 후보 + 썸네일 문구·이미지 프롬프트 |
| `output/03_업로드정보.md` | 제목, 설명글, 태그, 고정 댓글 + 🔗 주요 출처 (핵심 3~4개) |
| `_script/review.md` | 검수 리포트 (팩트체크 결과, 지적사항, 수정 내역) — 참고용 |

---

## 주요 명령어

| 말하면 되는 것 | 하는 일 |
|----------------|---------|
| `"채널 만들어줘"` | 대화형으로 채널 설정 생성 |
| `"대본 만들어줘"` | 전체 파이프라인 실행 |
| `"이어서 해줘"` | 중단된 지점부터 재개 |
| `"대본 다시 써줘"` | 해당 단계만 재실행 |
| `"30분짜리로 만들어줘"` | 타겟 러닝타임 지정하여 실행 |
| `"세팅해줘"` | 최초 설치 — 폴더 점검·가상환경·yt-dlp·동작 테스트 |
| `"점검해줘"` | 설치 상태 진단 (✅❌ 리포트) — 문제가 생기면 제일 먼저 |
| `"업데이트해줘"` | 새 버전 zip 적용 — 채널·작업물은 그대로 보존 |
| `"초기화해줘"` | 도구 파일을 원본 상태로 복구 — 채널·작업물은 그대로 보존 |
| `"타임스탬프 채워줘"` | 완성 영상을 분석해 설명글에 챕터 타임스탬프 추가 (영상 제작 후, 영상 파일과 함께) |

💡 대본 하나가 끝나면, 다음 대본은 **새 세션**(`/clear`)에서 시작하세요. 이전 대본의 맥락이 섞이는 것을 방지합니다.

---

## 모드

채널의 `workflow.json`에서 설정합니다.

- **auto**: 전 과정 자동. 결과만 보고.
- **ask**: 전략 단계(컨셉/제목/Hook/핵심 메시지)에서 3안을 제시하고 선택하게 합니다. 나머지는 auto.

---

## 러닝타임과 분량

- 타겟 러닝타임 우선순위: ①직접 말한 값 → ②profile.md의 "기본 러닝타임" → ③Claude가 "몇 분짜리로 만들까요?"라고 물어봄
- 분량 환산 기준: **1분 ≈ 500자** (채널 profile.md에 실측 분당 글자수를 기록하면 그 값을 우선 사용)
- **60분 초과 레퍼런스 영상은 기본적으로 수집하지 않습니다** — 분석 단계에서 사용량 리밋을 크게 소모하기 때문입니다. 정말 필요하면 Claude가 확인 후 `--allow-long`으로 진행합니다.

---

## 썸네일 이미지 자동 생성 (옵션)

기본값은 **프롬프트까지만 생성**(`02_썸네일제목.md`에 정리됨)하고 이미지는 만들지 않습니다.
Gemini API 키가 있으면 이미지까지 자동 생성할 수 있습니다 (이미지는 `output/썸네일/`에 저장):

1. 추가 패키지 설치: `pip install google-genai Pillow`
2. 루트에 `.env` 파일 생성: `GEMINI_API_KEY=발급받은키`
3. 채널 `config/settings.json`에서 `"thumbnail": { "generate_images": true }`로 변경

---

## 트러블슈팅

문제가 생기면 우선 **"점검해줘"** — 나온 결과를 캡처해서 조교에게 보내는 것이 가장 빠른 해결 방법입니다.

### yt-dlp 에러 / 429 Too Many Requests

YouTube가 짧은 시간에 요청이 많으면 일시적으로 차단합니다. 영구 차단이 아닙니다.

- **해결**: 5~15분 기다렸다가 다시 시도
- **재개**: "이어서 해줘"하면 이미 수집된 영상은 건너뛰고 남은 것만 수집
- **예방**: 일반적인 사용(영상 3~5개 연속 수집)에서는 거의 발생하지 않음

### 레퍼런스 수집이 아예 안 될 때

yt-dlp가 어떤 이유로든 동작하지 않으면, 대본을 직접 붙여넣어서 진행할 수 있습니다.
Claude에게 "대본 만들어줘"를 하면, 수집 실패 시 자동으로 "대본을 직접 붙여넣어 주세요"라고 안내합니다.
유튜브 영상 페이지에서 자막/스크립트를 복사해서 붙여넣으면 됩니다.

### yt-dlp 버전 경고

`Your yt-dlp version is older than 90 days` 경고가 뜨면:
```bash
# macOS/Linux
.venv/bin/pip install -U yt-dlp
# Windows
.venv\Scripts\pip install -U yt-dlp
```

---

## 참고사항

- Python 실행은 항상 가상환경의 python 사용 (macOS: `.venv/bin/python`, Windows: `.venv\Scripts\python`)
- `.venv`는 **컴퓨터마다 새로 만들어지는 폴더**입니다. 폴더를 다른 컴퓨터로 옮기거나 공유할 때 `.venv`는 복사하지 마세요 — 섞여 들어가도 "대본 만들어줘" 또는 "세팅해줘"가 현재 OS(macOS/Windows)에 맞게 자동으로 다시 만듭니다
- 레퍼런스 수집: 영상 원어 자동자막 사용 — 영어·일본어 등 외국어 영상도 원어 대본으로 수집 (분석은 원어 그대로, 최종 대본은 한국어)
- 분량 기준: 약 500자/분 (profile.md 실측치가 있으면 그 값 우선)
- 프로젝트 이름은 영어 kebab-case (예: `baemin-collapse`) — Claude가 자동으로 정합니다
- `channels/*/projects/`는 `.gitignore`에 포함 — 각자의 프로젝트 데이터는 git에 올라가지 않음
