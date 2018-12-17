from decimal import *
import numpy as np

def newton(x,eps):
    delta = 1
    def G(x):
       return np.sin(np.radians(x))-np.tan(np.radians(x))
    def g(x):
        return np.cos(np.radians(x))-np.tan(np.radians(x))**(2)-1
    while delta >eps :
        x0 = x
        x = x0-G(x0)/g(x0)
        delta =abs(x-x0)
        print "x_n=",x
        print "delta = ",delta

newton(0.1,0.001)

#http://docs.python.jp/3/library/decimal.html
