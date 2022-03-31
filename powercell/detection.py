import cv2 as cv
import numpy as np
import json
import random

camera = cv.VideoCapture(0, cv.CAP_DSHOW)

#Distance function
def getDistance(focal_length, real_width, width_in_frame):
    distance = (real_width * focal_length) / width_in_frame
    
    return distance
    
#Draw circle if contour is a circle
def isCircle(img, contour):
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    
    (coord_x, coord_y), radius = cv.minEnclosingCircle(contour)
    center = (int(coord_x), int(coord_y))
    
    contour_area = cv.contourArea(contour) 
    x, y, w, h = cv.boundingRect(contour)
    aspect_ratio = w/h
    percentage = str(random.randint(20, 100))  
    if  1.0 >= contour_area / (radius**2 * 3.14) >= .6 and 1.4 >= aspect_ratio >= .6 and contour_area > 200:            
        cv.circle(img, center, int(radius), (0, 255, 0) , 3)
        cv.putText(img, f"Powercell %{percentage}", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
def getContours(mask):
    global contours
    contours = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if len(contours) == 2:
        contours = contours[0]
        
    else:
        contours = contours[1]
    
    return contours 
    
    
def createMask(img):
    #blue values 
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([20, 100, 100])
    upper = np.array([30, 255, 255])
    mask = cv.inRange(hsv, lower, upper)

    return mask
        
#Call functions and process feed
while True:
    ret, frame = camera.read()
    for contour in getContours(createMask(frame)):
        isCircle(frame, contour)
        
    cv.imshow('display', frame)
    key = cv.waitKey(1)
    if key == 27:
        break
    
camera.release()
cv.destroyAllWindows()
    
    
    


