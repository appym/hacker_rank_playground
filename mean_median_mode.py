# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N = int(sys.stdin.readline())
arr = [0 for x in range(N)]
modes = dict()
tot=0
def median(aray):
    srtd = sorted(aray)
    alen = len(srtd)
    return 0.5*( srtd[(alen-1)//2] + srtd[alen//2])

def mode(modes):
    max_count = max(modes.values())
    mode_val = [k for k,v in modes.items() if v == max_count]
    return mode_val
    
line = map(int, sys.stdin.readline().split())
for i in range(len(line)):
    tot += line[i]
    arr[i] = line[i]
    if line[i] in modes:
        modes[line[i]] += 1
    else:
        modes[line[i]] = 1  
mean_val = 1.0*tot/N
median_val = median(arr)
mode_val = mode(modes)

print "%.1f" % mean_val
print "%.1f" % median_val
print min(mode_val)