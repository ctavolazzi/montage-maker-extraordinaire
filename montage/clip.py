"""Turn one source clip into one normalized vertical slice.

Cover-and-crop idea from harry0703/MoneyPrinterTurbo app/services/video.py (MIT): scale so the
frame is fully covered, then center crop. Random start and length idea from
hackersanddesigners/hdsa2019doc. Re-encode every slice to one format before concat, as in
mikhin's many-reels.js gist.
"""

from pathlib import Path

from .config import Config


def make_slice(src: Path, out: Path, cfg: Config) -> Path:
    """Cut a random 2 to 4 s piece of src, make it 1080x1920 at 30 fps, no audio."""
    # info = ffmpeg.probe(src)
    # length = random.uniform(cfg.slice_min_s, min(cfg.slice_max_s, info.duration_s))
    # start = random.uniform(0, info.duration_s - length)
    #
    # filters = []
    # if info.is_hdr:
    #     if ffmpeg.has_filter("zscale"):
    #         filters += [tonemap chain: zscale=t=linear, tonemap=hable, zscale=t=bt709, format=yuv420p]
    #     else:
    #         warn("HDR clip, colors may look washed out: " + src.name)
    # filters += [
    #     f"scale={cfg.width}:{cfg.height}:force_original_aspect_ratio=increase",
    #     f"crop={cfg.width}:{cfg.height}",
    #     f"fps={cfg.fps}",
    #     "format=yuv420p",
    #     "setsar=1",
    # ]
    #
    # ffmpeg.run(["-ss", start, "-t", length, "-i", src,
    #             "-vf", ",".join(filters),
    #             "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out])
    # return out
    raise NotImplementedError
