"""# syntax : lambda arg1,arg2,arg3,...........argn  : operation

#without lambda function
def add(a,b):
    return f"the sum of {a} and {b} is {a+b}"
print(add(10,20))



#with lambda function

add = lambda a,b: f"the sum of {a} and {b} is {a+b} "
print(add(10,20))

print((lambda a,b : f"the sum of {a} and {b} is {a+b} "     """


square = lambda a :f" the square of {a} is {a**2} "
print(square(10))


cube = lambda a: f"the cube of {a} is {a**3}"
print(cube(3))
