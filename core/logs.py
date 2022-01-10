import logging
import logging.handlers
import os
import sys

from core import venom


class Logger(object):

    def __init__(self):
        self.fmt = "%(asctime)s - %(levelname)s - %(message)s"
        self.level = logging.INFO
        self.date_fmt = "%Y-%m-%d %H:%M:%S"
        self.log_filename = "venom.log"
        self.max_bytes = venom.cfg["core.logs.max_bytes"]
        self.backup_count = venom.cfg["core.logs.backup_count"]
        self.logs_folder_path = venom.cfg["core.logs.folder_path"]

        # create logs directory
        if not os.path.exists(self.logs_folder_path):
            os.makedirs(self.logs_folder_path)

        # logging handlers
        self.stream_handler = logging.StreamHandler(sys.stdout)
        self.rotating_file_handler = logging.handlers.RotatingFileHandler(
            filename=os.path.join(self.logs_folder_path, self.log_filename),
            backupCount=self.backup_count,
            maxBytes=self.max_bytes
        )
        self.handlers = [self.stream_handler, self.rotating_file_handler]

    def configure(self):
        config = dict(level=self.level, format=self.fmt, datefmt=self.date_fmt, handlers=self.handlers)
        logging.basicConfig(**config)
        return self
