"""# syntax : lambda arg1,arg2,arg3,...........argn  : operation

#without lambda function
def add(a,b):
    return f"the sum of {a} and {b} is {a+b}"
print(add(10,20))



#with lambda function

add = lambda a,b: f"the sum of {a} and {b} is {a+b} "
print(add(10,20))

print((lambda a,b : f"the sum of {a} and {b} is {a+b} "     


square = lambda a :f" the square of {a} is {a**2} "
print(square(10))


cube = lambda a: f"the cube of {a} is {a**3}"
print(cube(3))   



#list comprahension with lambda function

positive = lambda a,b: [   i        for i in range(a,b+1)]
print(positive(10,20))   


div_2 = lambda a,b : [   (i,"even" )    for i  in range(a,b+1)     if i%2 == 0 ]
print(div_2(int(input("first number:")) , int(input("second number:"))))    


even_odd = lambda a,b : [  (i,"even")              if i%2 == 0  else  (i,"odd")        for i in range(a,b+1)]
print(even_odd(1,20))   """


fizz_buzz = lambda a,b : [       (i,"fizzbuzz")    if i%5 ==0  else (i,"fizz")   if i%3 == 0  else   (i,"buzz")      if i%5==0  else  (i,"miss")        for i in range(a,b+1)]
print(fizz_buzz(10,51))

                         




