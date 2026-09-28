'''class A:
    a=10
    b='abc'
    def display(self):
        self.a=11
        print(self.a)
obj=A()
print(obj.a)
print(obj.b)
obj.display()
print(obj.a)
print(A.a)


class shravan:
    a=10
    b='abc'
    def sanjan(self):
        self.a = 11
        self.b = 'ef'
print(shravan.a)
print(shravan.b)
obj=shravan()
print(obj.a)
print(obj.b)
obj.sanjan()
print(shravan.a)
print(shravan.b)
print(obj.a)
print(obj.b)   

class A:
    pass
obj = A()
A.a=10
print(obj.a)
obj.a=11
print(obj.a)
obj1 = A()
print(obj1.a)
obj1.a=12
print(obj1.a)
print(obj.a)
print(A.a)   


class sanjan:
    a=10
    b=20
    def shravan(self):
        self.c = 12
        self.d = 13
        self.a = 13
obj = sanjan()
print(obj.a)
print(sanjan.a)
obj.shravan()
print(obj.a)
obj1=sanjan()
print(obj1.a)    '''

"""     
class Animal:
    a = "elephant"
    b = "bear"
    c = "lion"
    def cat(self):
        self.e = "tiger"
        self.f = "cheetah"
    def dog(self):
        self.g = "giraffe"
        self.h = "zebra"   


print(Animal.c)
        
obj1 = Animal()
print(obj1.__dict__)
print(obj1.a)
print(Animal.c)

print(Animal.__dict__)

obj2=Animal()
obj2.cat()
print(obj2.e)

obj3=Animal()
obj3.dog()
print(obj3.h)  

def reverse(number):
    a=int(str(number)[::-1])
    '''a = ""
    for i in str(number):
        a = i + a'''
    return a
print(reverse(int(input("Enter the number: "))))



def reverse1(string):
    i=0
    b = ""
    while i<len(string):
        b=string[i]+b
        i+=1
    return b
print(reverse1(input("enter the string:")))     

class A:
    def sample(self):
        self.name = 'shravan'
obj = A()
print(obj.__dict__)
A.sample(1)  

class Animal:
    print("hello")
    def cat(self):
        print("hello")   

def Student(name,age,course):
    print(f"name:{name}")
    print(f"age:{age}")
    print(f"course:{course}")
Student("sanjan",21,"pst")    


class Student:
    def details(self,name,age,course):
        print(f"name:{name}")
        print(f"age:{age}")
        print(f"course:{course}")
        
obj = Student()
obj.details("sanjan",21,"pst")
obj.a = 10
print(obj.__dict__)   




class Student:
    def details(self,name,age,course):
        self.name = name
        self.age = age
        self.cource = course
        
obj = Student()
obj.details("sanjan",21,"pfs")
obj.details("ram",23,"jfs")
print(obj.name)
print(obj.__dict__)
print(a)   

class Employee:
    def emp_details(self,name,id,department,gender,salary):
        self.Ename =name
        self.id = id
        self.department = department
        self.gender = gender
        self.salary = salary
        
obj = Employee()
obj.emp_details(input("enter the name:"),int(input("enter the id:")),input("enter the department:"),input("enter the gender:"),float(input("enter the salary:")))
print(obj.__dict__)
print(f"name:{obj.Ename}")   """


# printing each employee details separately using class and methods 
class Employee:
    def emp_details(self,emp1,emp2,emp3):
        self.employee1 = emp1
        self.employee2 = emp2
        self.employee3 = emp2
obj=Employee()
obj.emp_details(
    [int(input("enter id:")),input("enter your name:"),float(input("enter your salary"))],
    [int(input("enter id:")),input("enter your name:"),float(input("enter your salary"))],
    [int(input("enter id:")),input("enter your name:"),float(input("enter your salary"))])
d=obj.__dict__
for i in d:
    print("_"*20)
    print(f"Emp ID:{d[i][0]}")
    print(f"Emp name:{d[i][1]}")
    print(f"Emp salary:{d[i][2]}")
    print("_" *20)
    

        

      















        
