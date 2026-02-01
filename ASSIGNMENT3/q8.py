# Write a Python script that takes several numbers as command-line arguments and
# prints their sum.
# • Use sys.argv to access the numbers from the command line.
# • Ensure the script ignores the filename while calculating the sum.
# • Display a clear error message if any argument is not a valid number.
# • Show a sample command-line usage and the expected output.
# Example Output:
# Command:
# python sumargs.py 10 20 30 40
# Output:
# Sum of numbers: 100
# Command:
# python sumargs.py 10 20 abc 30
# Error: Invalid input ’abc’. Please enter only numbers.

import sys

def is_number(s):
    # Check if the string can represent a valid number (integer or float)
    if s.count('.') <= 1 and (s.replace('.', '', 1).lstrip('-').isdigit()):
        return True
    return False

def main():
    args = sys.argv[1:]  # Ignore the script name

    if not args:
        print("Usage: python sumargs.py <num1> <num2> <num3> ...")
        return

    total = 0.0

    for arg in args:
        if is_number(arg):
            total += float(arg)
        else:
            print(f"Error: Invalid input '{arg}'. Please enter only numbers.")
            return

    # Print result
    print(f"Sum of numbers: {total:g}")

if __name__ == "__main__":
    main()
