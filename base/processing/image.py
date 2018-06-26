from PIL import Image

import numpy as np
import bisect
import logging

from scipy import misc

import skimage
import skimage.color

from skimage import exposure
from skimage import feature
from skimage import morphology
from skimage import measure

from scipy.ndimage.morphology import binary_fill_holes

class MoleImage:
    def __init__(self, img):
        self._img = np.array(img)

    def findEthalonContours(self, grayImg):
        ethalon = exposure.adjust_log(grayImg)
        ethalon = feature.canny(ethalon, low_threshold=0.15, high_threshold=0.15, sigma=10)
        ethalon = binary_fill_holes(ethalon)

        se = morphology.disk(1, int)
        ethalon = morphology.binary_opening(ethalon, se)

        contours = measure.find_contours(ethalon, 0.99) # countours coordinates will be returned here
        logging.error(">>>>>>>>>>>>>>>>>>>>>>")
        logging.error(">>>>>>>>>>>>>>>>>>>>>>")
        logging.error(contours)
        logging.error(">>>>>>>>>>>>>>>>>>>>>>")
        logging.error(">>>>>>>>>>>>>>>>>>>>>>")

    def process(self):
        grayImg = skimage.color.rgb2gray(self._img)
        self.findEthalonContours(grayImg)

        res = grayImg > 0.7         # Convert image to Blak-White image with threshold 0.7
        res = 1 - res.astype(int)   # Invert image

        return misc.toimage(res)
