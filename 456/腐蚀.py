import cv2
import numpy as np
img=cv2.imread('C:/Users/A/Desktop/1234/1.png',0)
#Opencv定义结构元素
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

#腐蚀图像
eroded=cv2.erode(img,kernel)
#显示
cv2.imshow('Eroded Image',eroded)


#膨胀图像
dilated=cv2.dilate(img,kernel)
#显示图像
cv2.imshow('Dilated Image',dilated)

#Numpy定义的结构元素
NpKernel=np.uint8(np.ones((3,3)))
Nperoded=cv2.erode(img,NpKernel)
#显示腐蚀后的图像
cv2.imshow('Eroded by Numpy kernel',Nperoded)

cv2.waitKey(0)
cv2.destroyAllWindows()