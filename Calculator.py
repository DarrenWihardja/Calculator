import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponentiate(x, y):
    return x ** y

def modulo(x, y):
    return x % y

def floor_divide(x, y):
    return x // y

def square_root(x):
    return math.sqrt(x)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Available operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Modulo")
print("7. Floor Division")
print("8. Square Root")

choice = int(input("Enter the operation number (1-8): "))

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)
elif choice == 5:
    result = exponentiate(num1, num2)
elif choice == 6:
    result = modulo(num1, num2)
elif choice == 7:
    result = floor_divide(num1, num2)
elif choice == 8:
    result = square_root(num1) if num2 == 1 else square_root(num2)
else:
    print("Invalid choice!")
    exit()

print("Result:", result)