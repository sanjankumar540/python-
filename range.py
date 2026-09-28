"""for i in range (0,11):
    print(i)

# reversing a list
inp = "redbean"
a = ""
for i in range(-1,-len(inp)-1,-1):
    a+=inp[i]
print(a)   

#reversing a tuple 
a= [1,2,3,4,5]
b=( )
for i in range (4,-1,-1):
    b+= (a[i],)
print(b)  

# WAP {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
#'s': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
d= {}
for i in range (65,91):
    d[chr(i+32)] =  chr(i)
print(d)   


#{12: 21, 13: 31, 14: 41, 15: 51, 16: 61, 17: 71, 18: 81, 19: 91}
d={}
for i in range (12,20):
    a =str(i) [::-1]
    d[i] = int(a)
print(d)    

for i in range(1,10):
    if i%2!=0:
        print(i)
    else:
        continue """

for i in range (1,10):
    pass
