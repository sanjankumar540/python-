"""# WAP to print square of a number only if it is even
inp = int(input("enter the value"))
if inp%2 == 0:   
    print(inp**2)

# WAP  
inp = input("enter the character")
vowels = "AEIOUaeiou"
if inp in vowels :
    print("character is vowels")

inp = input("enter the character:")
if "A"<= inp <="Z":
    print(ord(inp)) 

inp = int (input("enter the value:"))
if inp%9==0 or inp%6==0:
    print(inp**3) 

inp = int(input("enter the value:"))
if 100<= inp <=999:
          print(f"{inp} is 3 digit number") 

inp = int(input("enter the value:"))
if inp%10==5:
    print(f"the last digit of {inp} is 5") 

inp = eval(input(" enter the value :"))
if type(inp) == float:
    print(f"{inp} is a float value")

inp = eval(input("enter the value:"))
if type(inp) in [int,float,complex,bool]:
           print(f"{inp} is a single valued datatype") 

inp = int(input("enter the value:"))
if type(inp) == int:
    print(f"{inp} in a digit")

inp = int(input('enter the value:'))
if inp%3==0:
    print(f"{inp} is a multiplte of 3") 

inp = eval(input("enter the value:"))
if type(inp) in [list,tuple,dict]:
    print(f"{inp} is a multi valued datatype")""" 


""" WAP to check whether a number is even or odd.
WAP to print the square of a number if it is even; otherwise print its cube.





WAP to check whether a number is a multiple of 10 or not.
WAP to check whether a character is a vowel or consonant.
WAP to check whether a character is uppercase or lowercase.
WAP to check whether a character is an alphabet or not.
WAP to check whether a character is a digit or not.
WAP to print the ASCII value of a character if it is uppercase; otherwise print "Not an Uppercase Letter".
WAP to check whether the entered string is in uppercase or not.
WAP to check whether the entered string is in lowercase or not.
WAP to check whether the entered string starts with a vowel or not.
WAP to check whether the entered string ends with a digit or not.
WAP to check whether the length of a string is even or odd.
WAP to check whether the entered data is of type int or not.
WAP to check whether the entered data is of type float or not.
WAP to check whether the entered data is of type str or not.
WAP to check whether the entered data is mutable or immutable.
WAP to check whether the entered data is a single-value data type or a collection data type.
WAP to check whether the entered list is empty or not.
WAP to check whether the entered tuple has more than 5 elements or not.
WAP to check whether the entered dictionary is empty or not.
WAP to check whether a person is eligible for voting based on age.
WAP to check whether the entered marks are pass or fail (Pass marks = 35)."""

"""inp = int(input("enter the number:"))
if inp%2 == 1:
          print(inp**2)
else:
    print("it is  a even number")

# WAP to check whether a number is positive or negative.
inp = int(input("enter the number"))
if inp >0:
    print(f"{inp} is positive")
else:
    print(f"{inp} is negative") )

# WAP to check whether a number is divisible by 5 or not.
inp = int(input("enter the number :"))
if inp%5==0:
    print(f"{inp} is divisible by 5")
else:
    print(f"{inp} is not divisible by 5")

# WAP to check whether a number is divisible by both 3 and 7; otherwise print "Not Divisible".
inp =int(input("enter the number:"))
if inp%3==0 and inp%7==0:
         print(f"{inp } is divisuble both 3 snd 7")
else:
    print("not divisible") 

# WAP to check whether the given number is a 2-digit number or not.
inp = int(input("enter the number:"))
if 10<= inp <= 99:
          print( "the number is two digit")
else:
    print("it is not two digit number")

# WAP to check whether the last digit of a number is 5 or not.
inp =int(input("enter the number:"))
if inp%10 ==5:
         print("the last number of the digit is 5:")
else:
    print("invalid")
    

# WAP to check the first digit of a number is 1
a =int(input("enter the number:"))
a = str(a)
if a[0]=='1':
    print("starts with 1")

#WAP Check whether a string ends with ".com"
inp = input("enter the string")
if inp.endswith(".com"):
    print("ends with .com")
    
    
# WAP Check whether a numeric password length is at least 8 characters
inp = int(input("enter your password"))
inp = str(inp)
if len(inp)>=8:
    print("the password is having atleast 8 character")

#Check whether a number is a perfect number ( the sum of multiples of the given number is equal to the number)
inp = int(input("enter the number:"))
if inp in [6,28,496,8128]:
    print("entered number is a perfect number")
else:
    print("not a perfect number")

#WAP Check whether a number is a happy number.(A happy number is a number that eventually becomes 1 when you repeatedly replace it with the sum of the squares of its digits.)
inp = int(input("enter the number"))

#WAP Check whether a number is a strong number.(add the factorials of the digits. If the sum equals the original number, it is a strong number.)


# WAP to perform the operation of mobile phone using the given below concepts variables ,data types, operators , control statements, loops ,functions , advance datatypes.
a =[]
def unlockphone():
    print("phone is unlocked")
    a.append("unlock phne")
def openinstagram(a):
    print("instagram is opened")
    a.append("instagram")
    b= int(input("1.stories 2.reels 3.chats:"))
    if b==1:
        print("instagram is opened")
    elif  b==2:
        print("viewing reels")
    elif b==3:
        print("viewing chats")
    else:
        print("close instagram")
unlockphone()
openinstagram(a)
print(a)

def openwhatsapp(b)
print("watsapp is opened")
a.append("watsapp")"""


# rock paper scissor game using if -else:

name = input("enter your name:")
print(f"wellcome {name} lets start the game")
user_choice = int(input("""
1.Rock
2.Paper
3.Scissor
"""))
import random
computer_choice = random.randint(1,3)
d = {
1:"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
2:
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
3:
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""}
if user_choice == computer_choice:
    print(f"DRAW.. your choice and computer choice is same that is {d[user_choice]}")
else:
    if user_choice == 1 and computer_choice == 3 :
        print(f"Bingoo! you won your choice is {d[user_choice]} and computer choice is {d[computer_choice]}")
    else:
        if user_choice == 2 and computer_choice == 1:
            print(f"Bingoo! you won your choice is {d[user_choice]} and computer choice is {d[computer_choice]}")
        else:
            if user_choice == 3 and computer_choice == 2:
                print(f"Bingoo! you won your choice is {d[user_choice]} and computer choice is {d[computer_choice]}")
            else:
                print(f"OOPS.... you lose your choice is {d[user_choice]} and computer choice is {d[computer_choice]}")




    
    
    
