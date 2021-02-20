#!/usr/bin/python

from math import ceil,sqrt
# import line_profiler
# profile = line_profiler.LineProfiler()
from memory_profiler import profile

@profile
def gen_primes(n):
    l = range(2,n)
    primes = []
    for j in range(0,len(l)):
        p = True
        for d in primes:
            if(d > sqrt(l[j])):
                break
            if(l[j] % d == 0):
                p = False
                break;
        if(p):
            primes.append(l[j])

    return primes

@profile
def factorize(n,primes):
    factors = []
    init_n = n
    for p in primes:
        while(n%p == 0):
            n = n/p
            factors.append(p)
        if(p > sqrt(n)):
            break
    if(n > 1):
        factors.append(n)
    return factors

    
def phi(n,primes):
    factors = factorize(n,primes)
    p = 1

    for i in range(2,n):
        flag = True
        for f in factors:
            if i%f == 0:
                flag = False
                break
        if flag:
            p+=1
    return p

@profile
def fast_phi(n,primes):
    factors = factorize(n,primes)
    phi = factors[0]-1
    for i in range(1,len(factors)):
        if(factors[i] == factors[i-1]):
            phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
        else:
            phi *= (factors[i]-1)
    return phi

primes = gen_primes(1000)
m = 10000
#m = 8
fraq = 0
for i in range(2,m+1):
    fraq += fast_phi(i,primes)

print(fraq)
# profile_wrapper = profile(gen_primes)
# profile_wrapper(1000)
# profile.print_stats()

'''When using line-profiler for gen_primes I would primarily look into line 14 
and line 16. These lines are called often and take a lot of time'''

'''When using line-profiler for factorize line 28, 29 and 32 get called the 
most often and are time consuming so these could be optimized'''

'''When using line-profiler for fast_phi it is mostly running factorize that
is time consuming, however within this function line 57 and 58 are quite time
consuming.'''








