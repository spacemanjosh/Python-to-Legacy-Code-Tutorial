'''
Created on Apr 2, 2018

@author: elliotjp
'''

import os
import matplotlib.pyplot as plt
from PIL import Image

if __name__ == '__main__':
    from idlpy import *
    
    path = getattr(IDL, "!path")
    setattr(IDL, "!path", path + ":" + os.getcwd() + os.sep + 'idl')
    
    val = IDL.factorial(10)
    print(val)
    
    val = IDL.fibonacci(10)
    print(val)
    
    file = 'data' + os.sep + '20130502_214512_1024_0171.jpg'
    plt.imshow(Image.open(file))
    plt.show()
    
    edge_img = IDL.edge_detect(file)
    
    plt.imshow(edge_img)
    plt.show()
    
    IDL.exit()