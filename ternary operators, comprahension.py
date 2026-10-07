
"""a = 10
result ="hello" if a else "goodbye"
print(result)  

age = int(input("enter your age:"))
ans = "you can vote" if age >=18 else "not eligible to vote"
print(ans)   

#ternary operator
#comprahension for list (for loop and if condition)
l = [i      for i in range(-1,-6,-1)]
print(l)

l = [i      for i in range(0,6)]
print(l)  

l = [i     for i in range(1,11)  if i%2 == 0]
print(l)


l = [i    for i in range(1,11)   if i%2 !=0]
print(l) 



#comprahension for list (if - else both)
l = []
for i in range(1,11):
    if i %2 ==0:
        l.append((i,"even"))
    else:
        l.append((i,"odd"))
print(l)   


l = [ (i,"even")   if i%2==0  else  (i,"odd")   for i in range(1,11)]
print(l)   




# comprahension for list (multiple nested if else condition)
l = []
for i in range(1,51):
    if i%3==0:
        if i%5==0:
            l.append((i,"fizzbuzz"))
        else:
            l.append((i,"fizz"))
    else:
        if i%5 == 0:
            l.append((i,"buzz"))
        else:
            l.append((i,"kiss"))
print(l)    

# syntax [   (value if true)  if<condition>   (value if false)   else    (value if true)    if<condition>    (value if false)    (value if true)  else       (value if fals    for loop ]
l = [( (i,"fizzbuzz") if i%5 == 0   else   (i,"fizz") )   if i%3==0     else      (  (i,"buzz")  if i%5==0   else  (i,"miss")  )    for i in range(1,51)]
print(l)  



#comprahension for set

s = set()
for i in range(0,11):
    if i%2==0:
        s.add(i)
print(s)

s = {  i   for i in range(0,11)           if i%2==0}
print(s)     




l = []
for i in range(1,51):
    if i%3==0:
        if i%5==0:
            l.append((i,"fizzbuzz"))
        else:
            l.append((i,"fizz"))
    else:
        if i%5 == 0:
            l.append((i,"buzz"))
        else:
            l.append((i,"kiss"))
print(l)


s = { (i,"fizzbuzz")     if i%5==0      else (i,"buzz")     if i%3==0        else    (i,"buzz")          if i%5==0               else    (i,"miss")          for i in range(1,51)      }
print(s)       




# dictionary comprahension

d = {}
for i in range(1,6):
    d[i] = i*2
print(d)



d = {   i:i*2          for i in range(1,6)}
print(d)


d = {   i:i+1      for i in range(1,11)}
print(d)


d = {}
for i in range(65,91):
    d[chr(i)] = chr(i+32)
print(d)



d={ chr(i) : chr(i+32)                 for i in range(65,91) }
print(d)   


d = {}
for i in range(65,91):
    if chr(i) in 'AEIOU':
        d[chr(i)] = chr(i+32)
print(d)


d = {     chr(i) : chr(i+32)           for i in range(65,91)            if chr(i) in 'AEIOU'}
print(d)    




d = {}
for i in range(97,123):
    if chr(i) in 'aeiou':
        d[chr(i)] = chr(i-32)
print(d)


d = {    chr(i) : chr(i-32)           for i in range(97,123)     if chr(i) in 'aeiou'         }
print(d)   




d = {}
for i in range(65,91):
    if chr(i) not in 'AEIOU':
        d[chr(i)] = chr(i+32)
print(d)

d = {       chr(i):chr(i+32)        for i in range(65,91)     if chr(i) not in 'aeiou' }
print(d)   



#dictionary comprahension with for loop and if else
d={}
for i in range(1,11):
    if i%2 == 0:
        d[i] = "even"
    else:
        d[i] = "odd"
print(d)


d = {    i:"even"    if i %2 ==0    else   "odd"    for i in range(1,11) }
print(d)  """



d= { }
for i in range(1,51):
    if i%3 == 0:
        if i%5 == 0:
            d[i] = "fizzbuzz"
        else:
            d[i] = "fizz"
    else:
        if i%5 == 0:
            d[i] = "buzz"
        else:
            d[i] = "miss"
print(d)


d = { i:   ( "fizzbuzz"        if i%5 ==0    else   "fizz"     ) if i%3 ==0  else (   "buzz"        if i%5==0   else    "miss"  ) for i in range(1,51)}
print(d)




        
