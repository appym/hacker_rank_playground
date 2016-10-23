# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, math
res=0
line = map(float, sys.stdin.readline().split())
n = int(sys.stdin.readline())
def geometricDist(p,n):
    return math.pow(1-p,n-1) * p

p = 1.0*line[0]/line[1]
res = geometricDist(p,n)

print "%.3f" % res