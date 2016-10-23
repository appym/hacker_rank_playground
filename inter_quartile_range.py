# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N = int(sys.stdin.readline())
tot=0
def median(aray):
    alen = len(aray)
    return int(0.5*( aray[(alen-1)//2] + aray[alen//2]))

line = map(int, sys.stdin.readline().split())
freq = map(int, sys.stdin.readline().split())
A = [a for a,b in zip(line,freq) for x in range(1,b+1)]

srtd = sorted(A)
if (len(A) % 2 == 0):
    B = srtd[:len(srtd)/2]
    C = srtd[len(srtd)/2:]
else:
    B = srtd[:len(srtd)/2]
    C = srtd[(len(srtd)/2)+1:]

Q1 = median(B)
Q3 = median(C)
diff = Q3 - Q1
print "%.1f" % diff