import cv2

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