from math import sqrt, sin

Φ = (sqrt(5) - 1) / 2

def f(x):
    return sin(x) ** 2
    
def golden_ratio(a, b, TOL):
    c = b - Φ * (b - a)
    d = a + Φ * (b - a)
    fc = f(c)
    fd = f(d)
    
    while(abs(b - a) > TOL):
        if (fc > fd):
            a = c
            c = d
            fc = fd
            d = a + Φ * (b - a)
            fd = f(d)
            
        else:
            b = d
            d = c
            fd = fc
            c = b - Φ * (b - a)
            fc = f(c)
            
    return a

print(golden_ratio(2, 4, 0.001))        
