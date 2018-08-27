#importing math module and using some of its functions
# https://www.codechef.com/problems/FSQRT
import math
t=int(input()) #no. of test cases
while t>0 :
    x=int(input())
    print(math.floor(math.sqrt(x)))
    t=t-1
