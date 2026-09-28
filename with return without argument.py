"""
# reverse a string using while loop
def reverse():
    inp=input("enter the string:")
    t=""
    i=0
    while i<len(inp):
        t=inp[i]+t
        i=i+1
    return f"the reverse of {inp} is {t}"
print(reverse()) 

# important 
def list_to_dict():
    inp = [
        ['ramesh',1,'ramesh@gmail.com',8412345678],
        ['pranav',2,'pranav@gmail.com',8431138432],
        ['sanjan',3,'sanjan@gmail.com',9980039914]
        ]
    s=[]
    i=0
    while i<len(inp):
        s.append({
            'name':inp[i][0],
            'id':inp[i][1],
            'email':inp[i][2],
            'phone_no':inp[i][3]
            })
        i+=1
    return s
print(list_to_dict())  """



        


        
