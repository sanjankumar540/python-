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
sample(10,20,30,a=40,50)   


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



# dictionary packing
def dictionary_packing(kwargs):
    print(kwargs)
dictionary_packing({"name":"pranav" , "course":"pst"}) 

def student(**kwargs):
    print(f"student name : {kwargs.get('name')}")
    print(f"student course : {kwargs.get('course')}")
    print(f"student skills: {kwargs.get('skills')}")
student(name = 'sanjan',course = "pfs", skills = ['python','webtech','sql'])    


#tuple and dictionary packing together
def product(*args,**kwargs):
    print(f"product name :{kwargs.get('name')}")
    print(f"RAM: {kwargs.get('ram')}")
    print(f"ROM: {kwargs.get('rom')}")
    print(f"price:{args[0]}")
    print(f"quantity:{args[1]}")
    print(f"brand: {args[2]}")
product(49999,20,"nothing",name ="mobile",ram="16gb",rom="256gb" )   





# tuple unpacking

def student(name ,age,course):
    print(f"name:{name}")
    print(f"age:{age}")
    print(f"course:{course}")
    print(f"-"*30)
student("sanjan",21,"pfs")
details = ("shravan",21,"pfs")
student(*details)   """


#dictionary unpacking

def student(name ,age,course):
    print(f"name:{name}")
m    print(f"age:{age}")
    print(f"course:{course}")
    print(f"-"*30)
details = {'name':"pranav",'age':42, "course" : "mern"}   # dictonary unpacking
student(**details)      
