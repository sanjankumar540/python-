 #1. Student Name Formatter: Input a student's full name. Remove extra spaces. Convert it to title case. Count the number of words how to do this
"""a = input("Enter your name:")    
a = a.strip()
a = a.title()
b = a.split()
count = len(b)
print(b)
print("formatted name",a)
print("length of words",count)"""

#2. Email Validator: Input an email. Convert it to lowercase. Check if it ends with .com.
'''email = input("enter your email:")  
email = email.lower()
print("your email is",email)
if email.endswith(".com"):
    print("email is valid")
else:
    print("email is invalid")'''

 #3. Username Checker Input a username. Remove spaces. Check if it is alphanumeric. If valid, convert it to uppercase.
'''user = input("enter user name:")
user = user.strip()
if user.isalnum():
    print("formatted user name is",user.upper())
else:
    print("user name is invalid")'''

# 4. Sentence Analyzer : Input a sentence.  Print:Number of words ,Number of 'a' ,Number of 'e' ,First word  ,Last word
'''sent = ("you dont have to be great to start but you have to start to great")
words = sent.split()
print(words)
count = len(words)
print("number of words in above sentence is ", count)
print("the presence of letter 'e' in the above sentence is", sent.count("e"))
print("the presence of letter 'a' in the above sentence is", sent.count("a"))
print("the presence of letter 'g' in the above sentence is", sent.count("g"))
print("the first word of the sentence is " ,words[0])
print("the last word of the sentence is ",words[-1])'''

# 5.Input a password and check:Does it contain only letters? Does it contain only digits? Is it alphanumeric (letters and/or digits only)? Convert the password using swapcase().
'''password = input("enter your password :")
print("alphabetic" , password.isalpha())
print("only digits" , password.isdigit())
print("alphanumeric" , password.isalnum())
print(password.swapcase())'''

#6. File Name Converter: Input a filename.Convert to lowercase. Replace spaces with _.Check whether it ends with .jpg.If yes, change it to .png.
'''filename = input("enter your filename:")
filename = filename.lower()
print(filename)
filename = filename.replace(" " ,"_")
print(filename)
if(filename.endswith("jpg") ):
    print(filename.replace("jpg","png"))
else:
    print("condition is not satisfied")'''

#7 Write a Python program that performs the following operations: Accept a sentence from the user.Convert the sentence to Title Case. Split the sentence into individual words. Print the
#words in reverse order.
"""sentence = input("enter your sentence:")
sentence = sentence.title()
words = sentence.split()
print(words)
print(words[-1::-1])"""

#8  
a = "abc123xyz"
a= a.upper()
part1 = a[0:3]
part2 = a[3:6]
part3 = a[6::]
a = part1 + "-" + part2 + "-" +part3
print(a)
