from decimal import *
import numpy as np

def newton(x,eps):
    delta = x
    def G(x):
       return np.tanh(x)+0.2*x+0.3
    def g(x):
       return 1-np.tanh(x)**2+0.2
    while delta >eps :
        x0 = x
        x = x0-G(x0)/g(x0)
        delta =abs(x-x0)
        print "x_n=",x
        print "delta = ",delta

newton(1.3,0.00000000001)

#http://docs.python.jp/3/library/decimal.html
