def display_menu():
    print("Please choose an option from the menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

def main():
    while True:
        display_menu()
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            print("You chose Option 1.")
        elif user_choice == "2":
            print("You chose Option 2.")
        elif user_choice == "3":
            print("You chose Option 3.")
        elif user_choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()