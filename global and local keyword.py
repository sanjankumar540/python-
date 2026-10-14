"""
a =10
def sample():
    global a
    a+=1
    print(a)
sample()
print(a)


a = 10
def sample():
    global a
    a = 20
    print(a)
sample()
print(a)     





def sample():
    a = 10
    print(a)
sample()
#print(a)   #  name 'a' is not defined




def sample():
    global a
    a = 10
    print(a)
sample()
print(a)   """




def outer():
    name = "pranav"
    def inner():
        nonlocal name
        name = "sanjan"
        print(name)
    inner()
    print(name)
outer()


def outer():
    name = "sanjan"
    def inner():
        nonlocal name
        name = name + " " + "kumar"  
        print(name)
    inner()
    print(name)
outer()


"""def outer():
    name = "pranav"
    def inner():
        name = name + " " + "kumar"
        print(name)
    inner()
    print(name)
outer() """
