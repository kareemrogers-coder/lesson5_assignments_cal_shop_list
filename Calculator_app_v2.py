# Question1

""" The Calculator App


Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.


Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation. 
Task 2: Implement user input to receive numbers and an operation choice, their response for operation should call the associated function 
Task 3: Ensure your program can handle division by zero and other potential errors. """

def addition():
    a = float(input("enter first number "))
    b = float(input("enter second number "))
    print("{} + {} = {}".format(a, b, round(a+b)))

def subtraction():
    a = float(input("enter first number "))
    b = float(input("enter second number "))
    print("{} - {} = {}".format(a, b, round(a-b)))

def division():
    a = float(input("enter first number "))
    b = float(input("enter second number "))
    answer = a/b if b != 0 else 0
    print(f"{a}/{b} = {answer}")

def multiplication():
    a = float(input("enter first number "))
    b = float(input("enter second number "))
    print("{}*{} = {}".format(a, b, round(a*b)))


def main():
    flag = True
    while flag:
        ans = input('''
Welcome to the Calculator application, to begin select you arithmetic operation.
1 - For addition
2 - For subtraction
3 - For Division
4 - For Multiplication
5 - To quit application
''')
        if ans == "1":
            addition()
           
        elif ans == "2":
           subtraction()

        elif ans == "3":
            division()

        elif ans == "4":
           multiplication()

        elif ans == "5":
            flag = False
            print("Application closing, good bye")

        else:
            print("Invalid selection, Please between 1,2,3,4 or 5")
            
main()