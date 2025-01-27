print("select an operation to perform: ")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. division")
print("5.factorial")
operation = input()
if operation == "1":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("Addition = " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("Subtraction = " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("Multiplication =" + str(int(num1) * int(num2)))


elif operation == "4":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("Division = " + str(int(num1) / int(num2)))

elif operation == "5":
    number = int(input("Enter the non negetive integer: "))
    number >= 0
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
        print(f"the factorial of {number} is {factorial}.")
    else:
        print("factorial is not defined for negetive numbers.")    



else:
    print("Invalid Entry")    
