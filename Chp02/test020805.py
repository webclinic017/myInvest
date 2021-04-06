import matplotlib.pyplot as plt          # pip install matplotlib
import matplotlib.image as mping

plt.suptitle("Image Processing", fontsize=18)
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(mping.imread('src.png'))

plt.subplot(122)
plt.title("Pseudo Color Image")
dst_img = mping.imread('dst.png')
pseudo_img = dst_img[:, :, 0]
plt.imshow(pseudo_img)

plt.show()