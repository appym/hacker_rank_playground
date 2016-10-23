# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, math
combination=0
atmost=0
atleast=0
line = map(float, sys.stdin.readline().split())
F=line[0]
n=line[1]

def binomialDist(x,n,p):
    combination = (math.factorial(n) / (math.factorial(n-x) * math.factorial(x)))
    return math.pow(p,x) * math.pow(1-p, n-x) * combination

p = F/100
for i in range(2, 11):
    atleast += binomialDist(i, 10, p)
for i in range(0,3):
    atmost += binomialDist(i, 10, p)
print "%.3f" % atmost    
print "%.3f" % atleast