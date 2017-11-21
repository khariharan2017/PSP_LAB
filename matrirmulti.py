def matrixmulti(X, y):
    
    M = len(X)
    N = len(X[0])
    P = len(y[0])
    
    Z = [[0] * P  for row in range(M)]
    
    if  N != len(y):  
        print ("Incorrect dimensions.")
        return

    for i in range(M):
        for j in range(P):
            for k in range(N):
                Z[i][j] += X[i][k] * y[k][j]

    return Z
X = [[1, 1], [1, 1]]
y = [[1, 2, 1], [1, 2, 1]]
print(matrixmulti(X, y))
