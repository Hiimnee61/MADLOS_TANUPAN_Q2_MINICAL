a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Cannot Divide by Zero."
    else:
        return a / b

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    print("Result:", addition(a, b))
elif choice == '2':
    print("Result:", subtraction(a, b))
elif choice == '3':
    print("Result:", multiplication(a, b))
elif choice == '4':
    print("Result:", division(a, b))

    #Madlos - Helped with the choice and The Variables
    #Tanupan - Helped with the Functions and The Variables