from PIL import Image

import numpy as np
import bisect
import logging

from scipy import misc

import skimage
import skimage.color

from skimage import exposure
#from skimage import feature

class MoleImage:
    def __init__(self, img):
        self._img = np.array(img)

    def process(self):
        res = skimage.color.rgb2gray(self._img)
        res = exposure.adjust_log(res)
        #res = feature.canny(res)
        return misc.toimage(res)

    def read_chan(self, img, chan):
        img = img.copy()
        if chan != 'r':
            img[:, :, 0] = 0
        if chan != 'g':
            img[:, :, 1] = 0
        if chan != 'b':
            img[:, :, 2] = 0

        return img

    #def im2double(self, img):
    #    min_val = np.min(img.ravel())
    #    max_val = np.max(img.ravel())
    #    return (img.astype('float') - min_val) / (max_val - min_val)
