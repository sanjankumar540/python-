#specific exception handling
"""try:
    a="abc"
    b=10
    print(a+b)
    print(100/0)

except TypeError:
    print("concatination not supported bw int and str")
except ZeroDivisionError:
    print("number cannot be divide by 0")

try :
    print(10+100)
    print('a'+'b')
    print(100/10)

except:
    print("division is not posiible when denomenator is zero")

else:
    print("no exception found")

finally:
    print("program completed")  """

try:
    print(10/0)
    print('a'+1)

except Exception:
    print("int cant be divided by zer0")
