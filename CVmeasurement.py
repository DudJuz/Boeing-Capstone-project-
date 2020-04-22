#!/usr/bin/env python
# coding: utf-8


import cv2

image = cv2.imread('/Users/apple00882266/Desktop/opencv/6666.png')

# Gray, blur, adaptive threshold
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255,cv2.THRESH_BINARY)[1] #cv2.THRESH_BINARY + cv2.THRESH_OTSU


# Morphological transformations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find contours
cnts = cv2.findContours(opening, cv2.RETR_TREE, cv2.RETR_LIST) # CV_RETR_EXTERNAL, RETR_LIS
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

Q = []
    
for c in cnts:
    # Find perimeter of contour
    perimeter = cv2.arcLength(c, True)
    # Perform contour approximation
    approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)

    # We assume that if the contour has more than a certain
    # number of verticies, we can make the assumption
    # that the contour shape is a circle
    if len(approx) > 6:

        # Obtain bounding rectangle to get measurements
        x,y,w,h = cv2.boundingRect(c)

        # Find measurements
        diameter = w
        radius = w/2

        # Find centroid
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        
       
        W = str(w)
        Q.append(W)
        

        # Draw the contour and center of the shape on the image
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.drawContours(image,[c], 0, (36,255,12), 3)
        cv2.circle(image, (cX, cY), 5, (320, 159, 22), -5) 

        # Draw line and diameter information
        cv2.line(image, (x, y + int(h/2)), (x + w, y + int(h/2)), (156, 188, 24), 1)
    for i in range(len(Q)):
        cv2.putText(image, "Diameter: {}".format(Q[i]), (cX - 50, cY - 100*(i)), cv2.FONT_HERSHEY_SIMPLEX, 1, (156, 188, 24), 1)

cv2.imwrite('/Users/apple00882266/Desktop/opencv/image2333.jpg', image)
cv2.imwrite('/Users/apple00882266/Desktop/opencv/thresh2333.jpg', thresh)
cv2.imwrite('/Users/apple00882266/Desktop/opencv/opening2333.jpg', opening)
