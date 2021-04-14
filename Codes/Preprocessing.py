# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:05:05 2021

@author: divya
"""

from Parser import Parser
from skimage.io import imsave
import numpy as np
from skimage.io import imread

   
parser = Parser( 128 )
print( 'Data Pre Processing.....' )
X = parser.prepare_images_from_dir( r'Train images path' , 'grayscale' )
Y = parser.prepare_images_from_dir( r'Train images path' )
test = parser.prepare_images_from_dir( r'Test images path' , 'grayscale' )

np.save( r'X.npy' , X )
np.save( r'Y.npy' , Y )
np.save( r'test.npy' , test )
print( 'Data Processed' )
