import cv2 

# Open an Original Image
image = cv2.imread("profile.jpg")
print(image.shape)
# Rename the Window Name
window_name = "Original Image"

# Open an IMREAD_COLOR Image
image1 = cv2.imread("profile.jpg",1)
print(image1.shape)
# Rename the Window Name
window_name1 = "IMREAD_COLOR Image"

# Open an IMREAD_GRAYSCALE Image
image2 = cv2.imread("profile.jpg",0)
print(image2.shape)
# Rename the Window Name
window_name2 = "GRAYSCALE Image"

# Open an IMREAD_UNCHANGED Image
image3 = cv2.imread("profile.jpg",-1)
print(image3.shape)
# Rename the Window Name
window_name3 = "IMREAD_UNCHANGED Image"

# Display Original Image on Window
cv2.imshow(window_name,image)
cv2.imshow(window_name1,image1)
cv2.imshow(window_name2,image2)
cv2.imshow(window_name3,image3)

# Convert the image to grayscale
grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)



# Convert Image to Black and White
(thresh, blackAndWhiteImage) = cv2.threshold(grey_img, 127, 255, cv2.THRESH_BINARY)