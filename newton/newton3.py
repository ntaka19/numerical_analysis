from decimal import *
def newton(x,eps):
    delta = x
    def G(x):
       return Decimal(x**3-Decimal(0.1**20))
    def g(x):
       return 3*x**2
    while delta >eps :
        x0 = x
        x = x0-Decimal(G(x0)/g(x0))
        delta =abs(x-x0)
        print "x_n=",x
        print "delta = ",delta

newton(1,0.00000000001)

#http://docs.python.jp/3/library/decimal.html
