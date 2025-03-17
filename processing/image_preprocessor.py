import cv2
import numpy as np
from config.settings import settings

class ImagePreprocessor:
    def __init__(self):
        self.logger = settings.logger

    def preprocess(self, image_path):
        """Process image for OCR model input"""
        try:
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (settings.IMG_WIDTH, settings.IMG_HEIGHT))
            img = img.astype(np.float32) / 255.0
            img = np.expand_dims(img, axis=-1)
            return np.array([img])
        except Exception as e:
            self.logger.error(f"Image preprocessing failed: {str(e)}")
            raise