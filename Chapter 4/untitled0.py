#def swap(A, i1, i2):
#    A[i2], A[i1] = A[i1], A[i2]
#    
#    
#def gauss_elimination(A):
#    h = 1
#    k = 1
#    
#    while h <= m and k <= n :
#        i_max = 
#        
#        if A[i_max, k] == 0: # No pivot in this column, pass to next column
#            k += 1 
#            
#        else:
#            swap(A, h, i_max)
#            
#            for 
     
from numpy.linalg import norm    
            
def gauss_seidel(A, b, TOL):
    X = []
    x = []
    
    for k in range(len(b)):
        X.append(0)
        
    m = 1000
    ni = 0
    
    while (ni < m):
        for i in range(len(b)):
            soma = 0
            
            for j in range(i):
                soma += A[i][j] * x[j]
                
            for j in range(i + 1, len(b)):
                soma += A[i][j] * X[j]
                
            x.append((b[i] - soma) / A[i][i])
                
        if (abs(norm(x) - norm(X)) < TOL):
            break
            
        X = x
            
        ni += 1
        
    return x

matrix = [[9, 1, 5] , [1, 4, 6], [2, 9, 7]]
result = [25, 16, 29]

print(gauss_seidel(matrix, result, 0.00001))
    
    