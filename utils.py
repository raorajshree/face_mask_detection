import cv2
import numpy as np

def preprocess_frame(frame):
    resized = cv2.resize(frame, (64, 64))
    normalized = resized / 255.0
    return np.expand_dims(normalized, axis=0)

def draw_predictions(frame, prediction):
    label = f"Detected: {np.argmax(prediction)}"
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame
