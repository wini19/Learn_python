#program4
#1/08/18

#PYTHON STRINGS

# represented in 'single quotes' or in 'double quotes'
#no char datatype in PYTHON, char represented as string containing one element : 'c' or "c"

x="hello"
y='world'
print(x[0]+y[1]+'t'+'T') #prints : hotT


# print(arr[A:B]) is same as :
""" for(i=A;i<B;i++)
      print(arr(i)) """
# where arr is a string variable
print(y[1:5]) #prints orld
print(x[0:4]) #prints hell


# The strip() method removes any whitespace from the beginning or the end:
print("STRIP FUNCTION :")
x="     I got it     "
y=" okay "
x.strip() #doesnt changes x, it just returns stripped x
print(y.strip())
print(x+'!') #initial x printed
print(x.strip()+'!') #stripped x printed
# print(strip(x)) :---gives error


# other functions :
print("**\n"+"OTHER IMP FUNCTIONS"+'\t:')
x="123def"
y='abc'
print(len(x)) #returns lenth of string
# print(y.len()) :----error
print(len(x) + len(y)) #prints 9
print(x.upper())
print(x.lower())
y="ALL FOR ONE"
print(y.lower())
print(y) #prints "ALL FOR ONE" bcz y doesnt change by calling y.lower()
print(y.upper())
# print(upper(y)) :-----error
print(x.replace('123',"abc"))
print(x)
print(y.replace("L","A"))
print(y.split(" "))#prints : ['ALL', 'FOR', 'ONE']
x='thats#juz the#way Iam'
print(x.split("#"))


# command line string-input using input() method
print('\n' + "Type your name : ")
x=input()
print("hello " + x + " :)")
