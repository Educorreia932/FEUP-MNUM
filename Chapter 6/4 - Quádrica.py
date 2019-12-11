def f(x, y, n):
    return x ** 2 + y ** 2

def hfx(x, y):
    return 2

def hfy(x, y):
    return 2

def quadric(x0, y0, n):
    for _ in range(n):
        x = x0
        y = y0
        
        x = x - hfx(x, y)
        y = y - hfy(x0, y)
        
    return (x, y)

print(quadric(2, 2, 2000))