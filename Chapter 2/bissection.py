import numpy as np

#def bissection(n0, n):
#    n2 = n
#    n1 = (n0 + n2) / 2
#    
#    for i in range(100):
#        if (n0 ** 2 < n and n1 ** 2 > n):
#            n2 = n1
#            
#        else:
#            n0 = n1
#            
#        n1 = (n0 + n2) / 2
#        
#    return n1
#
#print(bissection(0, 2))

def f(x):
    return x ** 2 - 3 * x - 5

def df(x):
    return 2 * x - 3;
    
def bissection(a, b, TOL, nMax):
    for i in range(nMax):
        c = (a + b) / 2 #Novo ponto médio
        
        if (f(c) == 0 or (b  - a) / 2 < TOL):
            return c
        
        elif (np.sign(f(c)) == np.sign(f(a))):
            a = c
        
        else:
            b = c
            
            
def newton(x, nMax):
    for i in range(nMax):
        x = x - (f(x) / df(x))
        
    return x

def fixed_position(x0, x1, TOL, nMax):
    k0 = f(x0)
    k1 = f(x1)
    
    for i in range(2, nMax):
        x = x1 - k1 * (x1 - x0) / (k1 - k0)
    
        if (abs(x - x1) < TOL):
            return x
        
        k = f(x)
        
        if (k * k1 < 0):
            x0 = x1
            k0 = k1
        
        x1 = x
        k1 = k
    
    
def picard_peano(x0, nMax):
    x = x0
    
    for i in range(nMax):
        x = f(x)
    
#print(bissection(0, 5))
#print(newton(1, 10000000))
#print(false_position(-2, 0, 0.000001, 100))
print    

    