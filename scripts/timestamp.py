"""
완성 영상에서 시간별 전사(타임코드 대본)를 추출하는 스크립트

사용법:
    python scripts/timestamp.py --video "/path/to/영상.mp4"

출력 (stdout):
    [MM:SS] 문장
    ...

- 타임스탬프 스킬(.claude/skills/timestamp/SKILL.md)이 사용한다 — 출력을 대본의
  챕터 구조와 대조해 유튜브 설명글의 챕터 타임스탬프를 만든다.
- faster-whisper 필요 (requirements.txt 기본 설치에는 없음 — 첫 사용 시 스킬이 설치):
    macOS:   .venv/bin/pip install faster-whisper
    Windows: .venv\\Scripts\\pip install faster-whisper
- 첫 실행 시 음성 인식 모델(~150MB)을 자동 다운로드한다 (인터넷 필요).
"""

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from console import enable_utf8_output

enable_utf8_output()


def main():
    parser = argparse.ArgumentParser(description="완성 영상 → 시간별 전사 추출")
    parser.add_argument("--video", required=True, help="완성 영상(또는 오디오) 파일 경로")
    parser.add_argument("--model", default="base", help="faster-whisper 모델 (기본 base)")
    parser.add_argument("--language", default="ko", help="음성 언어 (기본 ko)")
    args = parser.parse_args()

    if not os.path.exists(args.video):
        print(f"파일을 찾을 수 없습니다: {args.video}")
        sys.exit(1)

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("faster-whisper가 설치되어 있지 않습니다. 아래 명령으로 설치하세요:")
        print("  macOS:   .venv/bin/pip install faster-whisper")
        print("  Windows: .venv\\Scripts\\pip install faster-whisper")
        sys.exit(3)

    print("음성 인식 모델 로딩 중... (첫 실행은 모델 다운로드로 1~2분 추가)", file=sys.stderr)
    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, info = model.transcribe(args.video, language=args.language, vad_filter=True)

    duration = int(info.duration or 0)
    print(f"영상 길이 {duration // 60}분 {duration % 60}초 — 전사 시작", file=sys.stderr)

    for seg in segments:
        m, s = divmod(int(seg.start), 60)
        print(f"[{m:02d}:{s:02d}] {seg.text.strip()}")


if __name__ == "__main__":
    main()
