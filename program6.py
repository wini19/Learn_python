#LISTS : List is a collection which is ordered and changeable. Allows duplicate members.
#REFER https://www.w3schools.com/python/python_lists.asp FOR MORE LIST METHODS

x=["hsm","thegreatestshowman","lalaland"]
print(x)
x[2]="hairspray"
print(x[2])

# list constructor to make List
x=list(("fabulous","breaking free",3))
print(x)

#remove and append functions
#append() and remove() takes exactly one argument
x=["Zac Efron","Anna Kendrick",30,5.8,32,5.2,"Zanna"]
print(x)
print("appending...")
x.append("haha")
x.append("haha")
print("seeee...duplicate members allowed : ",x)
x.remove('haha')
print(x)
x.remove(5.8)
print(x)
x.remove('haha')
print(x)
x.remove(5.2)
print(x)


#length of list : len()
print(len(x))
x.append("my")
x.append("favourite")
print(len(x),x) #IMP OBSERVATION : multiple things can be printed using one print()
#comma seperated arguments are printed on screen separated by a space

#Toodles! :)
