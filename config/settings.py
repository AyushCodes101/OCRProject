import os
from pathlib import Path

class Settings:
    BASE_DIR = Path(__file__).resolve().parent.parent
    LOG_DIR = BASE_DIR / "logs"
    MODEL_SAVE_PATH = BASE_DIR / "model/trained_models/cnn_model.h5"

    # Image processing constants
    IMG_WIDTH = 128
    IMG_HEIGHT = 32
    CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,;.!?'\"-:"

settings = Settings()