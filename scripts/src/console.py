"""표준 출력 인코딩 보정 — Windows cp949 환경에서 죽지 않게 한다.

Windows에서 출력이 파이프나 파일로 연결되면 파이썬은 로케일 인코딩(cp949)으로
인코딩하는데, 진행 표시에 쓰는 ✓ · → · ─ 같은 문자가 cp949에 없어서
UnicodeEncodeError로 스크립트 전체가 죽는다 (작업은 이미 끝났는데 마지막
완료 메시지에서 죽는 식). 출력 스트림을 UTF-8로 바꾸고, 그래도 표현할 수
없는 문자는 예외 대신 대체 문자로 흘려보낸다.

각 실행 스크립트가 import 직후 enable_utf8_output()을 한 번 호출한다.
"""

import sys


def enable_utf8_output():
    """stdout/stderr를 UTF-8 + errors="replace"로 재설정한다."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:  # 리다이렉트된 스트림 등 — 건드리지 않는다
            continue
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            pass
