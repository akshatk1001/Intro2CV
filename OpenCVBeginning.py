import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

imageTomatoes = cv2.imread("/Users/aneeshkhandelwal/Downloads/VSCode Projects/Intro2CV/Tomatoes.png")
imageRiana = cv2.imread("/Users/aneeshkhandelwal/Downloads/VSCode Projects/Intro2CV/RianaHands.jpeg")
imageMedianBlur = cv2.imread("/Users/aneeshkhandelwal/Downloads/VSCode Projects/Intro2CV/MedianBlurLena.png")

'''Showing image using OpenCV'''
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''Showing image using Matplotlib'''
# plt.imshow(image)
# plt.waitforbuttonpress()
# plt.close('all')

'''Changing the file type using OpenCV and deleting using OS'''
# cv2.imwrite("convertTojpg.jpg", image)
# print(os.listdir("/Users/aneeshkhandelwal/Downloads/VSCode Projects/Intro2CV/"))
# os.remove("/Users/aneeshkhandelwal/Downloads/VSCode Projects/Intro2CV/convertTojpg.jpg")

'''Adding images with different sizes/aspect ratios together'''
# newRiana = cv2.resize(imageRiana, (imageTomatoes.shape[1], imageTomatoes.shape[0]), interpolation = cv2.INTER_AREA)

# new_image = cv2.addWeighted(imageTomatoes, 0.5, newRiana, 0.5, 0)
# subtract_image = cv2.subtract(imageTomatoes, newRiana)

# cv2.imshow("pic", new_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows

'''Blurring Images'''
# cv2.imshow("Original Image", imageRiana)
# cv2.imshow("Original Median Blur", imageMedianBlur)

# kernels = [(15, 15)]
# parameters = [(30, 45, 30)]

# for (x, y) in kernels:
#     blur = cv2.blur(imageRiana, (x, y)) #Just normal blur of image
#     cv2.imshow("Normal Blur x:{}, y:{}".format(x, y), blur)

#     blurred_image = cv2.GaussianBlur(imageRiana, (x, y), 0) #For images with some noise
#     cv2.imshow("Gausian Blur x:{}, y:{}".format(x, y), blurred_image)

# median_blur = cv2.medianBlur(imageMedianBlur, 7) #Used for when image has ALOT of noise (salt and pepper)
# cv2.imshow("Median Blur 7", median_blur)

# for(diameter, sigmaColor, sigmaSpace) in parameters:
#     bilateral_blur = cv2.bilateralFilter(imageRiana, diameter, sigmaColor, sigmaSpace) # Reduce noise while still maintaining edges
#     cv2.imshow("BilateralBlur d:{}, sC:{}, sWS:{}".format(diameter, sigmaColor, sigmaSpace), bilateral_blur)

# cv2.waitKey(0)
# cv2.destroyAllWindows()