#---------------------PYTHON OPERATORS---------------------------
"""Types of operators in python :
   Arithmetic operators (c++ and some extra)
   Assignment operators(c++ and some extra)
   Comparison operators(same as c++)
   Logical operators(same as c++,syntax different)
   Identity operators (new)
   Membership operators
   Bitwise operators """

# Arithmetic OPERATORS
x=5
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y) #returns 2.5
print(x%y) #returns Remainder
print(x//y) #floor division : returns Quotient
print(x**y) #x^y

# Comparison operators
print(x==y) #prints 'false'
print(x>y) #prints 'true'
print(x>=y)
print(x<y)
print(x<=y)
print(x!=y)
# print(x=y) :-----gives ERROR
# print(x=20) :-----gives ERROR

# Logical operators
print(x==y or x>y)
print((x!=y) and (x<y))
print(not(x<=y))
print(not x) #prints 'false'
x=0
print(not x) #prints 'true'
x=-100
print(not x) #prints 'false'
#WEIRD RESULTS :::
print(x and y) #prints 2
print(x or y) #prints -100
x=100
print(y or x) #prints 2
print(x or y) #prints 100
print(y and x) #prints 100
# my point : in such cases, 'or' prints first written variable and 'and' prints 2nd variable

# Identity operators
# used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
# mypoint : consider python variables/object_name as c++'s pointers
x = ["apple", "banana"] #x is a list (refer next program)
y = ["apple", "banana"] #y is a list (refer next program)
z = x  #consider it to be analogous to copying address stored by pointer x to pointer z in c++
print('\n\nIDENTITY OPERATORS : \n')
print(x is z) # prints True because z is the same object as x
print(x is y)# prints False because x is not the same object as y, even if they have the same content
print(x is not y) #prints True
print(x is not z)#prints False
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Membership operators
print('\n\nMEMBERSHIP OPERATORS : \n')
x = ["apple", "banana"]
print("banana" in x)#prints True because a sequence with the value "banana" is in the list
y="apple"
print(y not in x) #prints False
y="chiku"
print(y not in x) #prints True
print("hi" in ["hi","bye"])
print("hi" in "hill") #also checks membership of a substring in a substring
print("dil" not in "hill") #prints True

#Bitwise operators
print('\n\nBITWISE OPERATORS : \n')
x=0b1010
y=0b0001
print(x&y)
print(x|y)
print(x^y) #XOR
print(~x) #invert all bits, prints -11
print(x<<3) #prints 80#Zero fill left shift : Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(x>>3) #prints 1 #Signed right shift : Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
#TO DO LIST : ANALYSE BELOW RESULTS LATER :-
x=12
y=-3
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x<<3)
print(y>>1)

# Assignment operators
#SAME AS C++
"""
Operator    Example	          Same As
    =	      x = 5	          x = 5
    +=	     x += 3	          x = x + 3
    -=	     x -= 3	          x = x - 3
    *=	     x *= 3	          x = x * 3
    /=	     x /= 3	          x = x / 3
    %=	     x %= 3	          x = x % 3
    //=	    x //= 3	          x = x // 3
    **=	    x **= 3	          x = x ** 3
    &=	     x &= 3	          x = x & 3
    |=	     x |= 3	          x = x | 3
    ^=	     x ^= 3	          x = x ^ 3
    >>=	    x >>= 3	          x = x >> 3
    <<=	    x <<= 3	          x = x << 3
"""
