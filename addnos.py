# adding two nos
#https://www.codechef.com/problems/FLOW001
t=int(input())
while t>0:
    n,k=input().split() #for inputing space seperated int nos. 
    # n,k = map(int,input().split()) :---"""this can be also used"""
    print(int(n)+int(k))
    t=t-1
