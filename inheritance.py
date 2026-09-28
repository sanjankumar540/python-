"""class parent :
    a=10
    def __init__(self):
        self.b=11

class child (parent):
    a=11  
    d=10
    def __init__(self):
        self.c=11
obj = child()
print(obj.__dict__)
        
print(obj.a)
  
print(obj.b)    

# method chaining (non parameterized)
class parent:
    def dcl(self):
        self.name1 = "shravan"
        self.email1 = "shravan@gmail.com"
class child(parent):
    def dcl(self):
        super().dcl()
        #parent.dcl(self)
        self.name2 = "sanjan"
        self.email2 = "sanjan@gmail.com"
obj = child()
obj.dcl()
print(obj.__dict__) 


#method chaining (parameterized)
class A:
    def sample(self,a,b):
        self.a = a
        self.b = b
class B(A):
    def sample(self,c,d,a,b):
        super().sample(a,b)  ###
        self.c = c
        self.d = d
obj = B()
obj.sample(5,6,7,8)
print(obj.__dict__)

# or
class A:
    def sample(self,a,b):
        self.a = a
        self.b = b
class B(A):
    def sample(self,c,d,a,b):
        A.sample(self,a,b)  ###
        self.c = c
        self.d = d
obj = B()
obj.sample(5,6,7,8)
print(obj.__dict__) 


# constructor chaining (non paraeterized)
class A :
    def __init__(self):
        self.a = 10
        self.b = 12
class B(A):
    def __init__(self):
        super().__init__()
        self.c = 13
        self.d = 14
obj = B()
print(obj.__dict__)

#or
class A:
    def __init__(self):
        self.a = 10
        self.b = 11
class B(A):
    def __init__(self):
        A.__init__(self)
        self.c = 12
        self.d = 13
obj = B()
print(obj.__dict__)   


# constructor chaining (parameterized)
class ylk :
    def __init__(self,a,b):
        self.a = a
        self.b = b
class btm(ylk):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c = c
        self.d = d
obj = btm(10,20,30,40)
print(obj.__dict__)    """


# MULTI LEVEL INHERITANCE #
#=========================#
class grandfather :
    a = 10
    def display(self):
        print("grandfather")
class father(grandfather):
    b = 11
    def display(self):
        super().display()
        print("father")
class son(father):
    c = 13
    def display(self):
        super().display()
        print("son")
obj = son()
obj.display()
print(obj.__dict__)

