import cv2
import os
import datetime
from detector import detect
from config import VIDEO_SOURCE, LOW_THRESHOLD, MEDIUM_THRESHOLD

os.makedirs("logs", exist_ok=True)
os.makedirs("captures", exist_ok=True)

cap = cv2.VideoCapture(VIDEO_SOURCE)

print("AI Crowd Density Monitoring Started... Press Q to Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    person_count, boxes = detect(frame)

    if person_count < LOW_THRESHOLD:
        density = "LOW"
        color = (0,255,0)
    elif LOW_THRESHOLD <= person_count < MEDIUM_THRESHOLD:
        density = "MEDIUM"
        color = (0,255,255)
    else:
        density = "HIGH"
        color = (0,0,255)

    for (x1, y1, x2, y2) in boxes:
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    cv2.putText(frame, f"People Count: {person_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.putText(frame, f"Density Level: {density}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    if density == "HIGH":
        with open("logs/crowd_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - HIGH density detected ({person_count})\n")

        filename = f"captures/high_density_{int(datetime.datetime.now().timestamp())}.jpg"
        cv2.imwrite(filename, frame)

    cv2.imshow("AI Crowd Density Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
