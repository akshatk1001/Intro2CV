import cv2
import os
import matplotlib.pyplot as plt

image = cv2.imread("/Users/aneeshkhandelwal/Downloads/VSCode Projects/Intro2CV/Tomatoes.png")

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