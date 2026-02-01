# Write a Python program that simulates a basic command-line calculator support-
# ing multiple operations (addition, subtraction, multiplication, and division). The pro-
# gram should perform the following tasks:

# • Accept user inputs in the format: {operation num1 num2} (for example, add 5
# 3).
# • Support the following operations: add, sub, mul, div.
# • Provide an option to exit the program with the command exit.
# • Print the result of each calculation immediately after execution.
# Example Output:
# Enter operation (add/sub/mul/div) or ’exit’ to quit:
# add 5 3
# Result: 8
# div 10 0
# Error: Division by zero is not allowed.
# mul 4 6
# Result: 24
# exit
# Program terminated.

def calculator():
    print("Enter operation (add/sub/mul/div) or 'exit' to quit:")

    while True:
        user_input = input("> ").strip().lower()

        # Exit condition
        if user_input == "exit":
            print("Program terminated.")
            break

        # Split input into parts
        parts = user_input.split()

        # Validate input format
        if len(parts) != 3:
            print("Error: Invalid input format. Use {operation num1 num2}.")
            continue

        operation, num1_str, num2_str = parts

        # Validate numbers (without try/except)
        if not (num1_str.replace('.', '', 1).lstrip('-').isdigit() and 
                num2_str.replace('.', '', 1).lstrip('-').isdigit()):
            print("Error: Both operands must be valid numbers.")
            continue

        # Convert to float
        num1 = float(num1_str)
        num2 = float(num2_str)

        # Perform operation
        if operation == "add":
            result = num1 + num2
            print(f"Result: {result:g}")
        elif operation == "sub":
            result = num1 - num2
            print(f"Result: {result:g}")
        elif operation == "mul":
            result = num1 * num2
            print(f"Result: {result:g}")
        elif operation == "div":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {result:g}")
        else:
            print("Error: Unsupported operation. Use add, sub, mul, or div.")

# Run the calculator
if __name__ == "__main__":
    calculator()
