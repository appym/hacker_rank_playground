import math
n=5
X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

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

b1 = pearsonCoefficient()
b = b1 * stddevY/stddevX
a = meanY - b * meanX

ans = a + b * 80
print'{:0.3f}'.format(ans)