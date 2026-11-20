def divide_numbers(a, b):
    try:
        # Attempt the division
        result = a / b
    except ZeroDivisionError:
        # Runs if b is 0
        print(f"Error: Cannot divide {a} by zero.")
    except TypeError:
        # Runs if a or b is not a number
        print(f"Error: Invalid input types ({type(a).__name__}, {type(b).__name__}). Use numbers only.")
    else:
        # Runs only if the try block succeeded
        print(f"Success: {a} / {b} = {result}")
    finally:
        # Always runs at the end
        print("--- Operation complete ---\n")

# Main execution block
if __name__ == "__main__":
    print("Test 1: Valid division")
    divide_numbers(10, 2)

    print("Test 2: Division by zero")
    divide_numbers(10, 0)

    print("Test 3: Invalid data type")
    divide_numbers(10, "five")
