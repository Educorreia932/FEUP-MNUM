import math
import numpy

e = numpy.float64(math.exp(1))
#e = 2.7182

value = e - 1

for i in range(1, 26):
    value = value * i - 1
    
print(value)