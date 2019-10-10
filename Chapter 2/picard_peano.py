from math import sqrt

def f(x):
    return 2 * x ** 2 - 5 * x - 3

def g1(x): #-0.5
    return (2 * x ** 2 - 3) / 5

def g2(x): #3
    return (5 * x + 3) / (2 * x)

def g3(x): #3
    return sqrt((5* x + 3) / 2)

def picard_peano(x0, nMax):
    x = x0
    
    for i in range(nMax):
        x = g2(x)
        print(x)
        
picard_peano(1, 20)