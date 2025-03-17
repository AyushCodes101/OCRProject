from processing.image_preprocessor import ImagePreprocessor
from model.ocr_model import OCRModel
from utils.logger import logger
from config.settings import settings
import keras

class OCRSystem:
    def __init__(self):
        self.logger = logger
        self.preprocessor = ImagePreprocessor()
        self.model = OCRModel().model
        self._load_weights()

    def _load_weights(self):
        try:
            self.model.load_weights(settings.MODEL_SAVE_PATH)
            self.logger.info("Successfully loaded model weights")
        except Exception as e:
            self.logger.error(f"Failed to load model weights: {str(e)}")
            raise

    def process_image(self, image_path):
        """Main processing pipeline"""
        try:
            self.logger.info(f"Processing image: {image_path}")
            processed_img = self.preprocessor.preprocess(image_path)
            prediction = self.model.predict(processed_img)
            # Add post-processing logic here
            return prediction
        except Exception as e:
            self.logger.error(f"Processing failed: {str(e)}")
            raise

if __name__ == "__main__":
    ocr = OCRSystem()
    result = ocr.process_image("1.jpg")
    print("OCR Result:", result)