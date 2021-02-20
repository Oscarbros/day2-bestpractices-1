# Program to multiply two matrices using nested loops
import random
import line_profiler 
# from memory_profiler import profile
profile = line_profiler.LineProfiler()

N = 250

#Line profiling
@profile
def matmult(N):
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    
    for r in result:
        print(r)

# matmult(N)
profile_wrapper = profile(matmult)
profile_wrapper(N)
profile.print_stats()
print('I would look into line 13, 17, 29 and 30 primarily in terms of time, however the for-loops are also an issue')

# mprofile_wrapper = mprofile(matmult)
# mprofile_wrapper(N)
# mprofile.print_stats()