import cv2 as cv
import numpy as np
cap = cv.VideoCapture("video.mp4")


while cap.isOpened():
    sucess, frame = cap.read()
    if sucess:
        zeros = np.zeros((frame.shape[0], frame.shape[1]), np.uint8)
        b, g, r = cv.split(frame)
        blue = cv.merge([b, zeros, zeros])
        green = cv.merge([zeros, g, zeros])
        red = cv.merge([zeros, zeros, r])
        gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("Frame", frame)
        cv.imshow("Gray frame", gray_img)
        cv.imshow("Blue", blue)
        cv.imshow("Green", green)
        cv.imshow("Red", red)
        k = cv.waitKey(50)
        if k & 0xff == ord('q'):
            break
    else:
        break
print("blue mattrix {}".format(b))
print("")
cap.release()
cv.destroyAllWindows()

