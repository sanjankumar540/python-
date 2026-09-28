"""# print numbers from 1 to 10
      i=10
while i>=1:
    print(i)
    i=i-1
# print numbers from 1 to 15  
i = 1
while i<=15:
    print(i)
    i=i+1

#print numbers from -1 to -15
i = -1
while i >= -15:
    print(i)
    i-=1   
# print numbers from -10 to 10
i = -10
while i<=10:
    print(i)
    i+=1  

# print even numbers between the starting and ending value
i = int(input("enter your starting value:"))
a = int(input("enter the ending value:"))
while i<=a:
    if i%2==0:
        print(i)
    i+=1 

# 
i = 1
while i <= 200:
    if i%3==0 and i%5==0:
        print(i)
    i+=1 

i = 1
while i<=20:
    print(i**2)
    print(i**3)
    i+=1  

# print each element of the string
a = input("enter your string:")
i = 0
while i <= len(a)-1:
    print(a[i])
    i+=1  
# print every elements of input separately
inp =('a','b','c','d','e','f')
i = 0
while i <= len(inp)-1:
    print(inp[i])
    i=i+1   

i = -10
while i<=10:
    if i%2==0:
        print(i)
    i=i+1  

# wap to print ['odd',2,'odd',4,'odd',6,'odd',8,odd,10]
l = []
i = 1
while i<=10:
    if i%2==0:
        l.append(i)
    else:
        l.append("odd")
    i+=1
print(l)


# wap to reverse the string
inp = input("enter you string:")
i = 0
s=" "
while i <= len(inp)-1:
    s=inp[i] + s
    print(s)
    i+=1 
print(s)

# or
inp = input ("enter your string:")
i = -1
k = " "
while i <= -len(inp):
    k = inp[i] + k
    print(k)
    i-=1
print(k) 

# reverse a list 
a = [1,2,3,4,5]
k = []
i = -1
while i>=-len(a):
    k.append(a[i])
    i=i-1
    print(k)
print(k)
# or
inp = [1,2,3,4]
i = len(inp)-1
k = []
while i >= 0 :
    k.append(inp[i])
    i = i-1
    print(k)
print(k) 

# reverse a tuple (important)
inp = (1,2,3,4)
i=0
s = ()
while i <=len(inp)-1:
    s = (inp[i],) + s 
    i=i+1
print(s)  
 # or
 
inp = (1,2,3,4,5)
s = ()
i = len(inp)-1
while i >= 0:
    s = s+(inp[i],) 
    i=i-1
print(s) 


# WAP to check whether the string is palindrome or not
inp = input("enter your string:")
i = 0
s =""
while i<=len(inp)-1:
    s = inp[i] + s
    i+=1
if inp == s:
    print("it is a palindrome") 
else:
    print("it is not a palindrome") 

#Find the sum of numbers from 1 to N  
inp = int(input("enter the number"))
i= 0
total = 0
while i<=inp:
    total = total +i
    i=i+1
print(total)

#Find the sum of even numbers from 1 to N
inp = int(input("enter the number"))
i= 0
total = 0
while i<=inp:
    if i%2==0:
        total = total +i
    i=i+1
print(total)  


# Count the numbers from 1 to N
inp = int(input("enter the number:"))
i = 1
total = 0
while i<=inp:
    total=total+1
    i=i+1
print(total)  

#Find the factorial of a number
inp = int(input("enter the number:"))
i=1
factorial = 1
while i<=inp:
    factorial = factorial*i
    i=i+1
print(factorial) 

# wAP to print square of a number
inp = int(input("enter the number:"))
i = 0
while i<=inp:
    print(i*i)
    i=i+1  

# WAP to print {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}  without any input
d= {}
i=1
while i<=9:
    d[i] = i+1   # alter method  
    i=i+1
print(d)  

# WAP to print {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q',
# 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}

d= {}
i = 65
while i <=90:
    d[chr(i)] =chr(i + 32)
    i =i+1
print(d)

# reverse of the above  {'Z': 'z', 'Y': 'y', 'X': 'x', 'W': 'w', 'V': 'v', 'U': 'u', 'T': 't', 'S': 's', 'R': 'r', 'Q': 'q', 'P': 'p', 'O': 'o', 'N': 'n', 'M': 'm', 'L': 'l', 'K': 'k',
# 'J': 'j', 'I': 'i', 'H': 'h', 'G': 'g', 'F': 'f', 'E': 'e', 'D': 'd', 'C': 'c', 'B': 'b', 'A': 'a'}

d= {}
i=90
while i>=65:
    d[chr(i)] = chr(i+32)
    i-=1
print(d)  


# WAP {12: 21, 13: 31, 14: 41, 15: 51, 16: 61, 17: 71, 18: 81, 19: 91}
d = {}
i=12
while i<=19:
    a = str(i)[::-1]
    d[i] = int(a)
    i+=1
print(d)   """


d={}
i=12
while i <=19:
    a = str(i)[::-1]
    d[i] = int(a)
    i+=1
print(d)



    








    
    
