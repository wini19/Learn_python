x=int(input("please enter a whole number : "))
fact=1
while x>0 :
    fact = fact * x
    # x-- :-----invalid in python
    x=x-1
print("factorial is : ",fact)
