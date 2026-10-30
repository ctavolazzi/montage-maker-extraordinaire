"""Defaults and paths. One place to change any number."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    clips_dir: Path = Path("clips")
    music_dir: Path = Path("music")
    captions_file: Path = Path("captions.txt")
    ready_dir: Path = Path("ready")
    state_file: Path = Path(".montage/state.json")
    work_dir: Path = Path(".montage/tmp")

    clips_per_video: int = 4
    slice_min_s: float = 2.0
    slice_max_s: float = 4.0

    width: int = 1080
    height: int = 1920
    fps: int = 30

    font_path: Path | None = None      # None means: find a bold system font
    font_size: int = 72
    caption_y_ratio: float = 0.12      # caption top edge, as a share of video height

    use_music: bool = True
    video_exts: tuple = (".mp4", ".mov", ".m4v")
    music_exts: tuple = (".mp3", ".m4a", ".wav")


def load(args) -> Config:
    """Build a Config from defaults, then montage.toml if present, then CLI args."""
    # cfg = Config()
    # if Path("montage.toml") exists: read it, set matching fields
    # for each CLI arg that was given: set the matching field
    # if cfg.font_path is None: cfg.font_path = find_font()
    # return cfg
    raise NotImplementedError


def find_font() -> Path:
    """Return the first bold sans font that exists on this machine."""
    # candidates = [
    #   macOS:   /System/Library/Fonts/Supplemental/Impact.ttf, Arial Bold.ttf
    #   Linux:   /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
    #   Windows: C:/Windows/Fonts/impact.ttf, arialbd.ttf
    # ]
    # return the first that exists, else raise with a message: pass --font PATH
    raise NotImplementedError
