#public access specifier
"""class A:
    __a=10
    print(__a)
obj = A()
print(obj.__a)

class A:
    a=10
    @classmethod
    def sample(cls):
        cls.a=11
obj=A()
obj.sample()
print(A.__dict__)

#protected access specifier
class B:
    _a=10
    @classmethod
    def sample(cls):
        cls.a=11
obj=B()
obj.sample()
print(B.__dict__)
print(B._a)  

#private
class C:
    __a=10
    print(__a)
obj = C()
#print(obj.__a)
print(obj._C__a)  


class ATM:
    name ='sanjan'
    _gender = 'male'
    __password = 9980

    def greet(self):
        print("wellcome to ATM")
    def _balance(self):
        print("your balance is 1000")
    def __withdraw(self):
        print("amount withdrawn successfully")

obj = ATM()

#public
print(obj.name)
obj.greet()

#protected
print(obj._gender)
obj._balance()

#private
print(obj._ATM__password)
obj._ATM__withdraw()   



#getter and setter method
class Pyhton:
    name = "shravan"
    id = 1
    email = "sh@gmail.com"
    __mock = 0
    
    def get_mock(self):
        if self.__mock >= 7.5:
            print(f"{self.name} is having {self.__mock} rating and he is eligible to attend drives")
        else:
            print(f"{self.name} is having {self.__mock} rating and he is not eligible to attend drives")
    def set_mock(self,marks):
        self.__mock = marks
        
obj = Pyhton()
obj.get_mock()
obj.set_mock(7.5)
obj.get_mock()  

# another example
class vote:
    name = "sanjan"
    __age = 17
    def get_age(self):
        if self.__age >=18:
            print(f"{self.name} is {self.__age} years old and he is eligible to vote")
        else:
            print(f"{self.name} is {self.__age} old so he is not eligible to vote")
    def set_age(self,cur_age):
        self.__age = cur_age

obj = vote()
obj.get_age()
obj.set_age(21)
obj.get_age()    


class student:
    name = "sanjan"
    __gender = "M"

    def fetch_gender(self):
        return f"{self.name } is {self.__gender}"

obj = student()
print(obj.fetch_gender()) # whenever we are using return keyword we have to use print statement

#property decorator
class student:
    name = "sanjan"
    __gender = "M"
    
    @property
    def fetch_gender(self):
        return f"{self.name } is {self.__gender}"

obj = student()
print(obj.fetch_gender) # we can access the method as a variable accessing   


# property decorator with getter and setter

class python:
    name = "pranav"
    __mock = 0

    @property
    def mock_rating(self):
        if self.__mock >= 7.5:
            print(f"{self.name} is eligible to attend drives")
        else:
            print(f"{self.name} is not eligible to attend the drives")

    @mock_rating.setter    # along with the method name we have to give ".setter" as a decorator name (it is a connection between both methods).
    def mock_rating(self,mark):
        self.__mock = mark

obj = python()
obj.mock_rating  
obj.mock_rating = float(input("enter mock rating:"))
obj.mock_rating
"""
class vote:
    name = "chethan"
    __age = 15

    @property
    def eligible(self):
        if self.__age >=18:
            print(f"{self.name} is {self.__age} older so he is  eligible to vote")
        else:
            print(f"{self.name} is {self.__age} older so he is not eligible to vote")

    @eligible.setter
    def eligible(self,cur_age):
        self.__age = cur_age

obj = vote()
obj.eligible
obj.eligible = 19
obj.eligible
obj.eligible = int(input("enter your current age"))
obj.eligible
