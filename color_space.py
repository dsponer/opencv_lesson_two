import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def nothing():
    pass


cv2.namedWindow('original')
cv2.createTrackbar('h_min', 'original', 0, 180,  nothing)
cv2.createTrackbar('h_max', 'original', 0, 180, nothing)
cv2.createTrackbar('s_min', 'original', 0, 255, nothing)
cv2.createTrackbar('s_max', 'original', 0, 255, nothing)
cv2.createTrackbar('v_min', 'original', 0, 255, nothing)
cv2.createTrackbar('v_max', 'original', 0, 255, nothing)

cv2.setTrackbarPos('h_min', 'original', 0)
cv2.setTrackbarPos('h_max', 'original', 180)
cv2.setTrackbarPos('s_min', 'original', 54)
cv2.setTrackbarPos('s_max', 'original', 255)
cv2.setTrackbarPos('v_min', 'original', 5)
cv2.setTrackbarPos('v_max', 'original', 253)

while True:
    flag, image_origin = cap.read()
    image_hsv = cv2.cvtColor(image_origin, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('h_min', 'original')
    h_max = cv2.getTrackbarPos('h_max', 'original')
    s_min = cv2.getTrackbarPos('s_min', 'original')
    s_max = cv2.getTrackbarPos('s_max', 'original')
    v_min = cv2.getTrackbarPos('v_min', 'original')
    v_max = cv2.getTrackbarPos('v_max', 'original')
    image_blue = cv2.inRange(image_hsv, (h_min, s_min, v_min), (h_max, s_max, v_max))
    # edges = cv2.Canny(image_blue, 10, 250)
    contours, hierarchy = cv2.findContours(image_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        cnt = max(contours, key=cv2.contourArea)
        # rect = cv2.minAreaRect(cnt)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # cv2.drawContours(image_origin, [box], 0, (255, 255, 0), 2)

        if len(cnt) > 4:
            ellipse = cv2.fitEllipse(cnt)
            cv2.ellipse(image_origin, ellipse, (0, 0, 255), 2)

    cv2.imshow('original', image_origin)
    # cv2.imshow('image blue', image_blue)
    # cv2.imshow('edges', edges)
    if cv2.waitKey(5) == 27:
        break

cap.release()
cv2.destroyAllWindows()
