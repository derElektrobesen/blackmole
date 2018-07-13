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

import cv2

#def process(img):
#    grayImg = skimage.color.rgb2gray(img)
#    findEthalonContours(grayImg)
#
#    res = grayImg > 0.7         # Convert image to Blak-White image with threshold 0.7
#    res = 1 - res.astype(int)   # Invert image
#
#    return res


def renderImage(img, cb, **kwargs):
    img = np.array(img)
    img = cb(img, **kwargs)
    return misc.toimage(img)

def findEthalonContours(grayImg):
    ethalon = exposure.adjust_log(grayImg)
    ethalon = feature.canny(ethalon, low_threshold=0.15, high_threshold=0.15, sigma=10)
    ethalon = binary_fill_holes(ethalon)

    se = morphology.disk(1, int)
    ethalon = morphology.binary_opening(ethalon, se)

    contours = measure.find_contours(ethalon, 0.99) # countours coordinates will be returned here

def grayImage(img):
    return skimage.color.rgb2gray(img)

def bwImage(img):
    return (grayImage(img) > 0.7).astype(int)

def invertedBWImg(img):
    return (1 - bwImage(img)).astype(int)

def adjustedImage(img):
    img = grayImage(img)
    return exposure.adjust_log(img)

def adjustedGammaImage(img):
    img = grayImage(img)
    return exposure.adjust_gamma(img)

def adjustedSigmoidImage(
        img,
        cutoff=0.7,
        gain=10,
        **kwargs,
    ):
    img = grayImage(img)
    return exposure.adjust_sigmoid(img, cutoff=float(cutoff), gain=float(gain))

def imageWithHoles(
        img,
        low_threshold=0,
        high_threshold=0.15,
        sigma=5,
        **kwargs,
    ):
    img = adjustedSigmoidImage(img, **kwargs)
    return feature.canny(
            img,
            low_threshold=float(low_threshold),
            high_threshold=float(high_threshold),
            sigma=float(sigma),
        ).astype(int)

def imageWithFilledHoles(img, **kwargs):
    img = imageWithHoles(img, **kwargs)
    return binary_fill_holes(img).astype(int)

def run_processor(img, processor_type, **kwargs):
    for a in actions:
        if a['name'] == processor_type:
            return renderImage(img, a['cb'], **kwargs)

    return None

actions = (
    #('gray', 'Gray image', grayImage),
    #('bwimg', 'Black-White image', bwImage),
    #('invertedbwimg', 'Inverted Black-White image', invertedBWImg),
    #('adjustedimg', 'Adjusted image', adjustedImage),
    {
        'enabled': False,
        'name': 'adjust_log',
        'description': 'adjust_log image',
        'cb': adjustedImage,
    },
    {
        'enabled': False,
        'name': 'adjust_gamma',
        'description': 'adjust_gamma image',
        'cb': adjustedGammaImage,
    },
    {
        'enabled': True,
        'name': 'adjust_sigmoid',
        'description': 'adjust_sigmoid image',
        'cb': adjustedSigmoidImage,
    },
    {
        'enabled': True,
        'name': 'holesimg',
        'description': 'Image holes',
        'cb': imageWithHoles,
    },
    {
        'enabled': True,
        'name': 'filledholesimg',
        'description': 'Image with filled holes',
        'cb': imageWithFilledHoles,
    },
)
