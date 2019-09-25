from timeit import default_timer as timer

start = timer()

def squareroot(n):
    division = 1
    
    while (n > division ** 2):
        division += 1        
    
    result = n / division
    
    while ((result ** 2) / n <= 0.99999):
        result += 0.00001
        
    print(result)
    
squareroot(123456789987654321)

end = timer()

print(end - start)
