import math
import sys

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("Type 'help' to see available commands or 'exit' to quit.\n")
    
    variables = {}
    history = []
    
    while True:
        try:
            user_input = input(">>> ").strip()
            
            if user_input.lower() == 'exit':
                print("Thank you for using the calculator. Goodbye!")
                break
            elif user_input.lower() == 'help':
                print_help()
                continue
            elif user_input.lower() == 'history':
                print_history(history)
                continue
            elif user_input.lower() == 'clear':
                history.clear()
                print("History cleared.")
                continue
            elif '=' in user_input:
                var_name, expression = user_input.split('=', 1)
                var_name = var_name.strip()
                expression = expression.strip()
                if not var_name.isidentifier():
                    print("Invalid variable name.")
                    continue
                result = evaluate_expression(expression, variables)
                if result is not None:
                    variables[var_name] = result
                    history.append(f"{var_name} = {result}")
                    print(f"{var_name} = {result}")
                continue
            else:
                result = evaluate_expression(user_input, variables)
                if result is not None:
                    history.append(f"{user_input} = {result}")
                    print(result)
                continue
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled by user. Exiting.")
            break

def evaluate_expression(expression, variables):
    try:
        # Replace variables in the expression with their values
        for var in variables:
            expression = expression.replace(var, str(variables[var]))
        
        # Safe evaluation of the expression
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names.update(variables)
        allowed_names['abs'] = abs
        allowed_names['round'] = round

        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def print_help():
    help_text = """
Available commands:
- Basic arithmetic operations: +, -, *, /, %, ** (exponentiation)
- Advanced functions: sin(x), cos(x), tan(x), log(x), log10(x), sqrt(x), factorial(x)
- Constants: pi, e
- Variables: You can assign values to variables (e.g., x = 10)
- Use variables in expressions (e.g., x + 5)
- Commands:
    - help: Show this help message
    - history: Show calculation history
    - clear: Clear calculation history
    - exit: Exit the calculator
Examples:
- 2 + 3 * 4
- sin(pi / 2)
- x = 10
- x ** 2
"""
    print(help_text)

def print_history(history):
    if history:
        print("Calculation History:")
        for item in history:
            print(item)
    else:
        print("History is empty.")

if __name__ == "__main__":
    calculator()
