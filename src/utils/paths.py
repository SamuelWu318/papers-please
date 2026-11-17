from pathlib import Path

ROOT_DIR: Path = Path(__file__).resolve().parent.parent.parent

SRC_DIR: Path = ROOT_DIR / "src"
PUBLIC_DIR: Path = ROOT_DIR / "public"
LOGS_DIR: Path = PUBLIC_DIR / "logs"
DEBUG: Path = LOGS_DIR / "debug.log"