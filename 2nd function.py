"""def generate(st,ed):
    for i in range(st,ed):
        print(i)
generate(0,10)
generate(int(input("enter starting value:")),int(input("enter the ending value:"))) 

def toggling(st):
    t=""
    for i in (st):
        if 'A'<=i<='Z':
            t+=chr(ord(i)+32)
        elif 'a'<=i<='z':
            t+=chr(ord(i)-32)
        else:
            t+=i
    print(t)
toggling(input("enter the string:")) "
        


def reverse(st,ed):
    d={}
    for i in range(st,ed):
        a = str(i)[::-1]
        d[i] = int(a)
    print(d)
reverse(12,20) 

def add_dict(st,ed):
    d={}
    for i in range(st,ed):
        d[i]=i+1
    print(d)
add_dict(1,10)    

def up_low(st,ed):
    d={}
    for i in range(st,ed):
        d[chr(i+32)] = chr(i)
    print(d)
up_low(65,91)  """

'''def add(a,b):
    print(f"sum of {a} and {b} is {a+b}")

def sub(a,b):
    print(f"difference of {a} and {b} is {a-b}")

def mul(a,b):
    print(f"the product of {a} and {b} is {a*b}")

def floor(a,b):
    print(f"the floor division of {a} by {b} is {a/b}")

def true(a,b):
    print(f"the true dividion of {a} by {b} is {a//b}")

def mod(a,b):
    print(f"the remainder after dividing {a} by {b} is {a%b}")

add(10,20)
sub(int(input("enter the first number:")),int(input("enter the second number:")))
mul(int(input("enter the first number:")),int(input("enter the second number:")))
floor(int(input("enter the first number:")),int(input("enter the second number:")))
true(int(input("enter the first number:")),int(input("enter the second number:")))
mod(int(input("enter the first number:")),int(input("enter the second number:")))'''





    
