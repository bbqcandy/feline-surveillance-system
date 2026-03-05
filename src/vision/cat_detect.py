import cv2
from ultralytics import YOLO

#load YOLO model
model = YOLO("yolo26n.pt")

def main():
    print("starting camera test")

    # try default camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    print("Camera opened successfully")
    print("press 'q' to quit")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame")
            break

        # run Yolo detection
        results = model(frame)

        for result in results:
            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                label = model.names[class_id]

                # only show cats
                if label == "cat":

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    #draw bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    #add label
                    text = f"{label} {confidence:.2f}"
                    cv2.putText(
                        frame,
                        text,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        2,
                    )

        #show video feed
        cv2.imshow("Camera Feed", frame)

        #wait for 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #release camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()