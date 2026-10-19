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
def getValues(a, b):
    f_num= a
    s_num= b
    return f_num, s_num

f_input, s_input= getValues(a, b)
    
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

print(f"First number is {f_input}")
print(f"Second number is {s_input}")

# Madlos - Helped with the choices, variables, and input of numbers.
# Tanupan - Helped with the functions, return statements, and displaying the results.
