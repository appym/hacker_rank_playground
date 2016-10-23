# SOMETHING WRONG WITH THE ERF FUNCTION I WROTE. SO USING math.erf
import math
mean, stddev = [int(x) for x in raw_input().split()]
var = stddev ** 2

def f(x):
    return math.exp(-1 * x**2)
    
def integral(start, end, numRect):
    width = end - start / numRect
    runningSum = 0
    for i in range(numRect):
        height = f(start + i*width)
        area = height * width
        runningSum += area
    return runningSum

def erf(z):
    return (2/math.pi) * integral(0, z, 1000000)

def normalDist(x):
    z1 = (x - mean) / (stddev * math.sqrt(2))
    return 0.5 * (1 + math.erf(z1))

normalDist1 = normalDist(19.5)
normalDist2 = normalDist(22) - normalDist(20)
print'{:0.3f}'.format(normalDist1)
print'{:0.3f}'.format(normalDist2)