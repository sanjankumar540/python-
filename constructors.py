# default constructors
"""
class A:
    pass

obj = A()
obj.a =10
obj.b=20
print(obj.__dict__)    

# USER DEFINED CONSTRUCTORS
# 1.parameterized

class A:
    def sample(self):
        self.a = 10
        self.b=20

obj = A()
obj.sample
print(obj.__dict__)   

class A:
    def __init__(self):
        self.a = 10
        self.b=20

obj = A()    
print(obj.__dict__)


class sanjan:
    def pranav(self,emp1,emp2,emp3):
        self.a=emp1
        self.b=emp2
        self.c=emp3
obj=sanjan()
obj.pranav(10,20,30)
print(obj.__dict__)   

class sanjan:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
chethan = sanjan(10,20,30)
print(chethan.__dict__)  

#  combining both static method to validate and user defined constructor
class Student:
    def __init__(self,details):
        self.details = details
        return self.validate(self.details)
        
    @staticmethod
    def validate(a):
        if a[1] >=18:
            print(f"{a[0]} is adult")
        else:
            print(f"{a[0]} is minor")
        if 35<=a[2]<=50:
            print(f"{a[0]} achieved just pass")
        elif 50<=a[2]<=65:
            print(f"{a[0]} achieved first class")
        elif 65<=a[2]<=85:
            print(f"{a[0]} achieved second class")
        elif 85<=a[2]<=100:
            print(f"{a[0]} achieved distinction")
        else:
            print(f"omg {a[0]} ,,, you failed")
        
    
obj = Student(["ram",15,83])
print(obj.__dict__)
print("-" *35)
obj1 = Student(["raj",21,92])
print(obj1.__dict__)
print("-" *35)
obj2 = Student(["lakshman",35,67])
print(obj2.__dict__)
print("-" *35)   

# combining both static method to validate and user defined constructor
class Student:
    total = 0

    def __init__(self,stud):
        self.std = stud
        Student.total +=1
        return self.validate(self.std)

    @staticmethod
    def validate(a):
        if len(a[0]) >3:
            print("valid name")
        else:
            print("invalid name")
        if 18<=a[1]<=25:
            print("you are adult")
        else:
            print("you are not adult")
        if a[3].endswith("@gmail.com"):
            print("valid email")
        else:
            print("invalid email")

obj=Student(["sanjan",21,101,"sanjan@gmail.com"])
print("*"*40)
obj1 = Student(["chethan",16,102,"chethangamil.com"])
print("*"*40)
print(obj.__dict__)
print(Student.total) 

# create a class using static method and user defined constructor
class marks:
    def __init__(self,mark1,mark2,mark3):
        self.sub1 = mark1
        self.sub2 = mark2
        self.sub3 = mark3
        return self.validation(self.sub1,self.sub2,self.sub3)
    @staticmethod   #  used for validation
    def validation(x,y,z):
        print(f"the average marks is {(x+y+z)/3} ")
obj = marks(60,70,35)
obj1 = marks(40,70,80)
print(obj.__dict__)   
"""

#
class ATM:
    def __init__(self,balance):
        self.balance = balance
        
    def deposit(self,depo):
        self.depo = depo
        self.balance += depo
        print(f"your total balance is {self.balance}")
        
    def withdraw(self,withd):
        self.withd = withd
        if withd > self.balance:
            print("insufficient balance")
        else:
            self.balance -= withd
            print(f"your withdrawn amount is {self.withd}")
obj = ATM(5000)
print(obj.__dict__)
obj.deposit(1000)
obj.withdraw(7000)
            
        





