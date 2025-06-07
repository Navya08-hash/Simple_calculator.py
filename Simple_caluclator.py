import Simple_caluclator
print("Addition")
print("Subraction")
print("Multiplication")
print("Division")
option = int(input("Choose the operation:"))
result = 0

if option in [1,2,3,4]:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    if option == 1:
        result = num1 + num2

    elif option == 2:
       result = num1 - num2 

    elif option == 3:
        result = num1 * num2

    elif option == 4 :
       result = num1 // num2

else:
    print("Invalid operation")

print("the result of the operation is {}".format(result))
