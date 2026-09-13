---
name: update
description: 새 버전 적용 스킬. Downloads의 새 autoworker-script zip을 찾아 도구 파일(.claude/·prompts/·scripts/·루트 문서)만 교체하고 channels/(채널 설정·작업물)는 보존한다. 적용 후 CHANGELOG 요약 보고. 트리거: "업데이트해줘", "새 버전 받았어", "update".
---

# Update Skill

새 배포 zip을 현재 폴더에 안전하게 적용한다. **채널 설정과 작업물(channels/)은 절대 건드리지 않는다.** 수동 폴더 교체(1기 방식)를 대체한다.

## 교체 범위

| 교체 (도구 파일) | 보존 (절대 건드리지 않음) |
|------|------|
| `.claude/` 전체 | `channels/` 전체 (아래 예외 1개 제외) |
| `prompts/` 전체 | `channels/*/projects/` — 대본 작업물 |
| `scripts/` 전체 | `.venv/`, `.env` |
| 루트: `README.md`·`CLAUDE.md`·`CHANGELOG.md`·`VERSION`·`requirements.txt` | |

- 예외: `channels/_template.json`은 도구 파일이므로 교체한다 (학생이 수정할 파일이 아님)
- 예시 채널 `channels/cclue-economy/`도 **건드리지 않는다** — 학생이 고쳐 쓰고 있을 수 있음

## 절차

### 1. 현재 버전 확인
루트 `VERSION` 읽기 → `{cur}`

### 2. zip 찾기
```
{VENV_PYTHON} -c "import os; from pathlib import Path; d=Path.home()/'Downloads'; zs=sorted(d.glob('autoworker-script*.zip'), key=os.path.getmtime, reverse=True) if d.exists() else []; print('\n'.join(str(z) for z in zs) if zs else 'NONE')"
```
- 없으면 안내 후 종료:
  > Downloads 폴더에서 zip을 찾지 못했습니다. 오토워커 2기 드라이브에서 최신 zip을 받아 Downloads에 두고 다시 "업데이트해줘" 해주세요. 다른 곳에 받으셨다면 그 경로를 알려주세요.

### 3. zip 검증 (아무것도 건드리기 전에 전부 확인)
- Python `zipfile`로 열어 확인: 최상위가 `autoworker-script/` 단일 폴더인지, 그 안에 `VERSION`·`CLAUDE.md`·`prompts/`·`scripts/`·`.claude/`가 있는지 — 하나라도 어긋나면 중단 ("정상 배포 zip이 아닙니다")
- zip 내부 `VERSION` 읽기 → `{new}`
- 버전 비교:
  - `{new}` > `{cur}` → 진행
  - `{new}` = `{cur}` → "이미 v{cur}입니다. 파일을 원래 상태로 되돌리는 게 목적이면 '초기화해줘'를 실행하세요." 종료
  - `{new}` < `{cur}` → 다운그레이드 경고. 사용자가 명시적으로 원할 때만 진행

### 4. 사용자 컨펌 (필수 — 생략 금지)
> v{cur} → v{new} 업데이트를 진행합니다. 채널 설정·대본 작업물(channels/)은 그대로 보존됩니다. 진행할까요?

### 5. 적용 (전부 Python — os·shutil·zipfile·tempfile)
1. 임시 폴더에 압축 해제
2. `.claude/` → `prompts/` → `scripts/` 순서로 폴더별 교체:
   - 기존 폴더를 `_old_.claude` 식으로 이름 변경(`shutil.move`) → 새 폴더 복사(`shutil.copytree`) → 성공 확인 후 `_old_` 삭제(`shutil.rmtree`)
   - 중간 실패 시 `_old_`를 원래 이름으로 되돌리고 중단
3. 루트 5파일(`README.md`·`CLAUDE.md`·`CHANGELOG.md`·`VERSION`·`requirements.txt`) + `channels/_template.json` → `shutil.copy2`
4. 임시 폴더 삭제
5. `{VENV_PIP} install -U -r requirements.txt` (새 버전에서 의존성이 늘었을 수 있음)

### 6. 보고
- 새 `CHANGELOG.md`에서 `{cur}` **이후** 버전 섹션들을 읽어 "이번 업데이트로 좋아진 것"을 3~5줄로 보고 (CHANGELOG의 학생용 문장을 그대로 활용)
- 마지막 줄 고정:
  > 업데이트 완료. **새 세션에서 사용하세요** (`/clear` 입력 후 "대본 만들어줘").

## 안전 규칙

- 3번 검증 통과 전에는 어떤 파일도 삭제·교체하지 않는다
- `channels/` 하위는 `_template.json` 외 어떤 것도 덮어쓰거나 삭제하지 않는다
- 이 폴더 밖은 zip 읽기 외에 건드리지 않는다
- 교체 중 오류 → 즉시 멈추고 현재 상태 보고 + "'점검해줘' 결과를 캡처해서 조교에게 보내주세요"
