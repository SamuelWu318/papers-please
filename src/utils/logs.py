import logging, sys
from logging.handlers import RotatingFileHandler
import utils.paths as proj

"""
guide to logging levels
DEBUG: temporary debugging logs
SKIP: skipping a file/step for any reason
STEP: basic step (start of a method, moving through a method)
INFO: a method that aggregates multiple step methods
WARNING: potential issues in returning/method call
SUCCESS: success in returning/method call
ERROR: error that should be addressed by the program
CRITICAL: error that should stop the program
"""

# ensure type hinting
DEBUG = logging.DEBUG
SKIP = 15
STEP = 18
INFO = logging.INFO
WARNING = logging.WARNING
SUCCESS = 35
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

_LEVELS = {
    10: "DEBUG",  15: "SKIP",     18: "STEP",
    20: "INFO",   30: "WARNING",  35: "SUCCESS",
    40: "ERROR",  50: "CRITICAL"
}

_COLORS = {
    10: "\x1b[37m",  15: "\x1b[33m",  18: "\x1b[34m",
    20: "\x1b[36m",  30: "\x1b[95m",  35: "\x1b[32m",
    40: "\x1b[91m",  50: "\x1b[91m"
}

class ColorFormatter(logging.Formatter):
    """Color Formatting wrapper class for _FORMAT"""
    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt, datefmt)

    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        if not sys.stderr.isatty(): return msg

        old = f"[{record.levelname}]"
        new = f"{_COLORS.get(record.levelno)}{old}\x1b[0m"
        return msg.replace(old, new, 1)

_LOGGER = "papersplease"

_FMT="%(asctime)s - [%(levelname)s] - (%(filename)s:%(lineno)d): %(message)s"
_DATEFMT="%Y-%m-%d %H:%M:%S"

_STDERR_FORMAT = ColorFormatter(_FMT, _DATEFMT)
_FILE_FORMAT = logging.Formatter(_FMT, _DATEFMT)

_LOG_LEVEL = 10

_STDERR_LEVEL = 20
_FILE_LEVEL = 10

def _logger() -> logging.Logger:
    logger = logging.getLogger(_LOGGER)
    if logger.handlers: return logger

    # build all additional level calls
    for num, name in _LEVELS.items():
        if logging.getLevelName(num) == (name): continue
        logging.addLevelName(num, name)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(_STDERR_LEVEL)
    stderr_handler.setFormatter(_STDERR_FORMAT)

    file_handler = RotatingFileHandler(proj.DEBUG, maxBytes=5_000_000, backupCount=10)
    file_handler.setLevel(_FILE_LEVEL)
    file_handler.setFormatter(_FILE_FORMAT)

    logger.addHandler(stderr_handler)
    logger.addHandler(file_handler)
    logger.setLevel(_LOG_LEVEL)
    logger.propagate = False

    return logger

_log = _logger()

def _msg(level: int, msg: str, *args):
    if not _log.isEnabledFor(level): return
    _log.log(level, msg, *args, stacklevel=3)

def debug(msg: str, *args: object) -> None: _msg(DEBUG, msg, *args)
def skip(msg: str, *args: object) -> None: _msg(SKIP, msg, *args)
def step(msg: str, *args: object) -> None: _msg(STEP, msg, *args)
def info(msg: str, *args: object) -> None: _msg(INFO, msg, *args)
def warning(msg: str, *args: object) -> None: _msg(WARNING, msg, *args)
def success(msg: str, *args: object) -> None: _msg(SUCCESS, msg, *args)
def error(msg: str, *args: object) -> None: _msg(ERROR, msg, *args)
def critical(msg: str, *args: object) -> None: _msg(CRITICAL, msg, *args)