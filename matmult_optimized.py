# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:39:50 2021

@author: oscbr226
"""

import line_profiler 
import numpy as np
from memory_profiler import profile
# profile = line_profiler.LineProfiler()

N = 250

#Line profiling
@profile
def matmult_optimized(N):
    mat1 = np.random.randint(0,high=100,size = (N,N))
    mat2 = np.random.randint(0,high=100, size=(N,N+1))
    
    matMult = np.matmul(mat1,mat2)
    print(matMult)

matmult_optimized(N)
# profile_wrapper = profile(matmult_optimized)
# profile_wrapper(N)
# profile.print_stats()

'''It took me ~20 s to run matmult.py while matmult_optimized.py took ~0.04 s
so that's a pretty significant improvement.'''

'''Memory usage was also much lower. I never finished running matmult.py with 
N=250, but with N=100 memory was around 115 MiB while here it is 69.5 MiB
when N = 250, so that's much better'''