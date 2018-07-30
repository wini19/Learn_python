# explains about type castings in python

#type castings

#float,int,string -> int
x=int(-4)
print(x)
x=int(-4.9982)
print(x)
x=int("4008") #string shpuld consist of a whole no. only
print(x)

# invalid :
# x=int("-4.2")
# print(x)
# x=int("g23")
# print(x)

#float,int,string -> float
x=float(-4)
print(x)
x=float(100.04)
print(x)
x=float("71.772")
print(x)
x=float("-71.772")
print(x)
x=float("0.007e2")
print(x)

#many datatypes including float,int,string -> string
x=str(-4)
print(x)
x=str(23)
print(x)
x=str(-4.007)
print(x)
x=str("hahaha" + "hohoho")
print(x)


# invalid :
# x=str("hahaha" + "hohoho" + 10) :-----int can't be concatenated with str
# print(x)
