# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:00:48 2021

@author: divya
"""


from skimage.io import imsave
from Colorizer import Model
import numpy as np
import matplotlib.pyplot as plt

model = Model()
test_X = np.load( r'test.npy' ) 
model.load_model( r'model.h5' )



values = model.predict( test_X )
values = np.maximum( values , 0 )
for i in range( test_X.shape[0] ):
    image_final = ( values[i] * 255).astype( np.uint8)
    imsave( r'Path for saving the images\{}.jpg'.format( i + 1 ) , image_final )
    
    
