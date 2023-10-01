import re

def perform_complex_math():
    print("Enter your equation. Use the following symbols:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    print("** for exponentiation")
    print("() for grouping")
    
    equation = input("Your equation: ")

    # Sanitize the input to only allow numbers and arithmetic operations
    if not re.match("^[0-9+\-*/().\s]*$", equation):
        return "Invalid characters in equation."
    
    try:
        result = eval(equation)
        return f"The result is: {result}"
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"An error occurred: {e}"

# Main Program Loop
#while True:
#    command = input("Math Assistant: How may I assist you with your calculations? Type 'exit' to quit. ")
#    if command.lower() == 'exit':
#        break
#    response = perform_complex_math()
#    if response:
#        print(response)
