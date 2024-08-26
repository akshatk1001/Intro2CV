import cv2
import numpy as np

image = cv2.imread("/Users/aneeshkhandelwal/Downloads/VSCode Projects/Intro2CV/RianaHands.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_purple = np.array([120, 50, 20])
upper_purple = np.array([160, 255, 255])

mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
mask_gray = cv2.bitwise_not(mask_purple)

res_purple = cv2.bitwise_and(image, image, mask=mask_purple)
res_gray = cv2.bitwise_and(image_gray, image_gray, mask=mask_gray)
res_gray = np.stack((res_gray,)*3, axis = -1)

final_image = cv2.add(res_purple, res_gray)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Result Purple Mask", cv2.WINDOW_NORMAL)
cv2.namedWindow("Result Gray Mask", cv2.WINDOW_NORMAL)
cv2.namedWindow("Final Image", cv2.WINDOW_NORMAL)

cv2.imshow("Final Image", final_image)
cv2.imshow("Result Purple Mask", res_purple)
cv2.imshow("Result Gray Mask", res_gray)
cv2.imshow("Original Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''Making all colors black except for red'''
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Can also convert to HSV

# LRange = np.array([0, 0, 0])
# URange = np.array([255, 80, 50])

# mask = cv2.inRange(rgb, LRange, URange)

# result = cv2.bitwise_and(rgb, rgb, mask=mask)

# plt.subplot(1, 2, 1) #If using HSV, you don't need to use plt. Can just use cv2.imshow
# plt.title("Original Image")
# plt.imshow(rgb)

# plt.subplot(1, 2, 2)
# plt.title("Detected Image")
# plt.imshow(result)

# plt.waitforbuttonpress()
# plt.close('all')