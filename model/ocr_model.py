from keras import layers, Model
from config.settings import settings

class OCRModel:
    def __init__(self):
        self.logger = settings.logger
        self.model = self.build_crnn_model()

    def build_crnn_model(self):
        """Create CRNN model architecture"""
        input_img = layers.Input(shape=(settings.IMG_WIDTH, settings.IMG_HEIGHT, 1), name='image')
        
        # CNN
        x = layers.Conv2D(32, (3,3), activation='relu', padding='same')(input_img)
        x = layers.MaxPooling2D((2, 2))(x)
        x = layers.Conv2D(64, (3,3), activation='relu', padding='same')(x)
        x = layers.MaxPooling2D((2, 2))(x)
        
        # RNN
        x = layers.Reshape((-1, 64))(x)
        x = layers.Bidirectional(layers.LSTM(128, return_sequences=True))(x)
        x = layers.Bidirectional(layers.LSTM(64, return_sequences=True))(x)
        
        # Output
        x = layers.Dense(len(settings.CHARACTERS) + 1, activation='softmax')(x)
        
        return Model(inputs=input_img, outputs=x)