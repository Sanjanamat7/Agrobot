import cv2
from ultralytics import YOLO

# 🔹 Load your trained model (update filename if needed)
model = YOLO("best.pt")   # or "yolov8n.pt" if that's your trained file

# Check which classes your model knows
print("Classes:", model.names)

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot access webcam")
    exit()

print("✅ Webcam opened. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Run inference (lower confidence if nothing shows up)
    results = model(frame, conf=0.25)

    # Plot results on the frame
    annotated_frame = results[0].plot()

    # Show the frame
    cv2.imshow("Leaf Disease Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
