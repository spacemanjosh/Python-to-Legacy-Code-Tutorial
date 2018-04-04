'''
Created on Apr 2, 2018

@author: Josh Elliott : joshua.elliott@lasp.colorado.edu
'''

class pipeline(object):

    def __init__(self):
        '''
        Constructor
        '''
        
        self.runners = []
        
    def add_step(self, step):
        self.runners.append(step)
        
    def run(self, *params):
        for step in self.runners:
            try:
                params = step.run(*params)
            except TypeError:
                params = step.run(params)
        return params