import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_file_path, exist_ok=True)

LOGFILEPATH = os.path.join(log_file_path, LOG_FILE)

logging.basicConfig(
    filename=LOGFILEPATH,
    format = "[%(asctime)s] %(lineno)d %(name)s %(levelname)s-%(message)s",
    level = logging.INFO,
)

if __name__ == "__main__":
    logging.info("logger.py successfully created")