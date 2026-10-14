"""def fun(a):
    print(a)
fun(1,2,3,4 ) 

def fun(*a):
    print(a)
    print(type(a))
fun(1,2,"abc",3,4)  


def sample(*args ,a,b):
    print(args)
    print(a)
    print(b)
sample(10,20,30,a=40,50)   """


def student(name,age,*skills):
    print("name:",name)
    print("age:",age)
    print("skills:",skills)

student("sanjan",21,"python","sql","webtech","django")


def student(name,age,*skills):
    print("name:",name)
    print("age:",age)
    print("skills:",list(skills))

student("sanjan",21,"python","sql","webtech","django")
