import numpy as np
    
def f(x):
    return x ** 2 - 3 * x - 5

def bissection(a, b, TOL, nMax):
    for i in range(nMax):
        c = (a + b) / 2 #Novo ponto médio
        
        if (f(c) == 0 or (b  - a) / 2 < TOL):
            return c
        
        elif (np.sign(f(c)) == np.sign(f(a))):
            a = c
        
        else:
            b = c            
    