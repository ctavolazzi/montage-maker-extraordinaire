"""Assemble slices into the final video, then grab the cover image."""

from pathlib import Path

from .config import Config


def concat(slices: list[Path], out: Path, work_dir: Path) -> Path:
    """Stitch slices end to end. They are already identical in format, so stream copy works."""
    # write work_dir/list.txt with one line per slice: file '<absolute path>'
    # ffmpeg.run(["-f", "concat", "-safe", "0", "-i", list.txt, "-c", "copy", out])
    # return out
    raise NotImplementedError


def finish(joined: Path, out: Path, cfg: Config,
           caption_png: Path | None, music: Path | None) -> Path:
    """Overlay the caption for the whole video and add music if given."""
    # inputs = ["-i", joined]
    # if caption_png: inputs += ["-i", caption_png]
    # if music:       inputs += ["-i", music]
    #
    # if caption_png:
    #     filter = f"[0:v][1:v]overlay=0:H*{cfg.caption_y_ratio}[v]"; map video from [v]
    # else:
    #     map video from 0:v
    #
    # if music: map its audio, "-shortest", "-c:a", "aac"
    #
    # ffmpeg.run(inputs + filters + maps +
    #            ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
    #             "-movflags", "+faststart", out])
    # return out
    raise NotImplementedError


def cover(video: Path, out: Path, at_s: float = 1.0) -> Path:
    """Save one frame (caption already burned in) as a JPG thumbnail."""
    # ffmpeg.run(["-ss", at_s, "-i", video, "-frames:v", "1", "-q:v", "2", out])
    # return out
    raise NotImplementedError


def make_one(cfg: Config, clips: list[Path], caption: str | None,
             music: Path | None, name: str) -> tuple[Path, Path]:
    """Full pipeline for one video. Returns (video path, cover path)."""
    # slices = [clip.make_slice(c, cfg.work_dir / f"{name}_{i}.mp4", cfg) for i, c in enumerate(clips)]
    # joined = concat(slices, cfg.work_dir / f"{name}_joined.mp4", cfg.work_dir)
    # png = caption.render(caption, cfg.work_dir / f"{name}.png", cfg.width, cfg.font_path) if caption else None
    # video = finish(joined, cfg.ready_dir / f"{name}.mp4", cfg, png, music)
    # thumb = cover(video, cfg.ready_dir / f"{name}.jpg")
    # delete work files for this name
    # return video, thumb
    raise NotImplementedError
