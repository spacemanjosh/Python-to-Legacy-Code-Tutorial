# SEA2018-Python-to-Legacy-Code-Tutorial
This tutorial will teach you how to incorporate code from popular scientific processing packages (such as IDL and Matlab) into your Python processing pipeline. This will allow you to tie together scientific code written in different languages, seamlessly.

We will be utilizing Python bridge utilities built into the most recent versions of IDL and Matlab.  As such, it is important to install compatible versions of Python and either IDL or Matlab.

Recomended versions are:  
Python 2.7, 3.5 or 3.6  
IDL 8.6.1 or higher  
Matlab R2016a or higher

For this tutorial I'll be demonstrating this functionality using the following software versions:  
Python 3.6  
IDL 8.6.1  
Matlab R2018a

# Python Setup

I recommend that you install the [Anaconda Python](https://www.anaconda.com/download) package because it includes many of the popular scientific packages already, and will greatly simplify your life.  But this is by no means a requirement.  You are free to use any Python installation as long as it meets the requirements listed above.

# Matlab setup

To wire up Matlab to your python installation, you'll need to follow the steps listed here.
https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html
For example, on a mac environment, the steps looks like this:

`cd /Applications/MATLAB_R2018a.app/extern/engines/python/`  
`python setup.py install`

# IDL setup

Note, for the Mac platform, the steps listed in the link below are incomplete, in that you will need to also add the following line to your sudoers by performing the following steps prior to executing the steps in the :  
Open your sudoers file with `sudo visudo`  
Add the line `Defaults         env_keep += "PYTHONHOME"` to the sudoers file.  

Next, follow the instructions listed here:  
http://www.harrisgeospatial.com/docs/python.html#Installation  
For Windows and Linux, the setup instructions are fairly simple.  For Mac systems however, you will need to have `sudo` privileges on your machine to execute the setup script.  If you do not have `sudo` privileges on your machine, you'll have to talk with your IT or sys-admin about executing these steps.  



