def func(x,n): 
    def G(x):
        return x**3 - 10
    def g(x):
        return 3*x**2
    print (G(x))
    print (g(x))
    for i in range (1,n+1): 
        x = x-float(G(x)/ g(x))
        print(x)
print (func(1,15))


 

