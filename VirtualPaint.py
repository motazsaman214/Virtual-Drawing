
import cv2
import numpy as np

frameWidth = 1200
frameHeight = 900

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

myColors = [ [99, 231, 0, 113, 255, 255]]      # BLUE

myColorValues = [  
                 [255, 0, 0]   # BGR for BLUE
                 ]

myLetters = [[]]  # Initialize with an empty array

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for color, colorValue in zip(myColors, myColorValues):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        if x != 0 and y != 0:
            newPoints.append([x, y, colorValue])
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgResult = img.copy()

    newPoints = findColor(img, myColors, myColorValues)

    if len(newPoints) != 0:
        # Start a new stroke if there are existing points and the distance is large enough
        if len(myLetters[-1]) > 0 and distance(myLetters[-1][-1][:2], newPoints[0][:2]) > 50:
            myLetters.append([])  # Start a new stroke for a new letter

        myLetters[-1].extend(newPoints)  # Add new points to the current stroke

    # Draw all the strokes
    for stroke in myLetters:
        if len(stroke) > 1:
            for i in range(1, len(stroke)):
                cv2.line(imgResult, (stroke[i - 1][0], stroke[i - 1][1]), (stroke[i][0], stroke[i][1]),
                         stroke[i][2], 9)

    cv2.imshow("Virtual Paint", imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


