def f(x, y):
    return x ** 2 + y ** 2

def dfx(x, y):
    return 2 * x

def dfy(x, y):
    return 2 * y

def gradient(x0, y0, n, h):    
    for _  in range(1, n):
        x = x0 - h * dfx(x0, y0)
        y = y0 - h * dfy(x0, y0)
        
        if (f(x, y) >= f(x0, y0)):
            h /= 2
            
        else:
            x0 = x
            y0 = y
            h *= 2
            
    return (x, y)

print(gradient(2, 2, 1500, 0.1))
