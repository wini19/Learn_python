#python tuples
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
t=("is","it","desire") #a tuple
print(t) 
print(t[1])

#IMP POINTS :
 """1. You cannot remove items in a tuple.
    2.You cannot change values in a tuple"""
    
t.append("or")
t[0]="was" #not allowed
print(t)

#tuple() constructor
t=tuple(("the","way","i","am"))
print(t)

#len() function
print(len(t))
