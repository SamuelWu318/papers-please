from pathlib import Path

ROOT_DIR: Path = Path(__file__).resolve().parent.parent.parent

SRC_DIR: Path = ROOT_DIR / "src"
LOGS_DIR: Path = ROOT_DIR / "logs"
DEBUG: Path = LOGS_DIR / "debug.log"