# author: sanjeet
# calculator with functions

import math  # math module

def _sum(x, y):   # addition funcition
    return x + y
def subtract(x, y):   # subtraction function
    return x - y
def multiply(x, y):   # multiplication function
    return x * y
def divide(x, y):   # division function
    return x / y
def floor_divide(x, y):   # floor division function
    return x // y
def modulus(x, y):   # modulus function
    return x % y
def square(x):   # square function
    return x * x
def square_root(x):   # square_root function
    return math.sqrt(x)
def power(x, y):   # power function
    return x ** y

def main():   # main function of the program
    print('Calculator')
    print('1. Sum')
    print('2. Subtract')
    print('3. Multiplication')
    print('4. Division')
    print('5. Floor Division')
    print('6. Modulus')
    print('7. Square')
    print('8. Square Root')
    print('9. Power')
    print('10. Exit')
    while True:   # to make sure it continues till the user doesn't quit
        choice = int(input('Enter your choice: '))
        if choice == 1:
            num1 = float(input('Enter a number: '))
            num2 = float(input('Enter another number: '))
            print('Result is', _sum(num1, num2))
        elif choice == 2:
            num1 = float(input('Enter a number: '))
            num2 = float(input('Enter another number: '))
            print('Result is', subtract(num1, num2))
        elif choice == 3:
            num1 = float(input('Enter a number: '))
            num2 = float(input('Enter another number: '))
            print('Result is', multiply(num1, num2))
        elif choice == 4:
            num1 = float(input('Enter a number: '))
            num2 = float(input('Enter another number: '))
            try:
                result = divide(num1, num2)
                print('Result is', result)
            except:
                print("Divide by zero error! Can't divide a number by zero")
        elif choice == 5:
            num1 = float(input('Enter a number: '))
            num2 = float(input('Enter another number: '))
            try:
                result = floor_divide(num1, num2)
                print('Result is', result)
            except:
                print("Divide by zero error! Can't divide a number by zero")
        elif choice == 6:
            num1 = float(input('Enter a number: '))
            num2 = float(input('Enter another number: '))
            try:
                result = modulus(num1, num2)
                print('Result is', result)
            except:
                print("Divide by zero error! Can't divide a number by zero")
        elif choice == 7:
            num1 = float(input('Enter a number: '))
            print('Result is', square(num1))
        elif choice == 8:
            num1 = float(input('Enter a number: '))
            print('Result is', square_root(num1))
        elif choice == 9:
            num1 = float(input('Enter a number: '))
            num2 = float(input('Enter another number: '))
            print('Result is', power(num1, num2))
        elif choice == 10:
            print('Thank you!')
            break
        else:
            print('Enter correct choice')
            
if __name__ == '__main__':   # calling the main function
    main()
