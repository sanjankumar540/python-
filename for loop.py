"""for i in 1,2,3,4:
    print(i)

# WAP to reverse the string using for loop
inp = "hello"
t=""
for i in inp:
    t=i+t
    print(i)
    print(t)
    print('-'*20)
print(t)

# WAP to check weather the string is palindrome or not

inp = input("enter the string:")
s=""
for i in inp:
    s=i+s
if inp == s:
    print("palindrome")
else:
    print("not palindrome")


# wAP for toggling
inp = input("enter the sentence:")
t=""
for i in inp:
    if 'A'<=i<='Z':
        t+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        t+=chr(ord(i)-32)
    else:
        t+=i
print(t)


import random
a="aeiouAEIOU"
inp =input("enter the alphabet:")
t=""
for i in inp:
    if i in a:
        t+=chr(ord(i)+1)
    elif i not in a:
        b = random.randint(0,9)
        t+=a[b]
print(t)  

inp = [1,2,3,4,7]
t=[]
for i in inp:
    t=[i]+t
print(t)    

# Count the number of characters in a string without using count() 
inp = input("enter the string:")
a=0
for i in inp:
    a=a+1
print(f"the length of your string is {a}")

# Count the number of vowels in a string without using count() 
inp = input("enter the string:")
a=0
for i in inp:
    if i in "aeiouAEIOU" :
        a = a+1
print(f" the number of vowels in the string is {a}")  

# Count uppercase and lowercase characters
inp = "PYthon PROGRamming"
a = 0
b = 0
for i in inp:
    if 'A'<=i<='Z' :
        a = a+1
    elif "a" <=i<= "z" :
        b = b+1
print(f"Uppercase: {a} ")
print(f"Lowercase: {b}")  "


# Count digits and alphabets  in a string

inp = "abc123xyGHz45PQRS3476"
a = 0
b = 0
for i in inp:
    if "A" <=i<= "Z" :
        a = a+1
    elif "a" <= i<="z":
        a=a+1
    elif i>="0":
        b = b+1
print(f"alphabets are :{a}")
print(f"digits are :{b}")

# remove all the  vowels from the word
inp = input("enter the word or sentence ")
c = ""
for i in inp:
    if i not in "aeiouAEIOU":
        c+= i
print(c)  


inp = int(input("enter the number:"))
factorial = 1
for i in range(1,inp+1):
    factorial = factorial *i
print(factorial)   """





    
