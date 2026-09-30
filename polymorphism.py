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
print(obj.__dict__)   """

class Student:
    name = "pranav"
    roll_no = 40
    gender = "male"
    def __str__(self):
        return self.name
obj = Student()
print(obj)

