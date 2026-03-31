# Python Errors and Exception Handling
from io import TextIOWrapper

# Exception Handling using try, except, finally, else

try:
    # Executable Statements
    with open('a.txt', 'r') as file:
        content = file.read()
        print(content)

    a, b = 10, 0
    c = a / b
    print(c)
except ZeroDivisionError as ex:
    print(f"Zero Division Error: {ex}")
except FileNotFoundError as ex1:
    print(f"a.txt File not found: {ex1}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Else Block")
finally:
    file.close()
    print("This is Finally Block")



