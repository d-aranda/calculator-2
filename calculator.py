"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    expression_input = input("Enter an expression: ")
    tokens = expression_input.split(" ")

    if tokens[0] == "q":
        print("quitting...")
        break

    




