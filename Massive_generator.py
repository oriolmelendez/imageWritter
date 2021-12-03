#!/usr/bin/python3
import cv2

def createBullets(number):
    #Path image
    image = cv2.imread('image.png')

    if image.any():
        #Put text in image
        cv2.putText(image,str(number),(1492,1025),cv2.FONT_HERSHEY_SIMPLEX,5,(41,40,150),12)
        #Write new image file
        cv2.imwrite('newImage.png',image)

#Iterate with for loop for images creation
for x in range(821,1001):
    createBullets(x)

print("Images created")