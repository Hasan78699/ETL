print("select an operation to perform: ")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. division")

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

else:
    print("Invalid Entry")    
