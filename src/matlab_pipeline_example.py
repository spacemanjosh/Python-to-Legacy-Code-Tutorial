'''
Created on Apr 2, 2018

@author: Josh Elliott : joshua.elliott@lasp.colorado.edu
'''

import matlab.engine
from runner import runner
from pipeline import pipeline

if __name__ == '__main__':
    eng = matlab.engine.start_matlab()
    eng.addpath('matlab')
    
    func1 = eng.fibonacci
    runner1 = runner(func1)
    func2 = eng.factorial 
    runner2 = runner(func2)
    
    result = runner1.run(7)
    print(result)
    
    result = runner2.run(result)
    print(result)
    
    # Build a pipeline
    pipe = pipeline()
    pipe.add_step(runner1)
    pipe.add_step(runner2)
    
    # Run it
    result = pipe.run(7)
    print(result)