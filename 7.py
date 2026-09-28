x="python is a programming language"  #1
a = x.upper()
print(a)  #a

print (x.capitalize()) #b

a=x.title()
print(a) #c

b=x.split()
print(b)  #d

print(x.replace(" ","-"))  #e

y = ['python','is','a','powerfull','programming','language']
d = " " .join(y)
print(d) #2

z = "abc123"

print(z.isalpha())
print(z.isalnum())

p = 'abcd'
print(p.isupper())

print(p.islower())

r = {1,2,4,5,9,3} #6
s = {9,1,3,5,6,7}
print(r.intersection(s))

print(r.symmetric_difference(s))

print(r.difference(s))

print(r.union(s))

r.update('abcd')
print(r)

t = ['a','c','a','f','l','g','t'] #7
t.sort()
print(t)

t.sort()
t.reverse()
print(t)

t1 = frozenset({'a','c','a','f','l','g','t'})

t2 = frozenset({1,2,3,4,5,6}) #8

A = (1,2,3,4,'a','c',2,2,3) #9
A1 = A.count(2)
print(A1)

A2 = A.index('a')
print(A2)


B = (1,2,3,[1,2],{'a','b','c'}) #10
B[3].extend('ab')
print(B)

B[3].pop(0)
B[3].pop(0)
print(B)

B[4].remove('a')
print(B)

B[4].add






