# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
lamA, lamB = [float(x) for x in raw_input().split()]
# C = 160 + 40 * X^2 
# E[C] = 160 + 40 * E[X^2]
# E[C] = 160 + 40 ( Var(X) + (E[X])^2)
ansA = 160 + 40 * (lamA + lamA ** 2)
ansB = 128 + 40 * (lamB + lamB ** 2)
print '{:0.3f}'.format(ansA)
print '{:0.3f}'.format(ansB)