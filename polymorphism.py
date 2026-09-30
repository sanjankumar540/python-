"""

class A:
    def arithematic(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return f"the addition of {self.a} ,{self.b},{self.c} is {self.a+self.b+self.c} "
obj = A()
print(obj.arithematic(10,20,30)) 

# method overloading
class A:
    def arithematic(self,a,b=10,c=30):
        self.a = a
        self.b = b
        self.c = c
        return f"the addition of {self.a} ,{self.b},{self.c} is {self.a+self.b+self.c} "
obj = A()
print(obj.arithematic(1,2,3))
print(obj.arithematic(5))
print(obj.arithematic(3,b=5))
print(obj.arithematic(9,c=2))

# method overrriding
class m:
    def sample(self):
        print("iam in sql class")
class n(m):
    def sample(self):
        print("iam in python class")
obj = n()
obj.sample()  

class m:
    def sample(self,a):
        self.a=a
class n(m):
    def sample(self,b):
        self.b=b
obj = n()
obj.sample(10)
print(obj.__dict__)  

class Student:
    name = "pranav"
    roll_no = 40
    gender = "male"
    def __str__(self):
        return self.name
obj = Student()
print(obj)   

# dunder methods or magic methods

class A:
    def __init__(self,a):
        self.value = a
    def __add__(self,other):
        return f" {self.value} + {other.value} = {self.value +other.value} "
    
    def __sub__(self,other):
        return f" {self.value} - {other.value} = {self.value - other.value} "

    def __mul__(self,other):
        return f" {self.value} * {other.value} = {self.value * other.value} "

    def __truediv__(self,other):
        return f" {self.value} / {other.value} = {self.value / other.value} "

    def __floordiv__(self,other):
        return f" {self.value} // {other.value} = {self.value // other.value} "

    def __mod__(self,other):
        return f" {self.value} % {other.value} = {self.value % other.value} "

    def __gt__(self,other):
        return f" {self.value} > {other.value} = {self.value > other.value} "

    def __lt__(self,other):
        return f" {self.value} < {other.value} = {self.value < other.value} "

    def __eq__(self,other):
        return f" {self.value} == {other.value} = {self.value == other.value} "
obj = A(100)
obj1 = A(10)
print(obj+obj1)
print(obj-obj1)
print(obj*obj1)
print(obj/obj1)
print(obj//obj1)
print(obj%obj1)
print(obj>obj1)
print(obj<obj1)
print(obj==obj1)   


class A:
    def __init__(self):
        self.a=10
class B:
    def __init__(self):
        self.b=11

obj = A()
obj = B()
print(obj.__dict__)  """


class plane :
    def fly(self):
        print("plane flies")
class crow: 
    def fly(self):
        print("crow flies")

def start_flying(obj):
    obj.fly()
start_flying(plane())
start_flying(crow())
        

