"""class parent1:
    x=10
    def __init__(self):
        self.a = 10
        self.b = 11
class parent2:
    x=11
    def __init__(self):
        self.c = 12
        self.d = 13
class parent3:
    x=12
    def __init__(self):
        self.e = 14
        self.f = 15
class child(parent3, parent2, parent1):
    x=13
    def __init__(self):
        super().__init__()#
        super().__init__()#
        super().__init__()#   
        self.g = 16
        self.h = 17
obj = child()
print(obj.__dict__)    

class parent1:
    x=10
    def __init__(self):
        self.a = 10
        self.b = 11
class parent2:
    x=11
    def __init__(self):
        self.c = 12
        self.d = 13
class parent3:
    x=12
    def __init__(self):
        self.e = 14
        self.f = 15
class child(parent3, parent2, parent1):
    x=13
    def __init__(self):
        parent3.__init__(self)
        parent2.__init__(self)
        parent1.__init__(self)
        self.g = 16
        self.h = 17
obj = child()
print(obj.__dict__)     """

class fly:
    def display(self):
        print("i can fly")
class swim:
    def display(self):
        print("i can swim")
class walk:
    def display(self):
        print("i can walk")
class duck(walk,swim,fly):
    def sample(self):
        fly.display(self)
        swim.display(self)
        walk.display(self)
obj = duck()
obj.sample()
