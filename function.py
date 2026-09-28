""" def reverse():
    inp = int(input("enter the number:"))
    a = str(inp)[::-1]
    b = int(a)
    print(b)
reverse()  

def reverse():
    l = [1,2,3,4,5]
    a = []
    for i in l:
        a = [i]+a
    print(a)
reverse()   """

def reverse2():
    t = (1,2,3,4,5)
    a = ()
    for i in range(0,len(t)):
        a = (t[i],)+ a
    print(a)
reverse2()



