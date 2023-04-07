from math import comb


class Drv:
    """
    Define a class for discrete random variables

    xk is a list of monoton increasing values
    pk is the list of probabilities belonging to xk
    """

    name = "Discrete random variable"    # class variable

    def __init__(self, xk=[0], pk=[1]):
        self.xk = xk                   # instant variable
        self.pk = pk                   # instant variable

    def pdf(self, x):
        """
        Return the value of the probability density function at x.
        x:: any real number
        """
        # TODO
        pass 

    def cdf(self, x):
        """
        Return the value of the cumulative distribution function at x.
        x:: any real number
        """
        # TODO
        pass

    def e(self):
        """
        Return the expected value of the discrete random variable.
        """
        # TODO
        pass

    def is_nonneg(self):
        """
        Return True if the random variable is non negative.
        Otherwise False.
        """
        # TODO        
        pass # return here True or False

    def reweight(self):
        """
        Reweighting a random variable using the expected 
        value of the random variable. 
        """
        # TODO
        pass

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
    """
    Class for binomial random variable derives from Drv.
    Parameters needed: n, p.
    """

    name = "Binomial random variable"

    def __init__(self, n=1, p=1):
        self.n = n
        self.p = p
        # TODO define the list of values and probabilities
        # of the binomial variable
        super().__init__(values, probabilities) # inheritance

    def e(self):
        # TODO rewrite this function, as it can be calculated easier
        pass # return the value here

    def is_nonneg(self):
        return True


class Uniform(Drv):
    """
    Class for a uniform random variable derives from Drv.
    n is the number a values (which are 1,2,...,n).
    """

    name = "Uniform random variable"

    def __init__(self, n=1):
        self.n = n
        # TODO
        # define the values and probabilities of the uniform variable here
        # and complete the code

    def e(self):
        """
        Return the expected value of the uniform random variable.
        """
        # TODO
        pass # return the value here

    def is_nonneg(self):
        return True
