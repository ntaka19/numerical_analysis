from decimal import *
import numpy as np

def newton(x,eps):
    delta = 1
    def G(x):
       return np.cos(x)+(x+1)*np.exp(x)
    def g(x):
        return -1*np.sin(x)+(x+2)*np.exp(x)
    while delta >eps :
        x0 = x
        x = x0-G(x0)/g(x0)
        delta =abs(x-x0)
        print "x_n=",x
        print "delta = ",delta

newton(-7,0.00000000001)

#http://docs.python.jp/3/library/decimal.html
