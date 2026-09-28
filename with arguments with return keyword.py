"""def vote (st,ed):
    l=[]
    for i in range(st,ed+1):
        if i>=18:
            l.append(f"{i} years is eligible")
        else:
            l.append(f"{i} years is not eligible")
    return l
print(vote(15,20)) """



"""def vote(name,age):
    if age>=18:
        a = f"{name} your age is {age}, you are eligible to vote"
    else:
        a = f"{name} your age is {age}, you are not eligible to vote"
    return a
print(vote (input("enter your name:") , int(input("enter your age:"))))  

#
def multiple(st,ed):
    d={}
    for i in range(st,ed+1):
        d[i**2]=i**3
    return d
print(multiple(1,10))

# string toggling
def tog(a):
    b=""
    for i in a:
        if 'A' <= i <='Z' :
            b+=chr(ord(i)+32)
        else:
            b+=chr(ord(i)-32)
    return b
print(tog("SANJANkumar"))  


  """

def add(a,b):
    c=a+b
    return c
print(add(int(input("enter first number")),int(input("enter the second number:"))))
        
        



    
        

    
