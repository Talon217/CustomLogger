import logging
from logging.handlers import RotatingFileHandler
from typing import ClassVar


class ColorFormatter(logging.Formatter):



    COLORS: ClassVar[dict[int, str]] = {
        logging.DEBUG: "\x1b[36;2m",       # Dim Cyan
        logging.INFO: "\x1b[32;2m",        # Dim Green
        logging.WARNING: "\x1b[33;2m",     # Dim Yellow
        logging.ERROR: "\x1b[31;2m",       # Dim Red
        logging.CRITICAL: "\x1b[91;1;2m",  # Dim, Bold Red 
    }
    RESET: ClassVar[str] = "\x1b[0m"

    def format(self, record):
        color = self.COLORS.get(record.levelno, self.RESET)
        original_levelname = record.levelname
        record.levelname = f"{color}{original_levelname:<8}{self.RESET}"
        formatted_str = super().format(record)
        record.levelname = original_levelname
        return formatted_str

def setup_logger(console_level=logging.WARNING, file_level=logging.DEBUG) -> logging.Logger:
    base_format = "%(asctime)s [ %(levelname)-8s ] [ %(name)s ~ %(filename)s:%(lineno)d ] - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Clear pre-existing handlers to prevent duplicate outputs
    if logger.hasHandlers():
        logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(ColorFormatter(fmt=base_format, datefmt=date_format))
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        filename="VLAI.log",
        mode="a",            # append
        maxBytes=5_000_000,  # 5 MB
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(file_level)
    file_handler.setFormatter(logging.Formatter(fmt=base_format, datefmt=date_format)
)
    logger.addHandler(file_handler)

    return logger

def main():
    logger = setup_logger(console_level=logging.DEBUG)

    logger.debug("lorem ispum dolor sit amet")
    logger.info("lorem ispum dolor sit amet")
    logger.warning("lorem ispum dolor sit amet")
    logger.error("lorem ispum dolor sit amet")
    logger.critical("lorem ispum dolor sit amet")

if __name__ == "__main__":
    main()