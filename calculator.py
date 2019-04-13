# calculator with functions

while 1 == 1:  # to make sure that the program runs until the user doesn't choose to quit
    print("options:")
    print("Type 'add' for the addition of two numbers")
    print("Type 'multiply' for the multiplication of two numbers")
    print("Type 'subtract' for the subtraction of two numbers")
    print("Type 'divide' for the division of two numbers")
    print("Type 'modulo' for the remainder by division of two numbers")
    print("Type 'floor' for the non-decimal value by division of two numbers")
    print("Type 'quit' to end the program")


    def add(num, num_1):   # addition function
        num = float(input("Enter a integer: "))
        num_1 = float(input("Enter another integer: "))
        result = str(num + num_1)
        print("The result is ", result)


    def multiply(num, num_1):   # multiplication function
        num = float(input("Enter a number: "))
        num_1 = float(input("Enter another number"))
        result = str(num * num_1)
        print("The result is ", result)


    def subtract(num, num_1):   # subtraction function
        num = float(input("Enter a number: "))
        num_1 = float(input("Enter another number: "))
        result = str(num - num_1)
        print("The result is ", result)


    def divide(num, num_1):   # division function
        num = float(input("Enter a number: "))
        num_1 = float(input("Enter another number: "))
        try:
            result = str(num / num_1)
            print("The result is ", result)
        except:
            print("Division by zero, can't divide a number by zero!!")


    def modulo(num, num_1):   # modulus function
        num = int(input("Enter a number: "))
        num_1 = int(input("Enter another number: "))
        try:
            result = str(num % num_1)
            print("The result is ", result)
        except:
            print("Division by zero, can't find a modulo when divided by zero!!")


    def floor(num, num_1):   # floor function
        num = int(input("Enter a number: "))
        num_1 = int(input("Enter another number: "))
        try:
            result = str(num // num_1)
            print("The result is ", result)
        except:
            print("Division by zero, can't find a floor when divided by zero")


    user_input = input(": ")
    if user_input == "quit":
        exit()
    elif user_input == "add":
        add(num=1, num_1=2)
    elif user_input == "multiply":
        multiply(num=1, num_1=2)
    elif user_input == "subtract":
        subtract(num=1, num_1=2)
    elif user_input == "divide":
        divide(num=1, num_1=2)
    elif user_input == "modulo":
        modulo(num=1, num_1=2)
    elif user_input == "floor":
        floor(num=1, num_1=2)
    else:
        print("Unknown input!!")

# program ends!!
