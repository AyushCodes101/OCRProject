import logging
import os
from datetime import datetime
from pathlib import Path
from config.settings import settings

class OCRLogger:
    def __init__(self):
        self._ensure_log_dir_exists()
        self._configure_logger()

    def _ensure_log_dir_exists(self):
        """Create log directory if it doesn't exist"""
        try:
            settings.LOG_DIR.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"FATAL: Could not create log directory: {str(e)}")
            raise

    def _configure_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(settings.LOG_DIR / f"ocr_{datetime.now().strftime('%Y%m%d')}.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger("OCRSystem")

logger = OCRLogger().logger