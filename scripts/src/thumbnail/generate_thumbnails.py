#!/usr/bin/env python3
"""Generate thumbnail images from thumbnail-prompts.json using Google Gemini (NanoBanana) API."""

import argparse
import asyncio
import json
import os
import sys
from io import BytesIO
from pathlib import Path

# Add parent paths for project_resolver
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.console import enable_utf8_output
from src.project_resolver import resolve_project_dir

enable_utf8_output()

# --- Root directory (autoworker-script/) ---
ROOT = Path(__file__).resolve().parents[3]

# 이미지 생성 라이브러리는 옵션 의존성 — 스위치가 켜진 뒤에만 로드한다.
# (기본 requirements.txt에는 없음. 스위치 OFF 환경에서 import 실패로 죽지 않게 lazy import)
genai = None
types = None
Image = None


def ensure_image_libs():
    """google-genai + Pillow lazy import (옵션 의존성)."""
    global genai, types, Image
    if genai is not None:
        return
    try:
        from google import genai as _genai
        from google.genai import types as _types
        from PIL import Image as _Image
    except ImportError:
        print("ERROR: 썸네일 이미지 생성에는 추가 패키지가 필요합니다.")
        print("설치: pip install google-genai Pillow (README의 썸네일 옵션 안내 참고)")
        sys.exit(1)
    genai, types, Image = _genai, _types, _Image


# --- Channel settings (on/off switch) ---

def load_channel_settings(prompts_file: Path) -> dict:
    """thumbnail-prompts.json 경로에서 상위로 올라가며 channels/{채널}/config/settings.json을 찾는다."""
    for parent in prompts_file.parents:
        candidate = parent / "config" / "settings.json"
        if candidate.exists():
            try:
                return json.loads(candidate.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                return {}
    return {}


def thumbnail_generation_enabled(settings: dict) -> bool:
    """settings.thumbnail.generate_images 값 (기본 False = off)."""
    thumb_cfg = settings.get("thumbnail", {}) if isinstance(settings, dict) else {}
    return bool(thumb_cfg.get("generate_images", False))


# --- Thumbnail strategy loading ---

def load_thumbnail_strategy(channel: str | None) -> dict | None:
    """Load channel's thumbnail-strategy.json if it exists."""
    if not channel:
        return None
    strategy_path = ROOT / "channels" / channel / "config" / "thumbnail-strategy.json"
    if strategy_path.exists():
        with open(strategy_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def get_prompt_suffixes(strategy: dict | None) -> list[str]:
    """Build boilerplate suffixes based on channel's thumbnail strategy."""
    suffixes = [
        "wide 16:9 aspect ratio, YouTube thumbnail composition",
    ]

    # Text space / composition rule
    text_space = (strategy or {}).get("text_space", "bottom-half")

    if text_space == "bottom-half":
        suffixes.append(
            "all key visual elements and the main subject fill the upper half "
            "of the frame edge to edge, the bottom half of the frame is reserved "
            "for text overlay and should contain only simple background with no "
            "important elements"
        )
    elif text_space == "left-right":
        suffixes.append(
            "main subject positioned on one side of the frame, the opposite side "
            "contains simple background suitable for text overlay"
        )
    # text_space == "full" → no composition suffix (full-frame image)

    suffixes.append("no text, no letters, no words, no numbers, no watermark")

    return suffixes


def apply_boilerplate(prompt: str, suffixes: list[str]) -> str:
    """Append boilerplate suffixes if not already present (case-insensitive)."""
    lower = prompt.lower()
    parts = [prompt.rstrip(". ")]
    for suffix in suffixes:
        if suffix.lower() not in lower:
            parts.append(suffix)
    return ". ".join(parts)


# --- API key ---

def load_api_key() -> str:
    """Load API key from environment or .env (GEMINI_API_KEY 우선, GOOGLE_API_KEY 폴백)."""
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if key:
        return key

    env_path = ROOT / ".env"
    if env_path.exists():
        env_keys = {}
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                env_keys[k.strip()] = v.strip().strip('"').strip("'")
        key = env_keys.get("GEMINI_API_KEY") or env_keys.get("GOOGLE_API_KEY")
        if key:
            return key

    print("ERROR: GEMINI_API_KEY not found in environment or .env")
    sys.exit(1)


# --- Image handling ---

MAX_FILE_SIZE = 1.5 * 1024 * 1024  # 1.5MB


def compress_image(img, output_path: Path) -> None:
    """Save image as JPEG, adjusting quality to stay under MAX_FILE_SIZE."""
    # Ensure RGB (JPEG doesn't support alpha)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # Start from high quality, step down until under limit
    for quality in range(95, 49, -5):
        buf = BytesIO()
        img.save(buf, "JPEG", quality=quality, optimize=True)
        size = buf.tell()
        if size <= MAX_FILE_SIZE:
            output_path = output_path.with_suffix(".jpg")
            with open(output_path, "wb") as f:
                f.write(buf.getvalue())
            print(f"    압축: quality={quality}, {size / 1024:.0f}KB")
            return

    # Fallback: save at quality 50
    output_path = output_path.with_suffix(".jpg")
    img.save(output_path, "JPEG", quality=50, optimize=True)
    print(f"    압축: quality=50 (최소)")


def save_image_from_response(response, output_path: Path) -> bool:
    """Extract and save image from Gemini response."""
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            image_data = BytesIO(part.inline_data.data)
            img = Image.open(image_data)
            compress_image(img, output_path)
            return True
    return False


# --- Generation ---

async def generate_thumbnail(
    client,
    model: str,
    prompt: str,
    output_path: Path,
    thumbnail_id: int,
    total: int,
    max_retries: int = 3,
) -> bool:
    """Generate a single thumbnail image with retries."""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"[{thumbnail_id}/{total}] 생성 중... (시도 {attempt}/{max_retries})")

            # 모델에 따라 config 분기
            config_kwargs = {"response_modalities": ["TEXT", "IMAGE"]}
            # gemini-2.0-flash-exp는 aspect_ratio/image_size 미지원
            if "2.0-flash-exp" not in model:
                config_kwargs["image_config"] = types.ImageConfig(
                    aspect_ratio="16:9",
                    image_size="2K",
                )

            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(**config_kwargs),
            )

            if save_image_from_response(response, output_path):
                print(f"  ✓ 썸네일 {thumbnail_id} 저장 완료: {output_path.name}")
                return True
            else:
                print(f"  ✗ 썸네일 {thumbnail_id}: 응답에 이미지 없음")

        except Exception as e:
            error_msg = str(e)
            print(f"  ✗ 썸네일 {thumbnail_id} 실패 (시도 {attempt}): {error_msg}")

            if attempt < max_retries:
                wait = 10 * attempt
                print(f"    {wait}초 대기 후 재시도...")
                await asyncio.sleep(wait)

    return False


async def generate_thumbnails(
    prompts_path: str,
    channel: str | None = None,
    model: str = "gemini-3.1-flash-image-preview",
    ids: list[int] | None = None,
    force: bool = False,
    subdir: str | None = None,
):
    """Generate thumbnail images from thumbnail-prompts.json."""

    prompts_file = Path(prompts_path)
    if not prompts_file.exists():
        print(f"ERROR: thumbnail-prompts.json not found: {prompts_file}")
        sys.exit(1)

    # On/off 스위치: settings.thumbnail.generate_images (기본 off). --force로 무시 가능.
    if not force and not thumbnail_generation_enabled(load_channel_settings(prompts_file)):
        print("썸네일 이미지 생성이 비활성화되어 있습니다 "
              "(settings.json의 thumbnail.generate_images=false). 건너뜁니다.")
        print("강제로 생성하려면 --force 옵션을 사용하세요.")
        return

    ensure_image_libs()

    with open(prompts_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    thumbnails = data.get("thumbnails", [])
    if not thumbnails:
        print(f"ERROR: No thumbnails found in {prompts_file.name}")
        sys.exit(1)

    # Filter by IDs if specified
    if ids:
        thumbnails = [t for t in thumbnails if t["id"] in ids]
        if not thumbnails:
            print(f"ERROR: No thumbnails matching IDs: {ids}")
            sys.exit(1)

    # 프롬프트는 _script/(내부), 이미지는 output/썸네일/(완성본 폴더)
    if prompts_file.parent.name == "_script":
        output_dir = prompts_file.parent.parent / "output" / "썸네일"
    else:
        output_dir = prompts_file.parent
    if subdir:
        output_dir = output_dir / subdir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load channel strategy for conditional boilerplate
    strategy = load_thumbnail_strategy(channel)
    suffixes = get_prompt_suffixes(strategy)

    api_key = load_api_key()
    client = genai.Client(api_key=api_key)

    print(f"모델: {model}")
    print(f"썸네일 {len(thumbnails)}개 생성 예정")
    if strategy:
        print(f"채널 전략: text_space={strategy.get('text_space', 'bottom-half')}")
    print(f"출력 디렉토리: {output_dir}\n")

    results = {"success": [], "failed": []}

    for thumb in thumbnails:
        tid = thumb["id"]
        output_path = output_dir / f"thumbnail_{tid:02d}.jpg"

        # Check both .jpg and legacy .png
        png_path = output_path.with_suffix(".png")
        if not force and (output_path.exists() or png_path.exists()):
            existing = output_path.name if output_path.exists() else png_path.name
            print(f"[{tid}/{len(data['thumbnails'])}] 이미 존재 — 건너뜀: {existing}")
            results["success"].append(tid)
            continue

        success = await generate_thumbnail(
            client=client,
            model=model,
            prompt=apply_boilerplate(thumb["prompt_en"], suffixes),
            output_path=output_path,
            thumbnail_id=tid,
            total=len(data["thumbnails"]),
        )

        if success:
            results["success"].append(tid)
        else:
            results["failed"].append(tid)

        # Rate limit: wait between requests
        if thumb != thumbnails[-1]:
            await asyncio.sleep(3)

    # Summary
    print(f"\n{'='*40}")
    print(f"✓ 성공: {len(results['success'])}개 {results['success']}")
    if results["failed"]:
        print(f"✗ 실패: {len(results['failed'])}개 {results['failed']}")
    print(f"출력: {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Generate thumbnail images from thumbnail-prompts.json (Gemini API)")
    parser.add_argument("prompts", nargs="?", help="Path to thumbnail-prompts.json (or use --project)")
    parser.add_argument("--project", "-p", help="Project name")
    parser.add_argument("--channel", "-c", help="Channel name")
    parser.add_argument(
        "--model", "-m",
        default="gemini-3.1-flash-image-preview",
        help="Gemini model (default: gemini-3.1-flash-image-preview)",
    )
    parser.add_argument("--ids", nargs="+", type=int, help="Generate only specific thumbnail IDs (e.g. --ids 1 3)")
    parser.add_argument("--subdir", "-s", help="Output subdirectory name (e.g. flash, pro)")
    parser.add_argument("--force", "-f", action="store_true",
                        help="Overwrite existing images and ignore the thumbnail.generate_images=false switch")

    args = parser.parse_args()

    # Resolve prompts path
    if args.prompts:
        prompts_path = args.prompts
    elif args.project:
        project_dir = resolve_project_dir(args.project, args.channel)
        prompts_path = str(project_dir / "_script" / "thumbnail-prompts.json")
    else:
        parser.error("Provide thumbnail-prompts.json path or --project")

    asyncio.run(generate_thumbnails(
        prompts_path=prompts_path,
        channel=args.channel,
        model=args.model,
        ids=args.ids,
        force=args.force,
        subdir=args.subdir,
    ))


if __name__ == "__main__":
    main()
