"""class parent:
    def __init__(self):
        self.a = 10
        self.b = 20
class child(parent):
    def __init__(self):
        super().__init__()
        self.c = 30
        self.d = 40
obj = child()
print(obj.__dict__)

class child1(child,parent):
    
# single level + maultiple
class parent:
    a = 10
class child(parent):
    b = 20
class child1(child ,parent):
    def __init__(self):
        self.c = 11
obj = child1()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.__dict__)


# multilevel + multiple
class A:
    def __init__(self):
        super().__init__()
        self.a = 10
class B(A):
    def __init__(self):
        super().__init__()
        self.b = 11
class C(B):
    def __init__(self):
        super().__init__()
        self.c = 12

class child(C,B,A):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        C.__init__(self)
        self.d = 14
obj = child()
print(obj.__dict__)  """


#multiple + hierarchical
class parent:
    def __init__(self):
        self.a = 10
        
class parent1:
    def __init__(self):
        self.b = 11
        
class parent2:
    def __init__(self):
        self.c = 12
        
class child(parent2,parent1,parent):
    def __init__(self):
        parent2.__init__(self)
        parent1.__init__(self)
        parent.__init__(self)
        self.d = 13

class child1(child):
    def __init__(self):
        child.__init__(self)
        self.x=20
        
class child2(child):
    def __init__(self):
        child.__init__(self)
        self.y = 30
        
class child3(child):
    def __init__(self):
        child.__init__(self)
        self.z = 40
        
obj1 = child1()
obj2 = child2()
obj3 = child3()
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)


