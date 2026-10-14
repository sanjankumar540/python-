"""
def sample(a,b,c,x=0,y=1,z=2):
    print(a,b,c)
    print(x,y,z)
    print(a+b+c+x+y+z)

sample(10,20,30)
sample(1,2,3,4,5,6)


# global scope and local scope
a = 10
def sample():
    b=20
    print(a,b)
sample()






# nested functions

def outer():
    name = "shravan"
    def  inner():
        name = "sanjan"
        print(name)
    inner()
    return name
print(outer())    



def outer():
    name = "shravan"
    def  inner():
        print(name)
    inner()
    return name
print(outer())    


name = "mithun"
def outer():
    def  inner():
        print(name)
    inner()
    return name
print(outer())    


name = "pranav"
def outer():
    name = "shravan"
    def inner():
        name = "sanjan"
        print(name)
    inner()
    return name
print(outer())
print(name)





#global and local variables

a = 10
def outer(b,c):
    print(a,b,c)
    def inner():
        print(a,b,c)
    inner()
outer(30,40)
print(b,c) #local variables cannot be accessed outside the function   (name 'b' is not defined)


a = 10
def outer(b,c):
    a = 11
    print(a,b,c)
    def inner():
        print(a,b,c)
    inner()
outer(30,40)
print(b,c)   



a = 10
def outer(b,c):
    a = 11
    print(a,b,c)
    def inner():
        a=10
        b=11
        c=12
        print(a,b,c)
    inner()
outer(30,40)   """





