import random
'''print(random.randint(1,200))
print(random.randint(1,20))'''

'''print(random.uniform(1,30))
print(random.uniform(20,60))'''

'''a= [1,2,3,4]
print(random.shuffle(a))

print(random.randrange(10,100,5))
print(random.randrange(30,50,2))
print(random.uniform(20,60))
print(random.random())

print(random.choice([1,2,3,4,5]))
print(random.choice(('abcd')))
print(random.choice(('abcd')))

print(random.choice({8:1,9:2,4:3,6:9}))'''


#copy operation (shallow copy)
'''a = [1,2,3,4,[5,6]]
b = a.copy()
print(b)
a[4].append(5)
print(b)
print(id(b))
print(id(a))'''

#deepcopy
'''import copy
c = [3,4,5,[1,2]]
d = copy.deepcopy(c)
c[3].append(10)
d[3].append(20)
print(c)
print(d)'''

import copy
a = [1,2,{3,4},['a','b','c'],'abcd']
b = copy.deepcopy(a)
a[3].append(10)
a[2].pop()
a[2].update('abcd')
b[3].append('xyz')
print(a)
print(b)
