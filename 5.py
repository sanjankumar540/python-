'''a = [2,4,3,1,5]
b = ['b','d','h','a','c','e']
c = [1,2,3,'a','b','c','d']

a.sort()
a.reverse()
print(a)

b.sort()
print(b)

c.reverse()
print(c)

e=a+b+c
print(e)

e.reverse()
print(e)

e.extend('mnopqrst')
print(e)

e.pop()
print(e)

e.insert(1,'z')
print(e)

e.clear()
print(e) '''

p = ['abc',1,['raju','python','java',['css','js','html','react'],6],2,3,4]

q = [p[5]]+[p[3]]+[p[1]]
print(q)

r = [p[0]]+[p[2]]+[p[4]]
print(r)

s = [p[2][0]]+[p[2][2]]+[p[2][4]]
print(s)

t = [p[2][3][0]]+[p[2][3][2]]+[p[2][3][3]]
print(t)



