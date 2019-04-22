import cv2
import numpy as np

img=cv2.imread('C:/Users/A/Desktop/123/1.bmp',0)
#定义结构元素
Kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#闭运算
closed=cv2.morphologyEx(img,cv2.MORPH_CLOSE,Kernel)
cv2.imshow('Close',closed)


#开运算
opened=cv2.morphologyEx(img,cv2.MORPH_OPEN,Kernel)
cv2.imshow('OPen',opened)

cv2.waitKey(0)
cv2.destroyAllWindows()