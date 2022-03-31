def isCircle(img, contour, color):  
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
   
    (coord_x, coord_y), radius = cv.minEnclosingCircle(contour)
    center = (int(coord_x), int(coord_y))
   
    contour_area = cv.contourArea(contour)
    x, y, w, h = cv.boundingRect(contour)
    aspect_ratio = w/h

   
    if  1.0 >= contour_area / (radius**2 * 3.14) >= .8 and 1.1 >= aspect_ratio >= .8 and contour_area > 200:
            return True
    return False
