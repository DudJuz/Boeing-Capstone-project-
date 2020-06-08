import cv2 as cv
import numpy as np




def circles_image(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 700, param1=200, param2=50, minRadius=200, maxRadius=400)
    
    #coins
    #param1 The high threshold in the detected double threshold, the low threshold is half of it
    #param2 Minimum number of votes (based on the center of the circle)
    #circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 100, param1=80, param2=30, minRadius=50, maxRadius=100)
    
    #burr
    #circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 500, param1=100, param2=30, minRadius=150, maxRadius=250)   
    
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 255), 2)
    cv.imshow("new", image)
#re-write with you own path 
src = cv.imread("C://CV_Final//pdftoimage//image01//image01-1.jpg")
cv.imshow("old", src)
circles_image(src)
cv.waitKey(0)
cv.destroyAllWindows()