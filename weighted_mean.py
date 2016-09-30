# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N = int(sys.stdin.readline())
X = [0 for x in range(N)]
num = 0
den=0
line = map(int, sys.stdin.readline().split())
for i in range(len(line)):
    X[i]=line[i]
line = map(int, sys.stdin.readline().split())
for i in range(len(line)):
    num += X[i] * line[i]
    den += line[i]
mean = 1.0* num/den
print "%.1f" % mean