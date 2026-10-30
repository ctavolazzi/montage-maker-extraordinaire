"""Draw a caption as a transparent PNG.

Adapted from `render_hook_png` in upload-post/upload-post-skills
skills/autoshorts/autoshorts.py (MIT License, Copyright the upload-post authors), read at
commit 935ea6f. Keep this credit when the body is filled in.

Why a PNG and not ffmpeg drawtext: drawtext needs an ffmpeg built with libfreetype, which
is often missing. Pillow is always there.
"""

from pathlib import Path


def render(text: str, out: Path, video_w: int, font_path: Path,
           font_size: int = 72, max_ratio: float = 0.85) -> Path:
    """White text, black stroke, rounded black pill behind each line, centered."""
    # font = ImageFont.truetype(font_path, font_size)
    # text_max_w = video_w * max_ratio - 2 * pad_x
    #
    # greedy word wrap:
    #   for each word: if current line + word is wider than text_max_w, start a new line
    #
    # canvas height = lines * pill_height + gaps + outer padding
    # img = transparent RGBA, width video_w
    #
    # for each line:
    #   x = centered
    #   draw rounded rectangle behind it, fill black at alpha 200
    #   draw text, fill white, stroke_width 3, stroke black
    #
    # img.save(out)
    # return out
    raise NotImplementedError
