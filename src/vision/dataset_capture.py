import cv2
import os
import time

SAVE_DIR = "data/raw"
CAPTURE_INTERVAL = 2 # seconds between captures

def capture_images():
    os.makedirs(SAVE_DIR, exist_ok=True)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    print("Camera opened successfully")
    print("press 'q' to quit")

    last_capture_time = time.time()
    capture_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame")
            break

        current_time = time.time()

        # save image if enough time has passed
        if current_time - last_capture_time >= CAPTURE_INTERVAL:

            filename = f"{SAVE_DIR}/image_{capture_count:04d}.jpg"
            cv2.imwrite(filename, frame)

            print(f"Saved image: {filename}")
            capture_count += 1
            last_capture_time = current_time

        #show video feed
        cv2.imshow("Capture Feed", frame)

        #wait for 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #release camera and close windows
    cap.release()
    cv2.destroyAllWindows()

    print(f"Total images captured: {capture_count}")
    print("Exiting...")

if __name__ == "__main__":
    capture_images()