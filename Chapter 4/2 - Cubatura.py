from math import sin

def f1(x, y):
    return 2

def f2(x, y):
    return x * y + sin(x)

def trapeze(points, h):     
    return h / 2 * (points[0] + points[-1] + 2 * sum(points))  

def simpson(points, h):
    n = len(points)
    odd_terms = 0
    even_terms = 0 
    
    for i in range(1, n, 2):
        odd_terms += points[i]
        
    for i in range(2, n, 2):
        even_terms += points[i]
    
    odd_terms *= 4
    even_terms *= 2
    integral = odd_terms + even_terms + points[0] + points[-1]
    
    integral *= h / 3
    
    return integral

def cubatura(x0, y0, x1, y1, hx, hy, method):
    nx = int((x1 - x0) / hx)
    ny = int((y1 - y0) / hy)
    
    values = []
    row = []
  
    for i in range(ny):
        row.clear()
        
        for j in range(nx):
            row.append(f2(x0 + j * hx, y0 + i * hy))       
        
        if method == "trapeze":
            values.append(trapeze(row, hx))
        
        elif method == "simpson":
            values.append(simpson(row, hx))
        
    return simpson(values, hy)
    
print(cubatura(0, 0, 2, 2, 0.1, 0.1, "trapeze"))
print(cubatura(0, 0, 2, 2, 0.1, 0.1, "simpson"))
    