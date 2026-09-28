"""name = input("enter your name:")
marks = int(input("enter your marks:"))
if marks >= 85:
    print(f"{name} got distinction")
elif 75<=marks<=84:
    print(f"{name} got A grade")
elif 65<=marks<=74:
    print(f"{name} got B grade")
elif 45<=marks<=64:
    print(f"{name} got C grade")
elif 35<=marks<=44:
    print(f"{name} just passed")
else:
    print("failed")

name1 = input("enter name1: ")
age1 = int(input("enter age1:"))
name2 = input(" enter name2:")
age2 = int(input("enter age2:"))
name3 = input("enter name3:")
age3 = int(input("enter age3:"))

if age1 >age2 and age1>age3:
    print(f"{name1} is elder")
elif age2>age1 and age2>age3:
    print(f"{name2} is elder")
elif age3>age1 and age3>age2:
    print(f"{name3} is elder")
else:
    print("invalid")

# simple calculator
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
op = input("enter the arithmatic operation symbol :")
if op == "+":
    print(f"the sum of {a} and {b} is {a+b}")
elif op == "-":
    print(f"the difference of {a} and {b} is {a-b}")
elif op =="/":
    print(f"the divison of {a} by {b} is {a/b}")
elif op =="*":
    print(f" the product of {a} and {b} is {a*b}")
elif op == "%":
    print(f" the remainder after dividing {a} by {b} is {a%b}")
elif op =="//":
    print(f" the floor division of {a} by {b} is {a//b}")
else:
    print("the arithmatic operator is invalid")



inp = int(input("enter the number"))
if inp%3==0 and inp%5==0:
    print(f"{inp} is divisible by both 3 and 5")
elif inp%3==0 and inp%5!=0:
    print(f"{inp} is noly divisible by 3")
elif inp%3!=0 and inp%5==0:
    print(f"{inp} is only divisible by 5")
else:
    print(f"{inp} is not divisible by both 3 and 5") 

a = int(input("enter marks in subject 1:"))
b = int(input("enter marks in subject 2:"))
c = int(input("enter marks in subject 3:"))
avg = (a+b+c)//3
if avg>=85:
    print("distinction")
elif 75<=avg<=84:
    print("A grade")
elif 65<=avg<=74:
    print("B garde")
elif 55<=avg<=64:
    print("c garde")
else:
    print("just pass")

a = input("enter the character:")
if 'A' <=a<= 'Z':
    print("character is uppercase")
elif 'a' <=a<= 'z':
    print("character is lowercase")
elif a.isdigit():
    print("it is a digit")
else:
    print("it is a special character")

age = int(input("enter your age:"))
if 0<=age<=4:
    print("you are a kid")
elif 5<=age<=12:
    print("you are child")
elif 13<=age<=19:
    print("you are teenager")
elif 20<=age<=59:
    print("you are adult")
elif 60<=age<=100:
    print("you are seniour citizen")
else:
    print("invalid age")

inp = int(input("enter the number:"))
if -9<=inp<=9:
    print("single digit")
elif -99 <=inp<=99:
    print("double digit")
elif -999 <=inp<=999:
    print("thriple digit")
else:
    print("more than three digit")


import random
a = input("enter your name:")
b = input("enter your crush name:")
lp = random.randint(35,100)
print(f"your love percentage if {lp}")
if lp>=90:
    print("your love is very strong and made for each other get married soon")
elif 70<=lp<=89:
    print("your love is good continue further")
elif 50<=lp<=69:
    print("your love is average")
elif  35<=lp<=50:
    print("your love is poor")
else:
    print("love failure")
    

age = int(input("enter your age:"))
if age<5 :
    print("your ticket price is 50 rupees")
elif age<=17:
    print("your ticket price is 70 rupees")
elif age<=59:
    print("your ticket price is 150 rupees")
elif age>=60:
    print("your ticket price is 100 rupees (discount for seniour citizen)")


a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = input("enter your arithmatic operator")
if c=="+" :
    print(f"the sum of {a} and {b} is {a+b}")
elif c == "-":
    print(f"the difference of {a} and {b} is {a-b}")
elif c == "*":
    print(f"the product of {a} and {b} is {a*b}")
elif c== "/":
    print(f"the division of {a} by {b} is {a/b}")
elif c=="//":
    print(f"the floor division of {a} by {b} is {a//b}")
elif c=="%":
    print(f"the remainder after dividing {a} by {b} is {a%b}")
else:
    print("the operator is invalid")

age = int(input("enter your age:"))
if age<=5 :
    print("your ticket price is 50 rupees")
elif age<=17:
    print("your ticket price is 70 rupees")
elif age<=59:
    print("your ticket price is 150 rupees")
elif age>=60:
    print("your ticket price is 100 rupees (discount for seniour citizen)")"""

user_name = input("enter your name:")
print(f" wellcome {user_name} lets start the game")
import random
computer_choice = random.randint(1,3)
user_choice =int(input("""
1.rock
2.paper
3.scissor"""))
d={
1:"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
2:"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
3:"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""}
if computer_choice == user_choice:
    print(f"your choice and computer choice is same that is {d[user_choice]}")
elif   user_choice ==2 and computer_choice == 1  :
    print(f"BINGOO! {user_name} you won your choice is {d[user_choice]} and computer choice is {d[computer_choice]}")
elif   user_choice ==3 and computer_choice == 1:
    print(f"BINGOO! {user_name} you won your choice is {d[user_choice]} and computer choice is {d[computer_choice]}")
elif   user_choice ==1 and computer_choice == 3:
    print(f"BINGOO! {user_name} you won your choice is {d[user_choice]} and computer choice is {d[computer_choice]}")
else:
    print(f"OOPS {user_name} you lost your choice is {d[user_choice]} and computer choice is {d[computer_choice]}")




    
    
    

    
    
    




























