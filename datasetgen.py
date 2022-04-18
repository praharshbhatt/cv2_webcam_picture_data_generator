import cv2
import os
from time import time


dataset_path = "Data/"
if not os.path.exists(dataset_path):
    os.mkdir(dataset_path)
cap = cv2.VideoCapture(0)
frame_count = 0
image_count = 0

while True:
    frame_count += 1
    _, frame = cap.read()

    if frame_count % 10 == 0:
        image_count += 1
        cv2.imwrite(f"{dataset_path + str(time())}.jpg", frame)

    image = cv2.putText(
        frame,
        str(image_count),
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2,
        cv2.LINE_AA
    )

    cv2.imshow("Frames", frame)
    key_press = cv2.waitKey(1)
    if key_press == ord('q'):
        print("Breaking...")
        break
cap.release()
cv2.destroyAllWindows()
