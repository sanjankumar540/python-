# reverse a number 
def rev_num(nums):
    t1 = str(nums)
    t2 = t1[::-1]
    t3 = int(t2)
    return t3
a = list(map(rev_num,[123,456,789]))
print(a)

#reverse a string of collection
def rev_str(string):
    return string[::-1]
a = list(map(rev_str ,("sanjan","shravan")))
print(a)


#using inbuilt functions
s = [[1,2,3],[4,5,6],[7,8,9]]
a = tuple(map(max,s))
print(a)

#using lambda function
square = list(map(lambda a: a**2 ,[1,2,3,4]))
print(square)


