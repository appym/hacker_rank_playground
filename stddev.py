# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, math
N = int(sys.stdin.readline())
arr = map(int, sys.stdin.readline().split())
def mean(arr):
    # could also do - > reduce(lambda x, y: x + y, arr)/len(l)
    return sum(arr)/len(arr) 

def stddev(arr, mean):
    sqr = sum(math.pow(i - mean,2) for i in arr)
    return math.sqrt(sqr/n)

std_dev = stddev(arr, mean(arr))
print "%.1f" % std_dev