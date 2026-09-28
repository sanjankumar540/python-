#mro (method resolution order)
"""class A:
    def sample(self):
        self.a = 10
class B(A):
    def sample(self):
        super().sample()
        self.b = 11
class C(B):
    def sample(self):
        super().sample()
        self.c = 12
obj = C()
obj.sample()
print(obj.__dict__)
print(C.mro())  """

#mro for hybrid inheritance
class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(B,C):
    pass
print(D.mro())


