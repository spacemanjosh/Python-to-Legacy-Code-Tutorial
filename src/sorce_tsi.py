'''
Created on Apr 4, 2018

@author: elliotjp
'''

import matlab.engine
import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    my_data = np.genfromtxt('data' + os.sep + 'sorce_tsi.txt', delimiter=',')
    
    time = my_data[:,0]
    tsi = my_data[:,1]
    w = np.where( tsi > 0)
    tsi = tsi[w]
    time = time[w]
    
    plt.plot(time, tsi)
    plt.ylim((1360,1363))
#     plt.show()
    
    # Now, call your favorite smoothing function
    eng = matlab.engine.start_matlab()
    windowSize = 100; 
    b = (1/windowSize)* np.ones((1,windowSize), np.double)
    b = matlab.double(b.tolist())
    a = 1;
    tsi = eng.filter(b,a,matlab.double(tsi.tolist()));
    tsi = np.array(tsi._data.tolist()).reshape(time.size)
    
    plt.plot(time, tsi)
    plt.ylim((1360,1363))
    plt.show()