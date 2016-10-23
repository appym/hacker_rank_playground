# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
maxx = int(raw_input())
n = int(raw_input())
mean = float(raw_input())
stddev = float(raw_input())
meanp = n * mean
stddevp = math.sqrt(n) * stddev

def normalDist(x):
    z1 = (x - meanp) / (stddevp * math.sqrt(2))
    return 0.5 * (1 + math.erf(z1))

normalDist1 = normalDist(maxx)
print'{:0.4f}'.format(normalDist1)