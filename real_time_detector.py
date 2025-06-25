import cv2
from cnn_model import load_model
from utils import preprocess_frame, draw_predictions

# Load pre-trained model
model = load_model()

# Open webcam
cap = cv2.VideoCapture(0)

print("Starting real-time detection. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    input_data = preprocess_frame(frame)
    prediction = model.predict(input_data)
    output_frame = draw_predictions(frame, prediction)

    cv2.imshow("Real-Time Detection", output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
