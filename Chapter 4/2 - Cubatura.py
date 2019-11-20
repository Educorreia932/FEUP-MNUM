from math import sin

def f1(x, y):
    return 2

def f2(x, y):
    return x * y + sin(x)

def simpson1(points, h):
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

def simpson2(x0, y0, x1, y1, hx, hy):
    nx = int((x1 - x0) / hx)
    ny = int((y1 - y0) / hy)
    
    values = []
    row = []
  
    for i in range(ny):
        row.clear()
        
        for j in range(nx):
            row.append(f2(x0 + j * hx, y0 + i * hy))       
        
        values.append(simpson1(row, hx))
        
    return simpson1(values, hy)
    
print(simpson2(0, 0, 2, 2, 0.1, 0.1))
    
        
        
        
