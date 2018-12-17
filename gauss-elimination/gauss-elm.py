def gauss(A): 

    for i in range(0,n):
        maxEl = abs(A[i][i])
        maxRow = i
        #search for maximum in this column
        for k in range(i+1,n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        #swap maximum row with the current row 
        for k in range(i,n+1): 
            tmp = A[maxRow][k] 
            tmp = A[maxRow][k] = A[i][k]
            A[i][k] = tmp 
        
        #make all rows below this one 0 in current column 
        for k in range(i+1,n): 
            c = -A[k][i]/A[i][i]
            for j in range(i,n+1): 
                if i == j: 
                    A[k][j] = 0 
                else: 
                    A[k][j] += c * A[i][j]

        #solve equation Ax = b for upper trangular matrix A 
        x = [0 for i in range(n)]
        for i in range(n-1,-1,-1):
            x[i] = A[i][n]/A[i][i]
            for k in range(i-1,-1,-1):
                A[k][n] -= A[k][i] * x[i]
        return x 

A = [[0 for i in range(4)]for j in range (4)]

        
