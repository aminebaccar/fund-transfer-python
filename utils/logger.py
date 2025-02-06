import logging
import sys
import os

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "../test_results.log")

# Configure logging
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# File handler
file_handler = logging.FileHandler(LOG_FILE_PATH, mode="w", encoding="utf-8")  # Overwrites each run
file_handler.setFormatter(log_formatter)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)

# Configure root logger
logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])

logger = logging.getLogger(__name__)

def log_test_result(test_name, status, message=""):
    """Logs test results with status and optional message."""
    log_message = f"{test_name} - {status.upper()} - {message}"

    if status.upper() == "PASS":
        logger.info(f"✅ {log_message}")
    elif status.upper() == "FAIL":
        logger.error(f"❌ {log_message}")
    else:
        logger.warning(f"⚠️ {log_message}")

    # Force log flush to file and console
    sys.stdout.flush()
    for handler in logger.handlers:
        handler.flush()
