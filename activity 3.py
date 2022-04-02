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
    img1 = plot_channels(img)
    display_histogram(img)


def separate_channels(img):
    # split the image into 3 channels
    b, g, r = cv2.split(img)
    print('Shape of blue channel: ', b.shape)
    print('Shape of green channel: ', g.shape)
    print('Shape of red channel: ', r.shape)
    return b, g, r

# plot the different channels
def plot_channels(img):
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
        plt.show()
    return color

# Display the histograms with the source image in one figure. 
# The histograms of the three channels are displayed in the same figure.
def display_histogram(img):
    b, g, r = separate_channels(img)
    color = b, g, r
    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2)
    plt.plot(b)
    plt.title('Blue Channel')
    plt.xticks([]), plt.yticks([]) # locates the x-axis ticks and y-axis ticks
    plt.subplot(2, 2, 3)
    plt.plot(g)
    plt.title('Green Channel')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4)
    plt.plot(r)
    plt.title('Red Channel')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    img1 = read_img("profile.jpg")
    img1 = loop(img1, "profile1")
    img2 = read_img("prof2.jpg")
    img2 = loop(img2, "profile2")
