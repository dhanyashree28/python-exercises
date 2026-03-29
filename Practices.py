# for loop to print 1 to 5

for i in range (1,6):
    print(i)
    
a=int(input("enter a number:"))
for i in range(1,a):
    print(i)

for i in range(2,9,2):
    print(i)

i = 2  #mannual counter
while i <= 10: #condition
    print(i) # values
    i += 2 #increment

a=20
for i in range(2,a,2):
    print(i)

a=int(input("Enter the number:"))
for i in range(5,a,5):
    print("this is the multiplication of table five:",i)

# nested loop
for i in range(1,4):
  for j in range(1,4):
     print("\n",i)
     print("\n",j)

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
for i in range(25,a,25):
  for j in range(25,b,25):
     print(i,j)

# Add two numbers using input

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
sum = a+b
print("Sum",sum)

# Area of circle using radius
    
radius = int(input("Enter the radius:"))
pi = 3.14
print(pi*radius**2)

# Area of rectangle

length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
area_of_rectangle = length*width
print("Area of Reactangle:",area_of_rectangle)

# Square and cube of number

a = int(input("Enter the number:"))
sq = a**2
cube = a**3
print("square",sq,"cube",cube)

# Take 2 numbers print product and division

a = 10
b = 20
p = a*b
d = a/b
print("Product=",p,"Division=",d)

# Take price and quantity calculate total cost

p = int(input("Enter the price:"))
q = int(input("Enter the quantity:"))
cost = p*q
print("Total cost:",cost)

# Take marks calculate percentage

s1 = int(input("Enter the marks:"))
s2 = int(input("Enter the marks:"))
per = s1+s2/2*100
print("Percentage of marks:",per)

# convert temperature

celsius = int(input("Enter the celsius:"))
f = celsius*9/5+32
print("Celsius to Faherneit:",f)

#PATTERN PRINTTING

n = 3
for i in range(1,n+1):
  for j in range(i): 
     print('*', end =' ')
  print()

n = 3
for i in range(n, 0, -1):
  for j in range(i): 
     print(' ','*', end = ' ')
  print()

n = 4
for i in range(1,n+1):
  print(' '*(n-i) + ' * '*i)