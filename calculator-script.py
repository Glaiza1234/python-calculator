def calculator():
    while True:
        print("\nSimple Calculator")
        
        # Input Numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Choose Operation
        print("\nChoose Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        # Calculate Result
        if choice == '1':
            result = num1 + num2
            operation = "Addition"
        elif choice == '2':
            result = num1 - num2
            operation = "Subtraction"
        elif choice == '3':
            result = num1 * num2
            operation = "Multiplication"
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                operation = "Division"
            else:
                print("Error: Cannot divide by zero")
                continue
        else:
            print("Invalid input")
            continue
        
        # Display Result
        print(f"\n{operation} Result: {result}")
        
        # Ask to continue or exit
        again = input("\nDo you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
