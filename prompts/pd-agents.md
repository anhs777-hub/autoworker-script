# PD 에이전트 호출 사양

---

## 에이전트별 스펙

| 에이전트 | model | 실행 방식 | 참조 프롬프트 |
|----------|-------|-----------|-------------|
| video-analyst | opus | 전체 동시 병렬 | prompts/reference-analyze.md |
| data-researcher | opus | 1개 (백그라운드, WebSearch. OUTLINE 데이터 갭 시 보충 모드 1회 추가 호출) | prompts/data-research.md |
| script-writer | opus | 1개 — 전체 순차 집필 (클린 컨텍스트: patterns/analysis/transcript 전달 금지) | outline.md + concept.md + hook-intro.md + verified-data.md + 채널 프로필 |
| script-reviewer | opus | 1개 (verdict 권한, WebSearch. 분량은 린터 결과 입력 — 재검사 안 함) | prompts/script-review-checklist.md |

**에이전트가 아닌 것**: 패턴 추출(DATA_PREP) · 크리에이티브 전략(STRATEGY) · outline(OUTLINE) · 업로드 정보(METADATA)는 PD가 직접 수행한다 — 기획은 레퍼런스를 아는 컨텍스트가 하는 게 일이므로 격리 실익이 없다. 격리가 실익인 것(레퍼 분석 · 리서치 · 집필 · 검수)만 에이전트로 위임한다.

---

## 병렬 호출 패턴

독립적인 에이전트 N개를 동시에 실행:
1. 전체 대상 목록에 대해 Agent tool 동시 호출 (run_in_background: true)
2. 출력 파일 존재 여부를 Glob으로 확인
3. 모든 파일 생성 확인 후 다음 단계

**배치 분할 하지 않는다** — 에이전트들이 독립적이고 TaskOutput을 사용하지 않으므로 PD 컨텍스트 부하 없음.

---

## Task tool 호출 시 전달 내용

에이전트에게 항상 전달:
1. **역할** (agents/*.md에 정의된 역할 설명)
2. **도메인 프롬프트** (prompts/*.md 내용 또는 파일 경로)
3. **프로젝트 데이터** (파일 경로 — 에이전트가 직접 Read)
4. **출력 경로** (결과 파일 절대 경로)

가능하면 **파일 내용을 prompt에 임베드하지 말고 파일 경로를 전달**하여 PD 컨텍스트를 절약한다.

---

## 결과 확인 규칙 (필수)

- **TaskOutput 절대 사용 금지**: 에이전트 전체 transcript(base64 이미지 포함)가 PD 컨텍스트에 덤프되어 컨텍스트 폭발을 일으킴
- **대신**: 출력 파일 존재 여부를 Glob으로 확인 → 필요한 부분만 Read
- 에이전트가 파일을 잘 생성했는지만 확인하면 충분
- 에이전트 실패 시: 해당 에이전트만 재실행 (파일 미생성으로 감지)
