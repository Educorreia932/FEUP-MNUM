def f(x):
    return x ** 2 - 3 * x - 5

def df(x):
    return 2 * x - 3;

def newton(x, nMax):
    for i in range(nMax):
        x = x - (f(x) / df(x))
        
    return x