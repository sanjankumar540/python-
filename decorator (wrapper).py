"""def decorator_function(func):
    def wrapper():
        print("before function call ")
        func()
        print("after function call")
    return wrapper

@decorator_function
def sample():
    i = 1
    while i<=5:
        print(i)
        i+=1
sample()  """


def timer(func):
    def wrapper():
        import time
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper

@timer
def palindrome():
    s = input("enter your string")
    t = ""
    for i in s:
        t = i+t   
    if t == s:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome()

def timer(func):
    def wrapper():
        import time
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper

@timer
def palindrome():
    s = input("enter your string")
    t = ""
    for i in s:
        t = i+t   
    if t == s:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome()



def timer(func):
    def wrapper():
        import time
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper

@timer
def palindrome():
    s = input("enter your string")
    t = ""
    for i in s:
        t = i+t   
    if t == s:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome()

