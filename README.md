# MyDailyWork – Task 2: Calculator

A simple command-line calculator developed in Python as part of my **MyDailyWork Python Programming Internship**.

## Project Overview

The calculator accepts two numbers, lets the user choose an arithmetic operation, displays the result, and allows the user to perform additional calculations until they choose to exit.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Repeated calculations in one session
- Numeric input validation
- Invalid menu-choice handling
- Division-by-zero protection

## Technologies Used

- Python 3
- Python standard library only

## Project File

```text
task2_calculator.py
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python task2_calculator.py
```

On some systems, use:

```bash
python3 task2_calculator.py
```

No third-party Python packages are required.

## Example Flow

```text
===== SIMPLE CALCULATOR =====

Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
```

Example calculation:

```text
Enter first number: 10
Enter second number: 5
Result: 10.0 + 5.0 = 15.0
```

For division by zero, the program reports:

```text
Error: Division by zero is not allowed.
```

## Error Handling

The program keeps asking until the user enters a valid numeric value and rejects invalid menu choices. Division by zero is handled without crashing the program.

## Internship Project

**Internship:** MyDailyWork – Python Programming Internship  
**Task:** Task 2 – Calculator

## Status

✅ Completed
