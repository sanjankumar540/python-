#specific exception handling
"""try:
    a="abc"
    b=10
    print(a+b)
    print(100/0)

except TypeError:
    print("concatination not supported bw int and str")
except ZeroDivisionError:
    print("number cannot be divide by 0")

try :
    print(10+100)
    print('a'+'b')
    print(100/10)

except:
    print("division is not posiible when denomenator is zero")

else:
    print("no exception found")

finally:
    print("program completed")  

try:
    print(10/0)
    print('a'+1)

except Exception:
    print("int cant be divided by zer0")     



# default exception handling

try:
    print(10/0)
except:
    print("exception handled successfully")    


# keyboard interrupt
try:
    i=1
    while i<=5:
        print(i)
except:
    print("program handled exception")
else:
    print("no exception")
finally:
    print("program completed")   

#raise keyword
a=1 
if a:  
    print("it is a truthy value")
else:
    raise Exception("it is a falsy value")   



age = int(input("enter your age:"))
if age >= 18:
    print("you are eligible to vote:")
else:
    raise Exception("you are minor")  

# custom exception
class impropername(Exception):
    pass
name = input("enter your name:")
if name.isalpha():
    print(f"{name} is in proper manner")
else:
    raise impropername("name can contain only alphabets")   


class valid_email(Exception):
    pass
email = input("enter your email:")
if email.endswith("dcl@gmail.com"):
    print("it is a dheecoding lab email")
else:
    raise valid_email("not a dheecoding lab email")   


inp = input("enter your sring:")
t = ""
for i in inp:
    t=i+t
assert t==inp,"it is not a palindrome"
print("it is a palindrome")  """

# list palindrome
l = eval(input())
temp = []
i=0
while i<=len(l)-1:
    temp = [l[i]]+temp
    i+=1
assert l==temp ,"list is not a palindrome"
print("list is a palindrome")
print(temp)
    
