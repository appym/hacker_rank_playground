# Enter your code here. Read input from STDIN. Print output to STDOUT
# SOMETHING WRONG WITH THE ERF FUNCTION I WROTE. SO USING math.erf
import math
mean, stddev = [int(x) for x in raw_input().split()]

def normalDist(x):
    z1 = (x - mean) / (stddev * math.sqrt(2))
    return 0.5 * (1 + math.erf(z1))

normalDist1 = 1 - normalDist(80)
normalDist2 = normalDist(60)
print'{:0.2f}'.format(100*normalDist1)
print'{:0.2f}'.format(100*(1 - normalDist2))
print'{:0.2f}'.format(100*normalDist2)