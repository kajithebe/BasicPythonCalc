import Art
print(Art.logo)


def addition(first, second):
    return first + second


def subtraction(first, second):
    return first - second


def multiplication(first, second):
    return first * second


def division(first, second):
    if second == 0:
        return "Error: Division by zero is undefined"
    return first / second


operations = {"+": addition, "-": subtraction, "*": multiplication, "/": division}


def calculator():
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    is_calculation_end = False
    while not is_calculation_end:
        operator = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        operation_function = operations[operator]
        result = operation_function(first_number, next_number)
        print(f"{first_number} {operator} {next_number} = {result}")
        repeat_calculation = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new "
                                   f"calculation: ").lower()
        if repeat_calculation == "y":
            first_number = result
        else:
            is_calculation_end = True
            calculator()


calculator()
