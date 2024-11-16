import cv2
import numpy as np

image = cv2.imread("/Users/akshatk/Coding/PersonalCoding/Intro2CV/RianaHands.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_face = np.array([0, 50, 20])
upper_face = np.array([13, 255, 255])

lower_purple = np.array([120, 50, 20])
upper_purple = np.array([160, 255, 255])

mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
mask_face = cv2.inRange(hsv, lower_face, upper_face)
masks_added = cv2.add(mask_purple, mask_face)
mask_gray = cv2.bitwise_not(masks_added)

res_purple = cv2.bitwise_and(image, image, mask=mask_purple)
res_gray = cv2.bitwise_and(image_gray, image_gray, mask=mask_gray)
res_face = cv2.bitwise_and(image, image, mask = mask_face)
res_gray = np.stack((res_gray,)*3, axis = -1)

final_image = cv2.add(res_purple, res_gray)
final_image = cv2.add(final_image, res_face)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Final Image", cv2.WINDOW_NORMAL)

cv2.imshow("Original Image", image)
cv2.imshow("Final Image", final_image)

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

#For help used: https://medium.com/featurepreneur/colour-filtering-and-colour-pop-effects-using-opencv-python-3ce7d4576140 