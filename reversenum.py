# program to reverse an integer and also tell whether its a pallindrome
x=int(input("enter a whole number : "))
y=x
rev=0
while x>0 :
    rev = rev*10 + x%10
    x//=10 #using floor division to get quotient. x=x//10. "x=x/10" :-could be used for this program in c/c++ but not in python.
print("reverse of ",y," is ",rev)
if y==rev :
    print("a pallindrome!")
else :
    print("not a pallindrome!")

#OBSERVATIONS :
"""very first time I wrote "x=x/10" and not "x=x//10" bcz of habit.
It gave no error but it gave undesired output. Value of 'rev' was resulting to 'inf'
which means 'infinity' in python. """
