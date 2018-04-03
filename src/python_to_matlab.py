'''
Created on Apr 2, 2018

@author: Josh Elliott : joshua.elliott@lasp.colorado.edu
'''

import matlab.engine
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

if __name__ == '__main__':
    eng = matlab.engine.start_matlab()
    eng.addpath('matlab')
    
    val = eng.factorial(10)
    print(val)
    
    val = eng.fibonacci(10)
    print(val)
    
    file = 'data' + os.sep + '20130502_214512_1024_0171.jpg'
    plt.imshow(Image.open(file))
    plt.show()
    
    img = eng.edge_detect(file)
    
    edge_img = np.array(img._data.tolist()).reshape(img.size)
    
    plt.imshow(edge_img)
    plt.show()
    
    eng.quit()
    