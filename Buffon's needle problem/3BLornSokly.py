# This is my solution and I didn't copy or sent it to the others
#Lorn Sokly N42TNN

import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import random
from scipy.stats import binom
import math
import sys, os


def Buffon(N,L):
    
    Xe=[]
    Ye=[]
    Xs=[]
    Ys=[]  
    
    angle=[random.uniform(0,math.pi/2) for i in range(N)]  #random angle    
    Xc=[random.uniform(0,1) for i in range(N)]      # random center
    Yc=[random.uniform(0,1) for i in range(N)]
    
    for j in range(len(Yc)):
        Xe.append(Xc[j]+(L/2)*np.cos(angle[j]))  # the one end of needle, coordinate x
        Ye.append(-Yc[j]+(L/2)*np.sin(angle[j]))  # the one end of neeedle, coordinate y
        
        Xs.append(Xc[j]-(L/2)*np.cos(angle[j]))  # the other end of needle, coordinate x
        Ys.append(-Yc[j]-(L/2)*np.sin(angle[j]))  # the other end of needle, coordinate x
        
        hit=[]
        for k in range(len(Ye)):
            hit.append(np.abs(np.floor(Ys[k]))+np.floor(Ye[k]))

    #print("coordinate of the 1st end",Ys) # try checking the list Ys
    #print("coordinate of the 2nd end",Ye) # try checking the list Ye
    #print("list of sorted hit",sorted(hit)) # try checking the list hit
    #print("center Yc",Yc)
    #print(np.abs(np.floor(Ys[0]))+np.floor(Ye[0]))
    
    y=[i/N for i in range(N)]
    x=sorted(hit)
    
    
    #print(x,y)
    
    plt.figure(figsize=(7, 5))
    plt.step(x, y)
    plt.title("Experimental cumulative distribution function of X on N experiments")
    plt.show()
    
def main():
    N = int(sys.argv[1])
    L = float(sys.argv[2])
    Buffon(N,L)
if __name__ == "__main__":
    main()  

# coordinate of x is not important, but I put it down anyway

