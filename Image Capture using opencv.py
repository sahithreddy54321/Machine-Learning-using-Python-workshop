import cv2 #pip install opencv-contrib-python
webcam = cv2.VideoCapture(0) # 0 stands for no.of cameras . If u have 2 camers write 1 instead of 0
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints True as long as the webcam is running
        print(frame) #prints matrix value of each framed
        cv2.imshow("Capturing",frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename = 'saved_img.jpg',img = frame )
            webcam.release()
            img = cv2.imread('saved_img.jpg')
            cv2.imshow("Captured Image", img)
            cv2.waitKey(0)
            print("Image Saved!")
            break
        elif key == ord('q'):
            print("Turning off Camera")
            webcam.release()
            print("Camera off.")
            print("Program ended")
            cv2.destroyAllwindows()
            break

    except(KeyboardInterrupt):
        print("Turning off camera")
        webcam.release()
        print("camera off")
        print("Program ended")
        cv2.destroyAllWindows()
        break