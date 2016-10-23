# Enter your code here. Read input from STDIN. Print output to STDOUT
numerator, denominator = [int(x) for x in raw_input().split()]
fail = 1.0 * numerator/denominator
number = int(raw_input().strip())
success = 1 - fail 

# ** is power of operator
ans_1 = 1 - success ** number

print'{:0.3f}'.format(ans_1)