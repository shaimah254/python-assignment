def basic_calculator():
    try:
        # Ask the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Ask the user for the operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the operation and display the result
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    basic_calculator()
