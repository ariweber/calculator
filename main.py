import menu
import operations

def main():
    running = True
    while running:
        menu.display_menu()
        choice = menu.get_choice()

        if choice == 6:
            print("Exiting calculator. Goodbye!")
            running = False
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
            continue

        result = None
        if choice == 1:
            result = operations.add(num1, num2)
        elif choice == 2:
            result = operations.sub(num1, num2)
        elif choice == 3:
            result = operations.multiply(num1, num2)
        elif choice == 4:
            if num2 == 0:
                print("Error: Cannot divide by zero")
                continue
            result = operations.divide(num1, num2)
        elif choice == 5:
            result = operations.power(num1, num2)

        print(f"Result: {result}")
        print("-" * 20)

if __name__ == "__main__":
    main()
