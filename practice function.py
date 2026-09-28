'''import random
def vowel(string):
    a='aeiouAEIUO'
    b=""
    for i in string:
        c=random.randint(0,9)
        if i in a:
            b+=chr(ord(i)+1)
        else:
            b+=a[c]
    return(b)
print(vowel(input("enter the string:"))) 

# reverse a string
def reverse(inp):
    s=""
    for i in inp:
        s=i+s 
    return(s)
print(reverse(input("enter the string:")))


# reverse a list
def reverse2():
    l=[1,2,3,4,9]
    i=0
    s=[]
    while i<=len(l)-1:
        s=[l[i]]+s
        i+=1
    return(s)
print(reverse2())

# reverse a tuple
def reverse3():
    t=(1,2,3,4,5)
    s=()
    for i in t:
        s=(i,)+s
    return(s)
print(reverse3())

# {12: 21, 13: 31, 14: 41, 15: 51, 16: 61, 17: 71, 18: 81, 19: 91}
def num_rev(st,ed):
    d={}
    for i in range(st,ed+1):
        a=str(i)[::-1]
        d[i]=int(a)
    return d
print(num_rev(12,19)) 

#{'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
#'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
def alpha(st,ed):
    d={}
    for i in range(st,ed+1):
        d[chr(i)]=chr(i+32)
    return d
print(alpha(65,90))

#{'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S',
#'t': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
def alpha2(st,ed):
    d={}
    for i in range(st,ed+1):
        d[chr(i+32)]=chr(i)
    return d
print(alpha2(65,90))  '''
    

    
            
