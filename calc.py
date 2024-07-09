# Extended calculator example with more operations and error handling

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Division by zero is not allowed")

def main():
    print("Welcome to Extended Calculator!")
    print("Enter two numbers:")

    try:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return

    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")

    choice = input("\nEnter choice (1-6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'
            elif choice == '5':
                result = num1 // num2
                operation = '//'
            elif choice == '6':
                result = num1 % num2
                operation = '%'

            print(f"\n{num1} {operation} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Division by zero")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
