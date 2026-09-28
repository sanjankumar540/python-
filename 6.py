'''tup = (['cpython','brython','jython'],('plainpython','java',('vertual machine','pvm')))
tup[0][1]='python1'
print(tup) #to alter

tup1 = tup[1][2][1][2]+tup[1][2][1][1]+tup[1][2][1][0]
print(tup1)

tup2 = tup[1][0][8]+tup[1][0][7]+tup[1][0][6]+tup[1][0][5]+tup[1][0][4]
print(tup2)

tup3 = tup[0][0],tup[0][1],tup[0][2]
print(tup3)'''

a={"a":10,"b":20}
a.update({'c':30})
print(a)

b={'a':10,'b':20}
b.pop('a')
print(b)

del b['b']
print(b)

b={'a':10,'b':20}
b.get('c','no value')
print(b)

c = "abcd"
d = dict.fromkeys(c,10)
print(d)
print(d.items())




