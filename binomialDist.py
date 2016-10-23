# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, math
combination=0
res=0
line = map(float, sys.stdin.readline().split())
B=line[0]
G=line[1]

def binomialDist(x,n,p):
    combination = (math.factorial(n) / (math.factorial(n-x) * math.factorial(x)))
    return math.pow(p,x) * math.pow(1-p, n-x) * combination

p = 1.0 * B/(B+G)
for i in range(3, 7):
    res += binomialDist(i, 6, p)
print "%.3f" % res