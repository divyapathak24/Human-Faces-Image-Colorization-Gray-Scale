# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:08:41 2021

@author: divya
"""

#For RGB to Gray training images conversion and dimension rescaling
from Parser import Parser
from skimage.io import imsave
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from skimage import color
import os

dir_path = "Put here the directory consisting of RGB images to be converted to Gray scale";
images_names = os.listdir(dir_path)
for imageName in images_names:
   full_path = dir_path + imageName
   image = imread( full_path )
   image = color.rgb2gray(image)
   image = resize( image , ( 128 , 128 , 1 ))
   imsave( 'Path for saving images'.format(imageName),image )
    