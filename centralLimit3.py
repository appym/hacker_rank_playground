# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(raw_input())
mean = float(raw_input())
stddev = float(raw_input())
p = float(raw_input())
z = float(raw_input())
meanp = n * mean
stddevp = math.sqrt(n) * stddev

A = (meanp - z * stddevp) / n
B = (z * stddevp + meanp) / n
print'{:0.2f}'.format(A)
print'{:0.2f}'.format(B)