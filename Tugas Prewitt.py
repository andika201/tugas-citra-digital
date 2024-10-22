import cv2
import numpy as np

# Membaca citra grayscale
img = cv2.imread('C:/Users/user/Downloads/belgian-waffle-recipe-003.jpg', 100)

# Mendefinisikan kernel Prewitt
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# Konvolusi dengan kernel
sobelx = cv2.filter2D(img, cv2.CV_64F, kernel_x)
sobely = cv2.filter2D(img, cv2.CV_64F, kernel_y)

# Menghitung magnitudo gradien
mag = np.sqrt(sobelx**2 + sobely**2)

# Normalisasi
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
mag = mag.astype(np.uint8)

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Sobel x', sobelx)
cv2.imshow('Sobel y', sobely)
cv2.imshow('Sobel Magnitude', mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
