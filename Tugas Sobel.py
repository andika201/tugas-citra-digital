import cv2
import numpy as np

# Membaca gambar dari file
img = cv2.imread('C:/Users/user/Downloads/Waffle.jpg', 100)

# Menggunakan operator Sobel untuk mendeteksi tepi
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Gradien tepi pada arah X
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Gradien tepi pada arah Y

# Menghitung magnitudo gradien
sobel_combined = cv2.magnitude(sobelx, sobely)

# Mengkonversi hasil ke format 8-bit untuk visualisasi
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobel_combined = cv2.convertScaleAbs(sobel_combined)

# Menampilkan gambar asli dan hasil deteksi tepi Sobel
cv2.imshow('Gambar Asli', img)
cv2.imshow('Tepi Sobel X', sobelx)
cv2.imshow('Tepi Sobel Y', sobely)
cv2.imshow('Tepi Sobel Gabungan', sobel_combined)

# Menunggu hingga tombol ditekan dan menutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()