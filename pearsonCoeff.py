# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(raw_input())
def convert(x):
    if float(x).is_integer():
        return int(x)
    else:
        return float(x)
    
X = [convert(x) for x in raw_input().split()]
Y = map(int, raw_input().split())

def mean(arr):
    # could also do - > reduce(lambda x, y: x + y, arr)/len(l)
    return sum(arr)/len(arr) 

def stddev(arr, mean):
    sqr = sum(math.pow(i - mean,2) for i in arr)
    return math.sqrt(sqr/n)

def pearsonCoefficient():
    runningSum = sum((a-meanX)*(b-meanY) for a,b in zip(X,Y))
    return runningSum/(n*stddevX*stddevY)

meanX = mean(X)
meanY = mean(Y)
stddevX = stddev(X, meanX)
stddevY = stddev(Y, meanY)
pc = pearsonCoefficient()
print'{:0.3f}'.format(pc)