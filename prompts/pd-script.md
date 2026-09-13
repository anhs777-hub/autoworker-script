# 대본 제작 — 상세 절차

`{P}` = `channels/{채널}/projects/{프로젝트}`
`{VENV_PYTHON}` = macOS/Linux: `.venv/bin/python` | Windows: `.venv\Scripts\python`

---

## COLLECT

**YouTube 레퍼런스 수집.**

1. 사용자에게 YouTube URL 수집 (또는 이미 있으면 확인)
   - 제목 확인 필요 시: `yt-dlp --get-title URL` (YouTube는 JS 렌더링이라 WebFetch 불가)
2. 실행:
```bash
{VENV_PYTHON} scripts/collect.py --project {프로젝트} --channel "{채널}" URL1 URL2 ...
```
3. 결과: `_refs/{NNN}/` 에 meta.md, transcript.txt, thumbnail.webp

### 60분 초과 영상 처리

collect.py는 **60분 초과 영상을 기본적으로 스킵**하고 경고를 출력한다 (exit 2 — 긴 영상은 분석 단계에서 사용량 리밋을 크게 소모).
- 스킵이 발생하면: 사용자에게 해당 영상 제목·길이와 리밋 소모 위험을 알리고 **진행 의사를 확인**한다
- 사용자가 진행을 원하면 해당 URL만 `--allow-long`을 붙여 재실행:
```bash
{VENV_PYTHON} scripts/collect.py --project {프로젝트} --channel "{채널}" --allow-long URL
```

---

## ANALYZE

**레퍼런스 영상 분석. 에이전트: video-analyst**

1. `_refs/*/analysis.md`가 없는 영상 목록 확인
2. **전체 동시 병렬 실행** (run_in_background: true, **TaskOutput 사용 금지** → Glob으로 확인)
3. 각 에이전트에게 전달:
   - 채널 프로필 (`channels/{채널}/config/profile.md`)
   - 분석 프롬프트 (`prompts/reference-analyze.md`)
   - 영상 데이터 (meta.md + transcript.txt + thumbnail.webp)
4. 출력: 각 `_refs/{NNN}/analysis.md`
5. 완료 후 요약 보고

---

## DATA_PREP

**데이터 검증/리서치(에이전트 백그라운드) + 패턴 추출(PD 직접). 병렬성 유지 — researcher를 먼저 발사한 뒤 PD가 패턴을 추출한다.**

### 1) data-researcher 에이전트 (백그라운드 — 먼저 발사)

1. 에이전트 1개 호출 (run_in_background: true, WebSearch 사용)
2. 전달: 채널 프로필 + `prompts/data-research.md` + 모든 transcript.txt + 모든 analysis.md
3. 출력: `{P}/_script/factcheck.md` + `{P}/_script/verified-data.md` (추가 리서치 포함)

### 2) 패턴 추출 (PD 직접 — researcher 완료를 기다리지 않고 바로 수행)

1. 최소 2개 analysis.md 필요 (부족하면 알림)
2. Read: `prompts/reference-patterns.md` (Lazy Load) + 모든 `_refs/*/analysis.md` + `_refs/*/meta.md`
3. PD가 직접 `{P}/_script/patterns.md` 작성 — reference-patterns.md의 규칙과 출력 형식을 그대로 따른다

### 완료 확인

- `_script/patterns.md` 존재 확인 (PD 작성 완료)
- `_script/verified-data.md`에 "## 추가 리서치" 존재 확인 (researcher 완료 — 없으면 대기)

---

## STRATEGY

**크리에이티브 전략 통합 설계 + 썸네일 프롬프트. PD 직접 수행 (5-Phase).**

입력: `_script/patterns.md` + `_script/verified-data.md` + 채널 프로필 + `config/pd-guide.md`(있으면)

Read (Lazy Load): `prompts/creative-strategy.md` + `prompts/ctr-reference.md` + `prompts/thumbnail-design.md`

### 5-Phase 수행 (PD 직접)

`prompts/creative-strategy.md`의 Phase 1~5를 PD가 직접 수행한다.
- 3개의 완전한 크리에이티브 패키지 생성 — 각 패키지에 **핵심 메시지(교훈)** 필드 포함 (creative-strategy.md "핵심 메시지(교훈) 설계" 규칙)
- 메시지는 레퍼런스가 아니라 **profile의 "채널 메시지 방향" + verified-data의 신규 데이터**에서 도출. 레퍼런스와 동일한 교훈이면 감점

### auto 모드

1. Phase 4 자체 평가로 최적안 확정 (핵심 메시지 포함) → `_script/concept.md` + `_script/hook-intro.md` 저장
2. Phase 5 수행 → `{P}/_script/thumbnail-prompts.json` 저장
3. 결과 요약 보고
4. 백그라운드 썸네일 이미지 생성 (fire-and-forget, thumbnail-prompts.json 존재 시):
```bash
{VENV_PYTHON} scripts/src/thumbnail/generate_thumbnails.py \
  --project {프로젝트} --channel "{채널}"
```
   - `run_in_background: true`로 실행, 완료 대기 없이 즉시 다음 단계 진행
5. OUTLINE 진행

### ask 모드

1. 3 패키지 → `_script/_strategy_candidates.md` 저장
2. 3 패키지 사용자에게 제시 (컨셉+제목+Hook+**핵심 메시지** 간결 비교)
3. 사용자 선택/수정/혼합:
   - "B로 해줘" → B 그대로 채택
   - "A 앵글에 B 제목으로" → 혼합
   - "B 컨셉에 A 교훈으로" → 메시지 혼합
   - "A 좋은데 Hook 좀 바꿔줘" → 수정
4. 확정 → `_script/concept.md` + `_script/hook-intro.md` 저장
5. Phase 5 수행 → `{P}/_script/thumbnail-prompts.json` 저장
6. 백그라운드 썸네일 이미지 생성 (fire-and-forget, thumbnail-prompts.json 존재 시):
```bash
{VENV_PYTHON} scripts/src/thumbnail/generate_thumbnails.py \
  --project {프로젝트} --channel "{채널}"
```
   - `run_in_background: true`로 실행, 완료 대기 없이 즉시 다음 단계 진행
7. OUTLINE 진행

---

## OUTLINE

**통합 기획서 작성. PD 직접 수행.**

입력: `_script/concept.md` + `_script/hook-intro.md` + `_script/patterns.md` + `_script/verified-data.md` + 채널 프로필

### ask 모드
1. 통합 기획서 초안 제시 (포맷은 `prompts/pd-templates.md` 참조, auto와 동일한 셀프체크 10항목 적용)
2. 사용자 검토/피드백 → 수정 → 확정
3. `_script/outline.md` 저장 → 데이터 갭 확인 → DRAFT 진행

### auto 모드
1. 오케스트레이터가 outline.md 직접 생성 (셀프체크 10항목 내장):
   1. 제목→구조 정합성
   2. 감정 전략 정합성
   3. 완시율 설계
   4. 핵심약속 이행
   5. 스테이크 상승
   6. 재참여 포인트 (2~3분 간격)
   7. 데이터 활용 검증 (verified-data.md에 존재하는 데이터만) — **필요한데 없는 데이터는 "데이터 갭"으로 목록화** (아래 보충 리서치 절차)
   8. 분량 현실성 (파트 범위 합 ↔ 타겟 러닝타임 — 분당 글자수는 profile 실측치 우선, 없으면 500자)
   9. 대본 작성 가능성
   10. 메시지 배치·완결 (concept.md의 핵심 메시지 — 중간 파트 1~2곳 복선 + 클로징 완결 배치)
2. `_script/outline.md` 저장 → 데이터 갭 확인 → DRAFT 진행

### 제목→구조 제약 규칙

확정 제목이 본문 구조를 제약한다. 반드시 확인:

| 제목 패턴 | 구조 제약 |
|-----------|----------|
| "N가지 이유/방법/실수" | 정확히 N개 섹션 |
| "~의 몰락/추락/붕괴" | 시간순 서사 |
| "A vs B" 비교 | 비교 프레임워크 |
| "진짜 이유/숨겨진 비밀" | 미스터리 구조 (표면→단서→진실) |
| "~하는 법" | 프로세스 구조 |

concept.md의 서사 유형과 확정 제목이 호환되는지도 확인한다. 비호환 시 서사 유형을 제목에 맞춰 조정.

### 타겟 러닝타임 결정 (우선순위)

OUTLINE에서 타겟 러닝타임을 확정하고 outline.md `## 1. 기획 뼈대`에 **분 + 목표 글자수**로 기록한다 (목표 글자수는 validate_draft 밴드 기준이 됨):

1. **사용자 지시** — 대화에서 "30분짜리로" 등 명시하면 최우선. 프로젝트 진행 중 언제 말해도 OUTLINE 전이면 반영
2. **채널 기본값** — `config/profile.md`의 "기본 러닝타임" 항목 (있으면)
3. **사용자에게 질문** — 위 둘 다 없으면 **"몇 분짜리로 만들까요?"**라고 묻는다 (auto 모드여도 이 질문은 한다). 보통 프로젝트 초기화 때 이미 물어봤으므로(SKILL.md §1) 그 답을 쓰면 되고, 여기까지 왔는데 값이 없으면 지금 묻는다. **자동 결정 폴백은 없다 — PD가 임의로 정하지 않는다**

**환산 기준**: profile.md에 실측 분당 글자수가 있으면 그 값 우선, 없으면 1분 ≈ 500자. TTS 완료 후 실제 오디오 길이가 최종 러닝타임이다.

### 본문 구조 가이드
- 모든 파트가 핵심약속 이행에 기여
- 핵심 포인트 3~5개를 가치 상승 순서로 배열
- 파트 전환 직전에 오픈루프 배치
- 1~2분 간격으로 소규모 리텐션 장치(질문, 반전, 감정 전환) 배치
- patterns.md의 검증된 리텐션 장치는 **장치 유형 + 배치 위치만** 리텐션 설계 섹션에 기록한다 — 레퍼 문장 발췌 금지, 문장은 집필 시 새로 작성
- **파트별 고유 장치 배정**: 비유·사례·전환구·리텐션 장치 유형을 **파트 전속**으로 배정한다 — 같은 비유/사례/장치 유형이 두 파트에 배정되면 집필에서 중복이 발생한다
- **파트별 분량은 고정값이 아닌 범위로 배정** (예: "2,000~3,500자 — 핵심 파트"). 범위 폭·크기가 중요도 정보가 된다 — 핵심 파트는 크게, 브릿지 파트는 작게. writer가 범위 안에서 흐름 따라 자유 배분하되 전체 합계로 타겟 러닝타임을 준수

### 리텐션 설계 가이드
- **재참여 포인트**: 파트 전환점마다 + 긴 파트 중간에 배치하여 2~3분 간격 유지. 타겟 러닝타임 전체에 걸쳐 빈 구간 없이 분포
- **스테이크 상승**: 파트가 진행될수록 "왜 이게 중요한가"의 규모가 커져야 함
- **감정 목표**: 각 파트별 시청자의 감정 상태를 명시 (예: 충격→분석→공감→경각심)

### 데이터 갭 보충 리서치 (ask/auto 공통 — outline.md 저장 후, DRAFT 진입 전)

리서치(DATA_PREP)는 영상 방향이 정해지기 전에 끝나므로, outline이 필요로 하는 데이터가 verified-data.md에 없을 수 있다. 셀프체크 ⑦에서 목록화한 데이터 갭으로 판단:

- **갭 없음** → 바로 DRAFT (보충 비용 0)
- **갭 있음** → data-researcher를 **보충 리서치 모드**로 1회 호출 (run_in_background: true):
  1. 전달: `prompts/data-research.md` + 데이터 갭 목록(타겟 질의 형태) + `{P}/_script/verified-data.md` 경로
  2. researcher는 타겟 검색·검증 후 verified-data.md 말미에 `## 보충 리서치` 섹션으로 append
  3. 완료 확인: verified-data.md에 `## 보충 리서치` 존재 (Grep) → DRAFT 진입

**저장 후: 사용자 확인 없이 (데이터 갭 보충만 거쳐) 바로 DRAFT 단계로 자동 진행한다.**

---

## DRAFT

**대본 초안 작성. 에이전트: script-writer 1개 — hook부터 클로징까지 통째 순차 집필 (클린 컨텍스트).**

### 클린 컨텍스트 원칙 (필수)

script-writer는 **레퍼런스 문장을 한 번도 본 적 없는 컨텍스트**에서 문장을 써야 한다.
- **전달하는 입력 (전부 — 파일 경로로)**: `_script/outline.md` + `_script/concept.md` + `_script/hook-intro.md` + `_script/verified-data.md` + 채널 프로필
- **전달 금지**: `patterns.md` · `analysis.md` · `transcript.txt` · `_refs/` — 내용은 물론 경로도 프롬프트에 언급하지 않는다

### script-writer 호출 (1개)

1. script-writer 에이전트 1개 호출:
   - 전달: 위 입력 5개 경로 + 출력 디렉토리(`{S}`)
   - writer가 `_draft_part0.md`(Hook & Intro — hook-intro.md 원문으로 시작)부터 `_draft_part{N}.md`(클로징)까지 **순서대로** 작성
2. 완료 확인: `ls {S}/_draft_part*.md`로 파일 수 == 본문 파트 수 + 1 (part0 = Hook & Intro)

### draft.md 조립 + Hook 변형 리포트

```bash
{VENV_PYTHON} scripts/src/merge_draft.py \
  --hook-intro {S}/hook-intro.md \
  --parts-dir {S} \
  --output {S}/draft.md
```

- 파트 파일들을 순서대로 조립하고, draft 시작부 vs hook-intro.md **변형 diff를 리포트**한다 (경고일 뿐 게이트 아님 — 자연스러운 다듬기 허용)
- ask 모드에서 변형이 크다고 리포트되면(유사도 85% 미만) 사용자에게 diff를 표시한다

### 분량 검증 게이트 (REVIEW 전 필수)

```bash
{VENV_PYTHON} scripts/src/validate_draft.py {S}/outline.md {S}/draft.md
```

검사 기준: **전체 합계 90~115% 밴드** + 파트별 느슨한 하한(배정 하한의 70% — 파트 스킵 방지). 파트별 고정 쿼터 검사는 하지 않는다.

- **exit 0** → REVIEW 진행
- **exit 1** → 보충/압축 재작성 (1회):
  1. **파트 하한 미달**: outline의 미사용 사례·verified-data의 미사용 데이터 식별 → script-writer 재호출로 해당 `_draft_part{N}.md`만 보충 재작성 (문장 늘려쓰기 금지)
  2. **전체 합계 초과(115%↑)**: 초과 기여가 큰 파트를 압축 재작성 (중복·필러 제거 우선)
  3. merge_draft.py 재실행 → validate_draft.py 재검증 (1회)

---

## REVIEW_FINALIZE

**검수 + 확정. 에이전트: script-reviewer(verdict 권한 + 신규 주장 WebSearch 검증). 검수는 최종 1회만 — TTS 비용 발생 전 마지막 게이트.**

1. **script-reviewer 에이전트 호출:**
   - 전달: `_script/draft.md` + `_script/outline.md` + `_script/concept.md` + `_script/verified-data.md` + `prompts/script-review-checklist.md` + 분량 린터 결과(validate_draft 출력 요약 — reviewer는 분량 재검사 안 함)
   - 출력: `{P}/_script/review.md` (체크리스트 + 심각도 분류 + 신규 주장 검증 결과 + verdict)
   - reviewer가 신규 주장을 식별하면 즉시 WebSearch로 검증하여 review.md에 포함

2. **verdict 확인:**
   - review.md의 `verdict:` 확인
   - `verdict: 통과` → finalize.py 실행
   - `verdict: 수정` → 리비전 1회

3. **리비전 (최대 1회):**
   - review.md 치명적 항목 (신규 주장 ❌/⚠️ 포함) 정리
   - script-writer 재호출 (클린 컨텍스트 입력 + 수정 지시) → 해당 `_draft_part*.md` 재작성 → merge_draft.py 재실행
   - finalize.py 실행 (재검수 없이 확정)
   - **리비전 완료 후 review.md 말미에 `## 리비전 반영 내역` 섹션을 append** (PD가 직접 작성): 재작성한 파트, 반영한 치명적 항목별 처리 결과, 미반영 항목과 사유 — 검수 리포트만 봐도 무엇이 왜 고쳐졌는지 보이게 한다

4. 확정 후 finalize:
```bash
{VENV_PYTHON} scripts/finalize.py --project {프로젝트} --channel "{채널}"
```
   - finalize.py가 마크다운 제거 + **대본 작성 가이드 6개조를 기계 검증·자동 보정**하고 위반 리포트를 출력한다 (①온점 뒤 띄어쓰기 ②따옴표 제거 ③문단 줄바꿈 유지 ④특수문자·이모지 제거 ⑤URL·이메일 제거 ⑥단어 뒤 괄호 제거)
   - 리포트에 보정 건수가 있으면 요약해서 보고한다 (보정은 이미 완료된 상태 — 재실행 불필요)
5. 결과: `{P}/_script/script.txt` (순수 텍스트, 문단은 빈 줄로 구분) + `{P}/output/01_대본.txt` 사본 (finalize.py가 자동 생성)

6. **TTS 검수 (프롬프트 이중 검수):**
   - `{P}/_script/script.txt` 읽기
   - `prompts/tts-rules.md` 규칙(6개조와 동일 기준)에 따라 finalize.py가 놓친 형식 문제만 정리 — **내용(문장·단어·어순) 변경 금지**
   - 수정할 것이 있으면 정리된 텍스트를 `{P}/_script/script.txt`와 `{P}/output/01_대본.txt` **둘 다**에 덮어쓰기 (사본이 낡으면 안 됨), 없으면 그대로 통과
   - 완료 후 METADATA 진행

---

## METADATA

**완성본 문서 생성 (02_썸네일제목 + 03_업로드정보). PD 직접 수행 (경량 단계 — 에이전트 호출 없음).**

상세 규칙 → `prompts/youtube-meta.md` (Lazy Load).

1. Read: `_script/concept.md`(확정 제목·앵글·핵심 약속·타겟·썸네일 텍스트 후보) + `_script/_strategy_candidates.md`(있으면 — 대안 제목용) + `_script/outline.md` + `_script/verified-data.md` + `_script/thumbnail-prompts.json` + `config/settings.json`
2. youtube-meta.md 규칙대로 두 파일 생성 (`{P}/output/`은 finalize.py가 이미 생성):
   - `{P}/output/02_썸네일제목.md` — 영상 방향 요약(핵심 각도·약속·타겟) + 제목 후보 + 썸네일 문구 + 이미지 프롬프트
   - `{P}/output/03_업로드정보.md` — 제목/설명글/태그/고정 댓글 (설명글에 verified-data.md 기반 **"🔗 주요 출처"** 필수 포함 — 핵심 출처 3~4개만 선별, 링크 최대 4개)
3. 저장 순서 **02 → 03** (`03_업로드정보.md`가 DONE 마커 — 반드시 마지막에 저장)
4. 저장 후 DONE 보고 (SKILL.md §5 형식)
