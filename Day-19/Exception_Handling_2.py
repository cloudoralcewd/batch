while True:
    try:
        a = int(input("Enter a Number Value"))
        b = int(input("Enter b Number Value"))
        c = a / b
    except ValueError as e:
        print(f"Value error occurred: {e}. Please enter valid integers.")
    except ZeroDivisionError as zde:
        print(f"Zero division error occurred: {zde}. 'b' cannot be zero. Please enter a non-zero integer for 'b'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")
    else:
        print(f"The result of {a} divided by {b} is: {c}")
        break
    finally:
        print("Attempt to perform division operation is complete.")

try:
    age = -2
    if age < 0:
        raise Exception("Age can not be Negative")
    elif age < 18:
        print("Minor")
    else:
        print("Major")
except Exception as e:
    print(e)