def f(x):
    return x ** 2 - 3 * x - 5

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