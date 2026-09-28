"""#object method
#non parameterized using inputs directly
class StudentDetails:
    def student(self):
        self.name = input("enter your name:")
        self.age=int(input("enter your age:"))
        self.id=int(input("enter your id:"))
        self.email=input("enter your email:")
obj=StudentDetails()
obj.student()
print(obj.__dict__)
obj.name="shravan"
print(obj.__dict__)

# parameterized
class StudentDetails:
    def student(self,name,age,roll_no,email):
        self.name = name
        self.age=age
        self.id=roll_no
        self.email=email
obj=StudentDetails()
obj.student(input("enter your name:"),int(input("enter your age:")),int(input("enter your id:")),input("enter your email:") )
print(obj.__dict__)


# non parameterized
class EmployeeDetails:
    @classmethod
    def employee(cls):
        cls.ename=input("enter the employee name")
        cls.eid=int(input("enter your id:"))
        cls.email=input("enter your email:")
        cls.department=input("eneter your department:")
obj = EmployeeDetails()
obj.employee()
print(EmployeeDetails.__dict__)


#class methods
#parameterized
class EmployeeDetails:
    @classmethod
    def employee(cls,ename,eid,email,department):
        cls.ename=ename
        cls.eid=eid
        cls.email=email
        cls.department=department
obj = EmployeeDetails()
obj.employee(input("enter the employee name"),int(input("enter your id:")),input("enter your email:"),input("eneter your department:"))
print(EmployeeDetails.__dict__)  


#updation
class EmployeeDetails:
    ename="sanjan"
    eid=1
    email="sanjan@123"
    department="developer"
    @classmethod
    def employee(cls,ename,eid,email,department):
        cls.ename=ename
        cls.eid=eid
        cls.email=email
        cls.department=department
obj = EmployeeDetails()
obj.employee(input("enter the employee name"),int(input("enter your id:")),input("enter your email:"),input("eneter your department:"))
print(EmployeeDetails.__dict__)  


# STATIC METHODS(HELPER METHOD)
class A:
    a=10
    def student(self,m1,m2,m3):
        self.sub1 = m1
        self.sub2 = m2
        self.sub3 = m3
        return self.validate(self.sub1,self.sub2,self.sub3)
    @staticmethod
    def validate(a,b,c):
        if a+b+c>=105:
            print("pass")
        else:
            print("fail")

obj = A()
obj.student(83,36,74)       

class A:
    a=10
    def student(self,m1,m2,m3):
        self.sub1 = m1
        self.sub2 = m2
        self.sub3 = m3
        return self.validate(self.sub1,self.sub2,self.sub3)
    @staticmethod
    def validate(a,b,c):
        if a >=35:
            print("pass in first subject")
        else:
            print("fail in first subject")
        if b >=35:
            print("pass in second subject")
        else:
            print("fail in second subject")
        if c>=35:
            print("pass in third subject")
        else:
            print("fail in third subject")

obj = A()
obj.student(int(input("enter marks obtained in first subject:")),int(input("enter marks obtained in second subject:")),int(input("enter marks obtained in third subject:")))   


class employee:
    def experience(self,emp1,emp2,emp3):
        self.emp1 = emp1
        self.emp2 = emp2
        self.emp3 = emp3
        return self.validate(self.emp1,self.emp2,self.emp3)
    @staticmethod
    def validate(a,b,c):
        if 1<=a<=3:
            print("1st employee is junior")
        else:
            print("1st employee is senior")
        if 1<=b<=3:
            print("1st employee is junior")
        else:
            print("1st employee is senior")
        if 1<=b<=3:
            print("1st employee is junior")
        else:
            print("1st employee is senior")
obj = employee()
obj.experience(int(input("enter your experience ")),int(input("enter your experience ")),int(input("enter your experience ")))


class Calculator:
    def operations(self,operator,a,b):
        self.operator=operator
        self.a=a
        self.b=b
        return self.validate(self.operator,self.a,self.b)

    @staticmethod
    def validate(z,c,d):
        if z=="+" :
            print(c+d)
        if z== "-" :
            print(c-d)
        if z == "*":
            print(c*d)
        if z == "/":
            print(c/d)
        else:
            print("invalid operator")

obj = Calculator()
obj.operations(input("enter the operator:"),int(input("enter the  first value:")),int(input("enter the second value:")))   """


            
class EmployeeDetails:
    @classmethod
    def employee(cls,ename,eid,email,department):
        cls.ename=ename
        cls.eid=eid
        cls.email=email
        cls.department=department
obj = EmployeeDetails()
obj.employee("sanjan",2,"@gmail.com","it")
print(EmployeeDetails.ename)









