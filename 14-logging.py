"""
COMPLETE PYTHON LOGGING TUTORIAL
From Beginner to Advanced
================================
All log files are stored inside the "logs" folder
located next to this script (project root).
"""

import logging
import logging.handlers
import sys
import json
from datetime import datetime
from pathlib import Path


# ============================================================
# IMPORTANT: Always create the logs folder next to the script
# ============================================================
# This guarantees the folder is created in your project,
# regardless of where you run the script from.
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


# ============================================================
# STEP 1 – Absolute Beginner: Why we need logging
# ============================================================
print("\n=== STEP 1: Why logging instead of print? ===")
print("print() is fine for quick tests, but it has no levels,")
print("no timestamps, no file output, and is hard to control in production.")


# ============================================================
# STEP 2 – Basic usage of the logging module
# ============================================================
print("\n=== STEP 2: Most basic logging ===")

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a DEBUG message – detailed diagnostic info")
logging.info("This is an INFO message – confirmation that things work")
logging.warning("This is a WARNING – something unexpected but not fatal")
logging.error("This is an ERROR – a serious problem")
logging.critical("This is a CRITICAL – the program may not continue")


# ============================================================
# STEP 3 – Understanding log levels
# ============================================================
print("\n=== STEP 3: Log levels (from lowest to highest severity) ===")
print("""
DEBUG     (10)  – Detailed information, typically of interest only when diagnosing problems
INFO      (20)  – Confirmation that things are working as expected
WARNING   (30)  – An indication that something unexpected happened
ERROR     (40)  – Due to a more serious problem, the software has not been able to perform some function
CRITICAL  (50)  – A serious error, indicating that the program itself may be unable to continue
""")


# ============================================================
# STEP 4 – Controlling the minimum level
# ============================================================
print("\n=== STEP 4: Setting a higher minimum level ===")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.WARNING)

logging.debug("You will NOT see this")
logging.info("You will NOT see this either")
logging.warning("You WILL see this warning")
logging.error("You WILL see this error")


# ============================================================
# STEP 5 – Adding useful format and writing to a file
# ============================================================
print("\n=== STEP 5: Formatted logs + writing to a file ===")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=LOG_DIR / "app.log",
    filemode="w"
)

logging.info("This message goes only to the file 'logs/app.log'")
logging.warning("File logging is useful for production servers")


# ============================================================
# STEP 6 – Logging to BOTH console and file at the same time
# ============================================================
print("\n=== STEP 6: Console + File at the same time ===")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter("%(levelname)-8s | %(message)s")
console_handler.setFormatter(console_format)

# File handler
file_handler = logging.FileHandler(LOG_DIR / "app_detailed.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s"
)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Detailed debug info → only in file")
logger.info("Normal information → console + file")
logger.error("Something went wrong → console + file")


# ============================================================
# STEP 7 – Using different loggers (hierarchy)
# ============================================================
print("\n=== STEP 7: Named loggers and hierarchy ===")

parent_logger = logging.getLogger("my_app")
parent_logger.setLevel(logging.DEBUG)

db_logger = logging.getLogger("my_app.database")
api_logger = logging.getLogger("my_app.api")

db_logger.info("Connected to database")
api_logger.warning("API rate limit almost reached")


# ============================================================
# STEP 8 – Logging exceptions with full traceback
# ============================================================
print("\n=== STEP 8: Logging exceptions properly ===")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("Division by zero occurred!")

divide(10, 0)


# ============================================================
# STEP 9 – Rotating file handlers
# ============================================================
print("\n=== STEP 9: Rotating log files ===")

rotating_logger = logging.getLogger("rotating")
rotating_logger.setLevel(logging.DEBUG)

rotating_handler = logging.handlers.RotatingFileHandler(
    LOG_DIR / "rotating.log",
    maxBytes=1024,
    backupCount=3
)
rotating_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
rotating_logger.addHandler(rotating_handler)

for i in range(50):
    rotating_logger.info(f"Log entry number {i}")

print("Check the files inside logs/: rotating.log, rotating.log.1, ...")


# ============================================================
# STEP 10 – Timed rotating handler
# ============================================================
print("\n=== STEP 10: Timed rotating logs ===")

timed_logger = logging.getLogger("timed")
timed_logger.setLevel(logging.INFO)

timed_handler = logging.handlers.TimedRotatingFileHandler(
    LOG_DIR / "daily.log",
    when="midnight",
    interval=1,
    backupCount=7
)
timed_handler.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))
timed_logger.addHandler(timed_handler)

timed_logger.info("This log will rotate every day at midnight")


# ============================================================
# STEP 11 – Custom filter
# ============================================================
print("\n=== STEP 11: Custom filters ===")

class ErrorOnlyFilter(logging.Filter):
    def filter(self, record):
        return "error" in record.getMessage().lower()

filter_logger = logging.getLogger("filtered")
filter_logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.addFilter(ErrorOnlyFilter())
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
filter_logger.addHandler(handler)

filter_logger.info("This is a normal message")
filter_logger.error("This contains the word ERROR")


# ============================================================
# STEP 12 – Structured / JSON logging
# ============================================================
print("\n=== STEP 12: Structured JSON logging ===")

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record)

json_logger = logging.getLogger("json")
json_logger.setLevel(logging.DEBUG)

json_handler = logging.StreamHandler()
json_handler.setFormatter(JsonFormatter())
json_logger.addHandler(json_handler)

json_logger.info("User logged in", extra={"user_id": 42})
json_logger.error("Payment failed")


# ============================================================
# STEP 13 – Production-ready configuration function
# ============================================================
print("\n=== STEP 13: Production-ready configuration function ===")

def setup_logging(log_dir: Path = None, level: str = "INFO"):
    """
    Recommended way to configure logging for real applications.
    By default uses the LOG_DIR next to the script.
    """
    if log_dir is None:
        log_dir = LOG_DIR
    else:
        log_dir = Path(log_dir)
        log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level.upper()))
    logger.handlers.clear()

    # Console
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S"
    ))
    logger.addHandler(console)

    # Rotating file
    file_handler = logging.handlers.RotatingFileHandler(
        log_dir / "app.log",
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
    ))
    logger.addHandler(file_handler)

    return logger


app_logger = setup_logging(level="DEBUG")
app_logger.info("Application started with production logging setup")
app_logger.debug("This debug message goes only to the file")


# ============================================================
# STEP 14 – Logging inside classes / modules
# ============================================================
print("\n=== STEP 14: Logging inside a class ===")

class UserService:
    def __init__(self):
        self.logger = logging.getLogger(__name__ + ".UserService")

    def create_user(self, username: str):
        self.logger.info(f"Creating user: {username}")
        try:
            if not username:
                raise ValueError("Username cannot be empty")
            self.logger.debug("User validation passed")
            self.logger.info(f"User {username} created successfully")
        except Exception:
            self.logger.exception("Failed to create user")

service = UserService()
service.create_user("alice")
service.create_user("")


print("\n=== Tutorial finished ===")
print(f"All log files are stored in: {LOG_DIR.resolve()}")
print("  - logs/app.log")
print("  - logs/app_detailed.log")
print("  - logs/rotating.log (+ backups)")
print("  - logs/daily.log")