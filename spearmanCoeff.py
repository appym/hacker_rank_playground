# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(raw_input())
X = map(float, raw_input().split())
Y = map(int, raw_input().split())

def d_rank(iterable):
    output = [0] * n
    for item, index in enumerate(sorted(range(n), key=lambda y: iterable[y])):
        output[index] = item + 1
    return output

def pearsonCoefficient(rx, ry, n):
    runningSum = sum((a-b)**2 for a,b in zip(rx,ry))
    return 6.0*runningSum/(n*((n**2)-1))

rx = d_rank(X)
ry = d_rank(Y)
    
ans = pearsonCoefficient(rx, ry, n)
print'{:0.3f}'.format(1- ans)