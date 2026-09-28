"""# object method (non parameterized using inputs directly )
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
print(obj.__dict__)"""

# non parameterized
class StudentDetails:
    def student(self,name,age,roll_no,email):
        self.name = name
        self.age=age
        self.id=roll_no
        self.email=email
obj=StudentDetails()
obj.student(input("enter your name:"),int(input("enter your age:")),int(input("enter your id:")),input("enter your email:") )
print(obj.__dict__)
print(obj) # <__main__.StudentDetails object at 0x0000020F4C78E900>  (it will give the referrnce address of that object) 




