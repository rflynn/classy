# ex: set ts=4 et:
import cv
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
from collections import Counter

def rgb_distance((r0,g0,b0), (r1,g1,b1)):
    return abs(r0 - r1) + \
           abs(g0 - g1) + \
           abs(b0 - b1)

img = cv2.imread(sys.argv[1])
height, width, depth = img.shape
pixels = cv.fromarray(img)

cnt = Counter()

for i in xrange(0, height):
    for j in xrange(0, width):

        pixel_value = cv.Get2D(pixels, i, j)
        # Since OpenCV loads color images in BGR, not RGB
        b = pixel_value[0]
        g = pixel_value[1]
        r = pixel_value[2]

	cnt[(int(r),int(g),int(b))] += 1

        #  cv.Set2D(result, i, j, value)
        #  ^ to store results of per-pixel
        #    operations at (i, j) in 'result' image

print sorted(cnt.iteritems(),
             key=lambda x:x[1],
             reverse=True)[:20]

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
#plt.xticks([]), plt.yticks([])
plt.show()

