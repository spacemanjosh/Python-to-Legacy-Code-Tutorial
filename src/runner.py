'''
Created on Apr 2, 2018

@author: Josh Elliott : joshua.elliott@lasp.colorado.edu
'''

class runner(object):

    def __init__(self, function):
        '''
        Constructor
        '''
        
        self.function = function
        
    def run(self, *params):
        result = self.function(*params)
        return result
        