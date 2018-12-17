from pprint import pprint
from numpy import max,array,zeros,diag,diagflat,dot
import numpy as np
import time 

def jacobi(A,b,N=30,x=None):
    if x is None:
        x = zeros(len(A[0]))
    
    D = diag(A)
    R = A - diagflat(D)

    for i in range(N):
        x = (b-dot(R,x))/D
    return x

#create n_yutaikaku
def n_yutaikaku(n):
    A = []
    for i in range(n):
        a = np.random.rand(n)*10
        c = sum(a) 
        
        a[i]=np.random.rand()*10+c-a[i]
        A.append(a)
    #print(A)
    return A

def main(n):
    start = time.time()
    """"
    for i in range (5,5*(n+1),5):
        A = n_yutaikaku(i)
        b = np.random.rand(i)
        x0 = np.random.rand(i)
        sol = jacobi(A,b,N=25,x=x0)
        pprint(sol)
    """
    A = n_yutaikaku(n)
    b = np.random.rand(n)
    x0 = np.random.rand(n)
    sol = jacobi(A,b,N=25,x=x0)
    pprint(sol)

    elapsed_time = time.time()-start
    print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
main(10000)

