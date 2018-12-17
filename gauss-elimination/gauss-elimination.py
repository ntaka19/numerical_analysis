def gauss(A,b):
    #x = [0 for i in range(n)]
    #A = [[0 for i in range (n)] for j in range(n)]
    n = len(b)
    #print n
    for i in range(0,n-1):
        for j in range(i+1,n):
            c = - float(A[j][i])/A[i][i]
             
            print c
            b[j] += c*b[i]
            print b
            for k in range(i,n):
                A[j][k] += c*A[i][k]
                print A
    
    x = [0 for i in range (n)]
    sigma = 0
    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            sigma += A[i][j] 
        x[i] =float(b[i]-sigma)/A[i][i]
        sigma = 0
        for j in range(n-1,-1,-1):
            A[j][i] *= x[i]
    print x    

"""
A = [[1,2,1],[2,3,4],[3,2,1]] 
b = [2,3,4]
"""
"""
A = [[1,2,1,1],[2,3,4,1],[3,2,1,1],[1,2,3,4]] 
b = [1,2,3,4]
"""

A = [[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,2]] 
b = [1,2,3,4]
gauss(A,b)
