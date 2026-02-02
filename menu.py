def display_menu():
    """
    Displays the calculator menu with 6 options.
    """
    print("-" * 20)
    print(" Calculator Menu")
    print("-" * 20)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Area of a circle")
    print("7. Area of a rectangle")
    print("8. Perimeter of a rectangle")
    print("9. Exit")
    print("-" * 20)

def get_choice():
    """
    Prompts the user for a choice and validates it is between 1 and 9.
    Returns the valid choice as an integer.
    """
    valid_input = False
    choice = 0
    while not valid_input:
        user_input = input("Enter your choice (1-9): ")
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= 9:
                valid_input = True
            else:
                print("Error: Please select a number between 1 and 9.")
        else:
            print("Error: Invalid input. Please enter a number.")
    return choice
