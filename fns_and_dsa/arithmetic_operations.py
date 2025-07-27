def perform_operation(num1, num2):

    num1 = float(num1)
    num2 = float(num2)
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2

    if num2 == 0:
        divide = "Error cannot divide by zero"

    else:
        divide = num1 / num2

    operation = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
        }

    return operation
