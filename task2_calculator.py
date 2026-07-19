"""
TASK 2: CALCULATOR
--------------------
A simple command-line calculator that:
  1. Asks the user for two numbers
  2. Asks the user to choose an operation
  3. Performs the calculation
  4. Displays the result
  5. Lets the user repeat or exit
"""

 
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("===== SIMPLE CALCULATOR =====")
    operations = {
        "1": ("Addition (+)", add),
        "2": ("Subtraction (-)", subtract),
        "3": ("Multiplication (*)", multiply),
        "4": ("Division (/)", divide),
    }

    while True:
        print("\nChoose an operation:")
        for key, (label, _) in operations.items():
            print(f"{key}. {label}")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        label, func = operations[choice]
        result = func(num1, num2)
        print(f"Result: {num1} {label.split('(')[1].strip(')')} {num2} = {result}")


if __name__ == "__main__":
    main()
