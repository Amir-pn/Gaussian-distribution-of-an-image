import skimage
from skimage import io
import matplotlib.pyplot as plt
from skimage.filters import gaussian

img3= io.imread(".../image.jpg",as_gray=True)
gaus1= gaussian(img3,sigma= 1.3)
plt.figure('gaussian_1')
plt.imshow(gaus1,cmap='gray')
gaus2= gaussian(img3,sigma= 0.7)
plt.figure('gaussian_0.5')
plt.imshow(gaus2,cmap='gray')
gaus3= gaussian(img3,sigma= 0.08)
plt.figure('gaussian_0.09')
plt.imshow(gaus3,cmap='gray')
plt.imsave(".../Image_1.jpg",gaus1,cmap='gray')
plt.imsave(".../Image_2.jpg",gaus2,cmap='gray')
plt.imsave(".../Image_3.jpg",gaus3,cmap='gray')
plt.show()
