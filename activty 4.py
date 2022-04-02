import cv2
import matplotlib.pyplot as plt


def read_img(img_name):
    img = cv2.imread(img_name)
    return img


def display_img(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function that plot the histogram of 2 different images
def plot_histogram(img, name):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist, label=name, alpha=0.7, linewidth=1)
    plt.show()
    return hist


def print_shape_and_size(img):
    print('Shape: ', img.shape)
    print('Size: ', img.size)


def loop(img, name):
    display_img(img, name)
    hist = plot_histogram(img, name)
    print(hist)
    convert_to_gray(img)
    display_histogram(img)
    display_edges(img)

# convert image to gray scale
def convert_to_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


# Display the histograms with the source image in one figure. 
# The histograms of the gray_image and the original image is displayed in the same figure.
def display_histogram(img):
    gray = convert_to_gray(img)
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    plt.subplot(2, 2, 2)
    plt.imshow(gray, cmap='gray')
    plt.title('Gray Image')
    plt.subplot(2, 2, 3)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title('Gray Histogram')
    plt.subplot(2, 2, 4)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.title('Original Histogram')
    plt.show()

# display the edges of the grey images
def display_edges(img):
    edges = cv2.Canny(img, 100, 200)
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Edges')
    plt.show()

if __name__ == '__main__':
    img1 = read_img("profile.jpg")
    img1 = loop(img1, "profile1")
    img2 = read_img("prof2.jpg")
    img2 = loop(img2, "profile2")
