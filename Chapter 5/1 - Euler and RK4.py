import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return x ** 2

def euler(x0, y0, x1, h):   
    x_points = []
    y_points = []
    
    x = x0
    y = y0
    
    n = (int) ((x1 - x0) / h)
    
    for _ in range(n):
        y += f(x, y) * h
        x += h        
        
        x_points.append(x)
        y_points.append(y)
    
    return (x_points, y_points)

def rk4(x0, y0, x1, h):
    x_points = []
    y_points = []
    
    x = x0
    y = y0
    
    n = (int) ((x1 - x0) / h)
    
    for _ in range(n):
        d1 = h * f(x, y)
        d2 = h * f(x + h / 2, y + d1 / 2)
        d3 = h * f(x + h / 2, y + d2 / 2)
        d4 = h * f(x + h, y + d3)
        
        y += d1 / 6 + d2 / 3 +  d3 / 3 + d4 / 6 
        x += h        
        
        x_points.append(x)
        y_points.append(y)
    
    return (x_points, y_points)

# Plotting

points_1 = euler(-25, -15622/3, 25, 2)
points_2 = rk4(-25, -15622/3, 25, 2)

## Setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

x = np.linspace(-25, 25, 100)
y = x ** 3 / 3 + 1

plt.axis(True)
plt.plot(x, y, 'r')
plt.plot(points_1[0], points_1[1]) 
plt.plot(points_2[0], points_2[1]) 
plt.legend(("Correct", "Euler", "Runga-Kutta's 4th Order"))

plt.show()