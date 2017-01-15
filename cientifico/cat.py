from scipy.misc import imread, imsave, imresize

# Read an JPEG image into a numpy array
img = imread('cat.jpg')
print img.dtype, img.shape  # Prints "uint8 (400, 248, 3)"

# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (400, 248, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively.
img_tinted = img * [1, 0.95, 0.9]

# Resize the tinted image to be 300 by 300 pixels.
img_tinted = imresize(img_tinted, (300, 300))

# Write the tinted image back to disk
imsave('cat_tinted.jpg', img_tinted)

from scipy import io as spio
import numpy as np
a = np.ones((3, 3))
spio.savemat('file.mat', {'a': a})  # savemat expects a dictionary
data = spio.loadmat('file.mat', struct_as_record=True)
data['a']


from scipy import misc
misc.imread('cat.jpg')

import matplotlib.pyplot as plt
plt.imread('cat.jpg')


from scipy import linalg
import numpy as np
arr = np.array([[1, 2],
                [3, 4]])
linalg.det(arr)

arr = np.array([[3, 2],
                [6, 4]])
linalg.det(arr)

linalg.det(np.ones((3, 4)))  # Lanza un error as spected

arr = np.array([[1, 2],
                [3, 4]])
iarr = linalg.inv(arr)
iarr
np.allclose(np.dot(arr, iarr), np.eye(2))  # Prueba que
# la multiplicación de una matriz por su inversa sea la
# matriz identidad.

arr = np.array([[3, 2],
                [6, 4]])
linalg.inv(arr)
