# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
lam = float(raw_input())
k = int(raw_input())
def poissonDist(k, lam):
    return ((lam ** k) * math.exp(-lam))/math.factorial(k)

ans = poissonDist(k, lam)
print'{:0.3f}'.format(ans)