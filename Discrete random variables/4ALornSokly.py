# This is my solution and I didn't copy or sent it to the others
#Lorn Sokly N42TNN


from math import comb
import math
class Drv:
    
    name = "Discrete random variable"    # class variable   
    
    def __init__(self, xk=[0], pk=[1]):   
        
        self.xk = xk                   # instant variable
        self.pk = pk                   # instant variable


    def pdf(self, x):   # x is any real number
        
        for m in range(len(self.xk)):
            if x==self.xk[m]:
                return self.pk[m]
        return 0
            
    def cdf(self, x):  # x here can be a float number  
        return sum([self.pk[m] for m in range(len(self.xk)) if self.xk[m] <x]) 
        
    def e(self):  
        return sum([self.xk[i]*self.pk[i] for i in range(len(self.xk))])
    
    def is_nonneg(self):
        
        return all((val>0 for val in self.xk))  #val=value of the random variable
    
        
    def reweight(self):    
        self.p1k=[self.xk[i]*self.pk[i]/self.e() for i in range(len(self.xk))]
        class reweight(Drv):
            def __init__(self, xk, pk):
                super().__init__(xk, pk)
        return reweight(self.xk,self.p1k)


    def __repr__(self):
        xk = self.xk
        pk = self.pk
        n = len(xk)
        x = '' . join(['('+str(xk[i]) + ', ' + str(pk[i]) + ') '
                      for i in range(min(n, 10))])
        if n > 10:
            x += '...'
        return self.name + ": " + x


class Binomial(Drv):

    name = "Binomial random variable"

    def __init__(self, n=1, p=1):
        self.n = n
        self.p = p
        
        values=[i for i in range(0,n+1)]
        probabilities=[math.comb(n,i)*pow(p,i)*pow(1-p,n-i) for i in range(0,n+1)]
        super().__init__(values, probabilities) # inheritance

    def e(self): 
        return self.n*self.p


    def is_nonneg(self):  
        return True

class Uniform(Drv):
    
    #n is the number a values (which are 1,2,...,n).

    name = "Uniform random variable"

    def __init__(self, n=1):
        self.n = n        
        values=[i for i in range(1,n+1)]       
        probabilities=[1/n]*n
        super().__init__(values, probabilities)
        
    def e(self):
        return (self.n+1)/2  # the formula for the expected value of uniform dis. is: n/2

    def is_nonneg(self):
        return True