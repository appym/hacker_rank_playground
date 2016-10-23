# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N = int(sys.stdin.readline())

def median(aray):
    alen = len(aray)
    return int(0.5*( aray[(alen-1)//2] + aray[alen//2]))

line = map(int, sys.stdin.readline().split())
srtd = sorted(line)
if (N % 2 == 0):
    B = srtd[:len(srtd)/2]
    C = srtd[len(srtd)/2:]
else:
    B = srtd[:len(srtd)/2]
    C = srtd[(len(srtd)/2)+1:]

Q1 = median(B)
Q2 = median(srtd)
Q3 = median(C)

print Q1
print Q2
print Q3