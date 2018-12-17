import numpy as np
from numpy import diag,zeros,max,sum

def n_yutaikaku(n):
    #A = np.empty((0,n),float)
    A = []
    for i in range(n):
        a = np.random.rand(n)*10
        c = sum(a) 
        print(c)
        
        a[i]=np.random.rand()*10+c-a[i]
        print(a)
        elm = [a]
        A.append(a)
        #A = np.append(A,elm,axis =0) 
    print(A)
    return A
n_yutaikaku(2)

