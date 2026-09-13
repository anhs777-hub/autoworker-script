---
name: setup
description: 환경 세팅 스킬. OS 감지 → 폴더 위치 점검(한글 경로·OneDrive·이중 폴더) → Python 가상환경 생성 → yt-dlp 설치 → 동작 테스트 1건 → ✅ 체크리스트 출력. 트리거: "세팅해줘", "설치해줘", "환경 설정해줘", "setup".
---

# Setup Skill

압축을 막 푼 폴더를 대본 제작이 가능한 상태로 만든다.
**여러 번 실행해도 안전하다** — 이미 완료된 단계는 확인만 하고 넘어간다.

`{PY}` = 시스템 Python (STEP 0에서 결정) · `{VENV_PYTHON}`·`{VENV_PIP}` = CLAUDE.md 크로스 플랫폼 규칙 참조

## 원칙

- 파일/폴더 조작은 셸 명령 대신 **Python(os·shutil)** — CLAUDE.md 크로스 플랫폼 규칙
- 각 STEP 결과를 한 줄씩 보고하며 진행, 마지막에 ✅ 체크리스트로 종합
- 한 STEP이 실패해도 진행 가능한 STEP은 끝까지 진행하고, 체크리스트에서 ❌로 표시

## STEP 0. OS·Python 확인

1. OS는 실행 환경에서 감지 (macOS / Windows)
2. 시스템 Python 찾기 — 아래 순서로 시도, 처음 성공하는 것이 `{PY}`:
   - `python --version` → `python3 --version` → (Windows) `py --version`
3. 3.10 미만이거나 Python이 없으면 **여기서 중단**하고 안내:
   > Python 3.12 설치가 필요합니다. python.org에서 설치하세요. **Windows는 설치 첫 화면에서 "Add python.exe to PATH"를 반드시 체크**하세요. 설치 후 VS Code를 완전히 껐다 켜고 다시 "세팅해줘"라고 해주세요. 잘 안 되면 이 화면을 캡처해서 조교에게 보내주세요.

## STEP 1. 폴더 위치 점검 — 반드시 가상환경 생성보다 먼저

(가상환경은 생성 위치의 절대경로를 품고 있어서, 폴더를 옮기려면 venv를 만들기 **전에** 옮겨야 한다)

```
{PY} -c "import os; p=os.getcwd(); print('PATH:', p); print('ROOT:', 'OK' if os.path.exists('CLAUDE.md') and os.path.exists('VERSION') else 'MISSING'); print('NESTED:', 'YES' if os.path.exists(os.path.join('autoworker-script','CLAUDE.md')) else 'NO'); print('ASCII:', 'OK' if p.isascii() else 'NON_ASCII'); print('ONEDRIVE:', 'YES' if 'onedrive' in p.lower() else 'NO')"
```

| 결과 | 대응 |
|------|------|
| ROOT MISSING + NESTED YES | **이중 폴더** — 압축이 폴더 안에 폴더로 풀린 상태. "VS Code에서 안쪽 `autoworker-script` 폴더를 다시 열고 '세팅해줘'를 해주세요" 안내 후 중단 |
| ROOT MISSING + NESTED NO | 잘못된 폴더 — "압축을 푼 `autoworker-script` 폴더 자체를 여세요" 안내 후 중단 |
| NON_ASCII 또는 ONEDRIVE | 아래 "폴더 이동" 진행 |
| 모두 정상 | STEP 2로 |

### 폴더 이동 (한글 경로·OneDrive일 때)

- 이유를 먼저 설명: 한글이 포함된 경로는 일부 도구가 오작동하고, OneDrive 폴더는 동기화가 파일을 잠가 오류가 난다
- 이동 목표: macOS `~/autoworker-script` / Windows `C:\autoworker-script` (권한 오류 시 `C:\Users\Public\autoworker-script`)
- **목표 경로를 알리고 사용자 동의를 받은 뒤** 실행:
  - macOS: `{PY} -c "import shutil; shutil.move(r'현재경로', r'목표경로')"`
  - Windows: 실행 중인 폴더는 이동이 잠길 수 있으므로 **복사** 방식 — `{PY} -c "import shutil; shutil.copytree(r'현재경로', r'목표경로')"`
- 실행 후 안내하고 **세팅 중단**:
  > VS Code에서 새 위치(`목표경로`) 폴더를 다시 열고 "세팅해줘"를 한 번 더 해주세요.
  (Windows는 추가: "이전 폴더는 새 위치에서 세팅이 끝난 것을 확인한 뒤 직접 삭제하세요.")

## STEP 2. 가상환경(.venv)

- `.venv` 없음 → `{PY} -m venv .venv`
- 있음 → `{VENV_PYTHON} --version` 실행 확인. 실패하면(폴더를 옮긴 경우, **다른 OS·컴퓨터에서 만든 .venv가 복사된 경우** 등) 지우고 재생성:
  `{PY} -c "import shutil; shutil.rmtree('.venv')"` → `{PY} -m venv .venv`

## STEP 3. yt-dlp 설치

```
{VENV_PIP} install -U -r requirements.txt
```

확인: `{VENV_PYTHON} -m yt_dlp --version`

## STEP 4. 동작 테스트 1건 (메타 조회 — 다운로드 없음)

collect.py가 쓰는 것과 같은 경로로 영상 정보만 조회한다:

```
{VENV_PYTHON} -m yt_dlp --skip-download --no-warnings --print "%(title)s | %(duration_string)s" "https://www.youtube.com/watch?v=jNQXAC9IVRw"
```

- 제목이 출력되면 성공
- 실패 → 인터넷 연결 또는 회사·학교망 차단 가능성. ❌로 기록하고 STEP 5로 계속

## STEP 5. ✅ 체크리스트 출력 (고정 양식)

```
✅ 세팅 완료 — autoworker-script v{VERSION}
──────────────────────────────
✅ OS          : macOS
✅ 폴더 위치    : /Users/xxx/autoworker-script
✅ Python      : 3.12.4 (.venv)
✅ yt-dlp      : 2026.8.6
✅ 동작 테스트  : 영상 정보 조회 성공
──────────────────────────────
다음 단계: "채널 만들어줘" → "대본 만들어줘"
```

- 버전은 루트 `VERSION` 파일에서 읽는다
- ❌가 하나라도 있으면 마지막 줄을 다음으로 교체:
  > ❌ 항목이 있습니다. **이 화면을 캡처해서 조교에게 보내주세요.** 가장 빠른 해결 방법입니다.
