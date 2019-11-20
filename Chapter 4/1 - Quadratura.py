def f(x):
    return x**2

def trapeze(x0, x1, h):
    y_sum = 0
    
    y0 = f(x0)
    yn = f(x1)
    
    while (x0 < x1):
        y_sum += f(x0)
        
        x0 += h
        
    return h / 2 * (y0 + yn + 2 * y_sum)    

def simpson(x0, x1, h):
    n = int((x1 - x0) / h)

    odd_terms = 0
    even_terms = 0    
    
    values = []
    
    for i in range(n):
        values.append(f(x0 + i * h))
    
    for i in range(1, n, 2):
        odd_terms += values[i]
        
    for i in range(2, n, 2):
        even_terms += values[i]
    
    return h / 3 * (values[0] + values[n - 1] + 4 * odd_terms + 2 * even_terms)

#print(trapeze(0, 4, 0.1))
print(simpson(0, 4, 0.1))
    