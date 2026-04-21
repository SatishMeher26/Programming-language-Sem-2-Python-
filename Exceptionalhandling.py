# exception handling examples in one file

# 1 basic try except
try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(a / b)
except:
    print("error")

# 2 specific exceptions
try:
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    print(x / y)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input")

# 3 else block
try:
    m = int(input("enter m: "))
    n = int(input("enter n: "))
    r = m / n
except ZeroDivisionError:
    print("zero division")
else:
    print(r)

# 4 finally block
try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("file not found")
finally:
    print("done")

# 5 raise exception
try:
    age = int(input("enter age: "))
    if age < 18:
        raise Exception("not allowed")
    print("allowed")
except Exception as e:
    print(e)

# 6 custom exception
class MyError(Exception):
    pass

try:
    num = int(input("enter number: "))
    if num < 0:
        raise MyError("negative not allowed")
    print(num)
except MyError as e:
    print(e)
except ValueError:
    print("invalid")