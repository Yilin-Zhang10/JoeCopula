# !/usr/bin/env python
# -*- coding: utf-8 -*-

#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Yilin Zhang'

__date__ = '2017-8-18'

__moduleVersion__ = '1.0'

#----------module document----------


#----------module import----------

import numpy as np

#----------module import----------


#----------class definition----------

## JoeCopula (distributed with theta)
class JoeCopula(object): # object waiting to change 
    """
    An joe_copula with one parameter theta.
    Get pdf, cdf, logpdf, sf, logsf given 2D-ndarray,
    seeing each row as a point in distribution.
    
    Parameters
    ----------
        x: 2D-ndarray;
           number in x should be between (0,1);
    theta: float;
    
    Examples
    -----------
    x = np.array([[0.1,0.2,0.3],[0.2,0.3,0.4]])
    myjoe = JoeCopula()
    myjoe.pdf(x,1.2)
    """
    def __init__(self):
        pass
        
    """
    def rvs(self):
        return self._random_state.standard_exponential(self._size)

    """
    
    def cdf(self, x, theta):
        # in two dimension, the equation is 1-cdf = (1-x1)^theta+(1-x2)^theta-((1-x1)^theta*(1-x2)^theta)^(1/theta)
        term = (np.sum((1.0-x)**theta,axis=-1)-np.prod((1.0-x)**theta, axis=-1))**(1.0/theta)
        return 1.0-term
    
    def pdf(self, x, theta):
        term = (np.sum((1.0-x)**theta,axis=-1)-np.prod((1.0-x)**theta, axis=-1))**(1.0/theta)
        # term = (1-x1)^theta+(1-x2)^theta-((1-x1)^theta*(1-x2)^theta)^(1/theta)
        eqa1 = np.prod((1.0-x)**(theta-1.0), axis=-1)*theta*term**(1-theta)
        # eqa1 = (1-x1)^(theta-1)*(1-x2)^(theta-1)*theta*term^(1-theta)
        eqa2 = np.prod((1.0-x)**(theta-1.0), axis=-1)*(theta-1)*term**(1-2*theta)*np.prod(1.0-(1.0-x)**theta, axis=-1)
        # eqa2 = (1-x1)^(theta-1)*(1-x2)^(theta-1)*(theta-1)*term^(1-2*theta)*(1.0-(1.0-x1)^theta)*(1.0-(1.0-x2)^theta)
        return eqa1+eqa2

    def logpdf(self, x, theta):
        return np.log(pdf(x,theta))

    def sf(self, x, theta):
        return 1.0-cdf(x, theta)

    def logsf(self, x, theta):
        return np.log(sf(x,theta))     
#----------class definition----------
        
        

#----------main function----------

if __name__ == '__main__':
    x = np.array([[0.1,0.2,0.3],[0.2,0.3,0.4]])
    myjoe = JoeCopula()
    print myjoe.cdf(x,0.7)
    
#----------main function----------

