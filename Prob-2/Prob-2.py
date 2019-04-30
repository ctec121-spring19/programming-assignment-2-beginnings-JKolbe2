# Module 2
#   Programming Assignment 2
#     Prob-2.py

# Jeremy Kolbe

# Follow the steps below. Add your code in the blank line after each comment

# define the main function with no parameters

    # create a variable and assign it the value returned by an input function
    # that asks the user for a number. Don't forget to use the int() function.

    # print out a message that says: "The sqare of ? is ?" where the question
    # marks are replaced with the value read in from the user and its square.

    # copy your input statement from above and replace "int" with "float"

    # copy the print statment from above

    # copy your input statement from above and replace "int" with "eval"

    # copy the print statment from above

# call the function main

def main(): 
    number = int(input("Enter a number: "))
    squared = number * number
    print("The square of", number, "is", squared)
    number1 = float(input("Enter a number: "))
    squared1 = number1 * number1
    print("The square of", number1, "is", squared1)
    number2 = eval(input("Enter a number: "))
    squared2 = number2 * number2
    print("The square of", number2, "is", squared2)



main()