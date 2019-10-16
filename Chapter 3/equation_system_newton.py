from math import log10, log

def f1(x, y):
    return 2 * x ** 2 - x * y - 5 * x + 1

def f2(x, y):
    return x + 3 * log10(x) - y ** 2

def detJ(x, y):
    return (3 / (log(10) * x) + 1) * x - 2 * (-y + 4 * x - 5) * y
    
def detM1(x, y):
    return x * (-y ** 2 + 3 * log10(x) + x) - 2 * y * (-x * y + 2 * x ** 2 - 5 * x + 1)    

def detM2(x, y):
    return (-y + 4 * x - 5) * (-y ** 2 + 3 * log10(x) + x) - (3 / (log(10) * x) +1) * (-x * y + 2 * x ** 2 - 5 * x +1)

#Do h/k in Maxima (?)

def newton(x0, y0, nMax):  
    x = x0
    y = y0
    first = True
    
    while((x != x0 and y != y0) or first == True):
        x0 = x
        y0 = y
        
        h = detM1(x0, y0) / detJ(x0, y0)
        k = detM2(x0, y0) / detJ(x0, y0)
        
        x -= h
        y -= k
        
        first = False

    return x, y

print(newton(4, 2, 100))