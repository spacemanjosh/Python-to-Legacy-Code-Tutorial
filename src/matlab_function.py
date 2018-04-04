'''
Created on Apr 2, 2018

@author: Josh Elliott : joshua.elliott@lasp.colorado.edu
'''

import matlab.engine

class matlab_function(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        
    def run(self, *params):
        eng = matlab.engine.start_matlab()
        eng.addpath('matlab')
        result = eval("eng." + self.name + "(*params)")
        eng.exit()
        return result
