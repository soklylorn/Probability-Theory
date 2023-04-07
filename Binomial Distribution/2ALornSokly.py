# This is my solution and I didn't copy or sent it to the others
# LORN SOKLY
# N42TNN


import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import random
from scipy.stats import binom
import sys

def P(n, p, k):
 
    dist=[]
    poi=[]
    lamda=n*p
    for i in range(n+1):
        dist.append(math.comb(n,i)*pow(p,i)*pow(1-p,n-i))  # binomial distribution
        poi.append((pow(lamda,i)/math.factorial(i))* math.exp(-lamda))  # Poisson distribution

    x=np.random.binomial(n, p, k)
    sim = [np.equal(x,i).mean() for i in range(n)]   #simulate the binomial k times
    
    plt.figure(figsize=(12, 3))
    
    plt.subplot(131)                         # the first diagram
    plt.bar(list(range(n+1)),dist)
    plt.title('Binomial Distribution')
    
    plt.subplot(132)                          #the second diagram
    plt.bar(list(range(n)),sim)
    plt.title('Simulated binomial distribution')
    
    plt.subplot(133)                         # the third diagram
    plt.bar(list(range(n+1)),poi)
    plt.title('Approximated with Poisson-distribution')
    plt.show()

def main():    
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    k = int(sys.argv[3])
    P(n,p,k)
if __name__ == "__main__":
    main()
    	