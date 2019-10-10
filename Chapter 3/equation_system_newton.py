from math import log10
from sympy import symbols, diff
from numpy.linalg import det

f1 = "2 * x ** 2 - x * y - 5 * x + 1"
f2 = "x + 3 * log10(x) - y ** 2"

def f(expression, x, y):
    print(expression)
    return eval(expression)

def dfx(expression, x0):
    expression = str(diff(expression, x))
    
    return f(expression, x0, 0)
    
def dfy(expression, y0):
    expression = str(diff(expression, y))
    
    return f(expression, 0, y0)

x, y = symbols('x y', real = True)

#diff(f1, x)

def newton(x0, y0, nMax):        
    for i in range(nMax):
        J = [[dfx(f1, x0), dfy(f1, y0)], [dfx(f2, x0), dfy(f2, y0)]]
        J1 = [[f(f1, x0, y0), dfy(f1, y0)], [f(f2, x0, y0), dfy(f2, y0)]]
        
        h = - det(J1) / det(J)    
        k = - det(J1[::-1]) / det(J)
        
        x0 += h
        y0 += k
    
    return x, y

print(newton(1, 5, 20))
