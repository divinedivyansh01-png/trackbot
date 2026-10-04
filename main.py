import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("Could not open webcam")
for _ in range(30):
    cap.read()
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    cv2.imshow("TrackBot", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()