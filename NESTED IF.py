"""inp = int(input("enter the number :"))
if inp%3==0:
    if inp%5==0:
        print(f"{inp} is divisible by both")
    else:
        print(f"{inp} is only divisible by 3")
else:
    if inp%5==0:
        print(f"{inp} is only divisibl by 5")
    else:
        print(f"{inp} is not divisible by both") 


inp = int(input("enter the number:"))
if  inp>0:
    print("number is positive")
else:
    if inp==0:
        print("number is zero")
    else:
        print("number is negative")
        

inp = int(input("enter the number:"))
if inp>0:
    if inp%2==0:
        print(f"{inp} is even")
    else:
        print(f"{inp} is odd")
else:
    print(f"{inp} is not positive")


inp = input("enter the alphabet")
if 'A'<=inp<='Z' or 'a'<=inp<='z' :
    if inp in 'AEIOUaeiou':
        print(f"{inp} alphabet is vowel")
    else:
        print(f"{inp} alphabet is consonent")
else:
    print(f"{inp} is not a alphabet")
    

inp=int(input("enter the number:"))
if 100<=inp<=999:
    if inp%2==0:
        print(f"{inp} is even")
    else:
        print(f"{inp} is odd")
else:
    print(f" {inp} is a {len(str(inp))} digit number")
    

inp = input("enter the string:")
if inp[::] == inp[::-1]:
    print("the string is palindrome")
else:
    print("string is not palindrome")

#WAP to Check whether a person is eligible to vote and has a voter ID
age = int(input("enter your age:"))
if age >= 18:
    voter_id = input("do you have voter id (yes/no):")
    if voter_id == "yes":
        print("you are eligible to vote")
    else:
        print("you don't have voter_id")
else:
    print("you are not eligible to vote")

# WAP to ATM login using PIN and balance check.
name = input("enter your name:")
if name =="sanjan":
    password = int(input("enter your password:"))
    if password == 12345678:
        print("wellcome to your dashboard")

    else:
        print("password is incorrect")
else:
    print("your name is not registered") """

#


        



        
        
    


