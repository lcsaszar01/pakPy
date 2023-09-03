#!/usr/bin/env python3

'''Credit to @Dennis Ganzaroli From Medium for creating this code.
https://medium.com/mlearning-ai/install-tensorflow-on-mac-m1-m2-with-gpu-support-c404c6cfb580'''


import sys
import pandas as pd
import sklearn as sk
import scipy as sp
import platform
import stats

def precheck():
    stats.sysinto()
    print('\n')
    print(f"Python Platform: {platform.platform()}")
    print(f"Python {sys.version}")
    print(f"Pandas {pd.__version__}")
    print(f"Scikit-Learn {sk.__version__}")
    print(f"SciPy {sp.__version__}")


    
    
    
    