print('hello world')

a=30
b=60
print(a+b)

length = int(input("enter the lenght of a rectangle:")) 
bredth = int(input("enter the bredth of a rectangle:"))  # area of rectangle
area = length * bredth
print ("area of rectangle is " ,area)
perimeter = (2*length) * (2*bredth)
print ("perimeter of rectangle is" , perimeter)  # perimeter of rectangle

a = 10
b = 20   # swap two numbers using third variable
temp = a
a=b  
b=temp
print(a)
print(b)

a = 30
b = 40
a,b = b,a    #swap two numbers without using third variable
print(a) 
print(b)

a = 38
print(a**2)
print(a**3)  # find the square root of a number

p = 22000
t = 5
r = 15
interest = (p*t*r)/100
print(interest)       #  find the simple interest

x = 24
y = 65
z = 99
a = (x+y+z)/3            # find the average of three numbers
print(f"average of {x},{y} and {z} is {a}")   

a = 110
b = 20
print( "partial quotient " , a//b)    # find the partial quotient anf remainder
print( "remainder is ", a%b)

r = 20
area = 3.14 * (r**2)  
print(area)
perimeter = 2*3.14*r
print(perimeter)          # find the area, perimeter of a circle and area of a semi circle
area_semi_circle = area/2
print(area_semi_circle)

radius = 15
diameter = 2*radius
print(diameter)     # find the diameter of a circle

















