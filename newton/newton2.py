from decimal import *
def newton(x,eps,alpha):
    delta = x

    def G(x):
       return x**3-10
    def g(x):
       return 3*x**2
    while delta >eps :
        x0 = x
        x = x0-Decimal(G(x0)/g(x0))
        delta =abs(x-x0)
        convergence = Decimal(abs(x0-alpha)**2)-abs(x-alpha)
        print "x_n=",x
        print "delta = ",delta
        print "convergence=",convergence 

newton(1,0.00000000001,Decimal(2.1544346900318837217592935665))

#http://docs.python.jp/3/library/decimal.html
