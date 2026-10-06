"""a = 10
result ="hello" if a else "goodbye"
print(result)  

age = int(input("enter your age:"))
ans = "you can vote" if age >=18 else "not eligible to vote"
print(ans)   


l = [i      for i in range(-1,-6,-1)]
print(l)

l = [i      for i in range(0,6)]
print(l)  

l = [i     for i in range(1,11)  if i%2 == 0]
print(l)


l = [i    for i in range(1,11)   if i%2 !=0]
print(l) 




l = []
for i in range(1,11):
    if i %2 ==0:
        l.append((i,"even"))
    else:
        l.append((i,"odd"))
print(l)   


l = [ (i,"even")   if i%2==0  else  (i,"odd")   for i in range(1,11)]
print(l)   





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
print(l)    """


l = [( (i,"fizzbuzz") if i%5 == 0   else   (i,"fizz") )   if i%3==0     else      (  (i,"buzz")  if i%5==0   else  (i,"miss")  )    for i in range(1,51)]
print(l)
