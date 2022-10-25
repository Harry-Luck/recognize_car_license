import numpy as np
import cv2
import sys
import imutils
import pytesseract
import cv2 as cv


# Image read and write

image = cv2.imread("images/2.jpg")
if image is None:
    sys.exit("Could not read the image.")
image = imutils.resize(image, width=300 )
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equ = cv.equalizeHist(gray_image)
blur = cv2.medianBlur(equ,3)
ret,thresh = cv.threshold(blur,150,255,cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
x, y, w, h = 0, 0, 0 ,0
for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    if (w/h >4) & (w/h<5):
        # cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        break
print(x, y ,w,h)
re = np.zeros((h,w), dtype = "uint8")
re = equ[y:y+h, x:x+w]
re = imutils.resize(re, width = 300)
cv2.imshow("grge", re)

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'

plate = pytesseract.image_to_string(re, lang='eng')
print("Number plate is:", plate)
cv2.waitKey(0)
cv2.destroyAllWindows()

