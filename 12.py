"""print([10] not in [1,2,[10]])
print(('a')in('a','b','c'))
print( 'a' not in ('a','b','c'))
print('a' in 'abc')
print( 10 in [10,20,30])"""

a=1
b=1
print(a is not b)
a=1.2
b=1.2
print(a is not  b)
a=1+1j
b=1+1j
print(a is not b)
a=False
b=False
print(a is not b)

a="abc"
b="abc"
print(a is not b)

a=[1,2,3]
b=[1,2,3]
print(a is not b)

a=('1','2','3','4')
b=('1','2','3','4')
print(a is not b)

a={'1','2','3','4'}
b={'1','2','3','4'}
print( a is not b)

a = {'a':'hii'}
b = {'a':'hii'}
print(a is not b)
