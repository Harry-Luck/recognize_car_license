from email.mime import image
import cv2
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'

image = cv2.imread('car.jpg')
image = imutils.resize(image, width=300)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image1 = cv2.bilateralFilter(gray_image, 11,17,17)
cv2.imshow("original image", gray_image)
cv2.imshow("eee", gray_image1)
edged = cv2.Canny(gray_image1, 30, 200)

cnts, new = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
cv2.imshow("countours", image2)
cv2.drawContours(image2, cnts, -1,(0, 255, 0),3)
cnts = sorted(cnts, key= cv2.contourArea, reverse=True)[:30]
screenCnt = None
image3 = image.copy()

cv2.imshow('Top30contours', image3)

i = 7
for c in cnts:
    perimeter = cv2.arcLength(c,True)
    print(c, 'eseeffs', perimeter)
    approx = cv2.approxPolyDP(c, 0.04*perimeter, True)
    print("eee",approx, "esreerr")
    if len(approx) == 4:
        screenCnt = approx
        x,y,w,h = cv2.boundingRect(c)
        new_img = image[y:y+h, x:x+w]
        cv2.imwrite('./'+str(i)+'.png', new_img)
        i+=1
        break;
print(screenCnt)
cv2.drawContours(image, [screenCnt], -1, (0,255, 0),3)
cv2.imshow('imagewith detectd', image)
cropped_loc = './7.png'
cv2.imshow('cropped', cv2.imread(cropped_loc))
plate = pytesseract.image_to_string(cropped_loc, lang='eng')
print("Number plate is:", plate)
cv2.imshow("edge", edged)
cv2.waitKey(0)
