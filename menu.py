def main():
    while True:
        print_main_menu()
        main_choice = input("Enter your choice: ")
        if main_choice == "1":
            sub_menu("1")
        elif main_choice == "2":
            sub_menu("2")
        elif main_choice == "3":
            sub_menu("3")
        elif main_choice == "4":
            sub_menu("4")
        elif main_choice == "5":
            sub_menu("5")
        else:
            print("Invalid choice. Please try again.")

def print_main_menu():
    print("\nMain Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")

def sub_menu(main_choice):
    while True:
        print_sub_menu(main_choice)
        sub_choice = input("Enter your choice (or 'b' to go back): ")
        if sub_choice == "1":
            print(f"You selected sub-option 1 of main option {main_choice}")
        elif sub_choice == "2":
            print(f"You selected sub-option 2 of main option {main_choice}")
        elif sub_choice == "3":
            print(f"You selected sub-option 3 of main option {main_choice}")
        elif sub_choice.lower() == 'b':
            break
        else:
            print("Invalid choice. Please try again.")

def print_sub_menu(main_choice):
    print(f"\nSub-Menu for Main Option {main_choice}:")
    print("1. Sub-Option 1")
    print("2. Sub-Option 2")
    print("3. Sub-Option 3")

if __name__ == "__main__":
    main()