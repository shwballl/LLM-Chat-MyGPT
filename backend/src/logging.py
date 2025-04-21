import logging
from enum import StrEnum
from colorlog import ColoredFormatter

LOG_FILE = "./logs/app.log"
ERROR_LOG_FILE = "./logs/error.log"

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
COLOR_FORMAT = "%(log_color)s%(asctime)s - %(levelname)s - %(message)s"

class LogLevels(StrEnum):
    info = "INFO"
    warning = "WARNING"
    error = "ERROR"
    debug = "DEBUG"

def configure_logging(log_level: str = LogLevels.error):
    """Configure the root logger with a given log level.

    Args:
        log_level (str, optional): The log level to set. Defaults to LogLevels.error.

    Notes:
        If the provided log_level is not in the list of valid log levels, it will default to LogLevels.error.

        This function will also set the log level for the following modules to WARNING:
        - httpx
        - uvicorn
        - uvicorn.error
        - uvicorn.access

        The root logger will be configured with two handlers: a StreamHandler with a ColoredFormatter and a FileHandler
        with a standard Formatter. The StreamHandler will log all messages to the console, while the FileHandler will
        log all messages to a file named "app.log".

        Additionally, an error handler will be added to log all ERROR and CRITICAL messages to a file named "error.log".
    """
    log_level = str(log_level).upper()
    log_levels = [level.value for level in LogLevels]

    if log_level not in log_levels:
        log_level = LogLevels.error

    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    logger = logging.getLogger()
    logger.setLevel(log_level)

    logger.handlers = []

    color_formatter = ColoredFormatter(
        COLOR_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(color_formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(file_handler)

    error_handler = logging.FileHandler(ERROR_LOG_FILE, encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(error_handler)
