# calculator.py

# Req. 1: Variables & Types - The numbers will be stored in variables with correct data types
# Req. 3: Input Validation - Function to get and validate numeric input from the user

def get_numeric_input(prompt_message):
    """
    Prompts the user for input and continuously re-prompts until a valid
    numeric (integer or float) value is entered. Handles ValueError for
    non-numeric input.
    """
    while True: # Loop indefinitely until valid input is received
        user_input = input(prompt_message)
        try:
            # Try to convert input to a float first to handle both integers and decimals
            number = float(user_input)
            return number # If successful, return the number
        except ValueError:
            # If conversion fails, print an error and the loop continues
            print("Invalid input! Please enter a valid number (e.g., 5, 3.14).")

# Req. 2: Arithmetic Ops - Implement four arithmetic functions

def add(num1, num2):
    """Performs addition of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Performs subtraction of two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Performs multiplication of two numbers."""
    return num1 * num2

def divide(num1, num2):
    """
    Performs division of two numbers.
    Handles division by zero to prevent errors.
    """
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2

# Main part of the calculator program
if __name__ == "__main__":
    print("Welcome to the Simple Command-Line Calculator!")

    # Req. 1 & 3: Get the two numbers from the user with validation
    # The variables 'first_number' and 'second_number' will store either
    # int or float values based on the user's input.
    first_number = get_numeric_input("Enter the first number: ")
    second_number = get_numeric_input("Enter the second number: ")

    # Display the type of the variables for verification (for Req. 1 screenshot)
    print(f"\nDebug Info: First number type: {type(first_number)}")
    print(f"Debug Info: Second number type: {type(second_number)}")

    # Req. 2: Invoke each operation and print results clearly
    print("\n--- Results ---")

    # Addition
    sum_result = add(first_number, second_number)
    print(f"{first_number} + {second_number} = {sum_result}")

    # Subtraction
    difference_result = subtract(first_number, second_number)
    print(f"{first_number} - {second_number} = {difference_result}")

    # Multiplication
    product_result = multiply(first_number, second_number)
    print(f"{first_number} * {second_number} = {product_result}")

    # Division (with zero handling)
    division_result = divide(first_number, second_number)
    print(f"{first_number} / {second_number} = {division_result}")

    print("\nThank you for using the calculator!")
