def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handle division by zero
    if y == 0:
        return "❌ Cannot divide by zero"
    return x / y

def calculator():
    print("🧮 Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("⚠️ Invalid input")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("⚠️ Please enter valid numbers.")
        return

    if choice == '1':
        result = add(num1, num2)
        op = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        op = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        op = '*'
    elif choice == '4':
        result = divide(num1, num2)
        op = '/'

    print(f"\n✅ Result: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    while True:
        calculator()
        again = input("\nDo you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thank you for using the calculator!")
            break
