# coding:UTF-8
from pprint import pprint
from numpy import max,array,zeros,diag,diagflat,dot
import numpy as np
import time 

def jacobi(A,b,alpha=0.0001,x=None):
    if x is None:
        x = zeros(len(A[0]))
    
    D = diag(A)
    R = A - diagflat(D)
    delta = 1 
    while delta > alpha:
        x_in = x 
        x = (b-dot(R,x))/D
        #pprint(x)
        delta = max(abs(x_in -x)) 
    return x

#狭義優対角行列を作る
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
    A = n_yutaikaku(n)
    b = np.random.rand(n)*10
    x0 = np.random.rand(n)*10
    
    start = time.time()
    sol = jacobi(A,b,alpha=0.0001,x=x0)
    pprint(sol)

    elapsed_time = time.time()-start
    print("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
main(10)

