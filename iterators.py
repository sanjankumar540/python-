"""#iterators on list
a = [1,2,3,4,5]
b = iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#iterators on string

p = "sanjan"
q = iter(p)
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))     


x = (10,20,30,40,50)
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))   


s = {1,2,3,4,5,5}
t = iter(s)
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))   


d = {1:"odd" ,2:"even", 3:"odd", 4:"even", 5:"odd"}
e = iter(d)
print(d[next(e)])
print(d[next(e)])
print(d[next(e)])
print(d[next(e)])
print(d[next(e)])   """



def gen_num():
    for i in range(1,11):
        yield i
a = gen_num()
print(next(a))
print(next(a))
print(a)
print(set(a))

