#1 display a menu to user
def display_menu():
    print("Menu Options:")
    print("1. Yes/ no Test")
    print("2. Compare 2 numbers")
    print("3. Work with Text")
    print("4. Exit")

#2 Loop until user chooses to exit
running: bool = True

while running:
    #3 Prompt user for input
    display_menu()
    choice: str = input("Enter your choice (1-4):  ").strip()

    #4 Validate user input and call the appropriate function
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid selection. Please enter a number between 1-4.")
        continue

    option: int = int(choice)

    #5 Execute the appropriate function based on user input
    if option == 1:
        answer = input("Are Cats little goobers? (yes/no): ").strip().lower()
        if answer == "yes":
            print("Glad you agree!")
        elif answer == "no":
            print("You're wrong, but i respect your opinion")
        else:
            print("Please answer yes or no.")
    elif option == 2:
        print("Compare 2 numbers selected.")
    elif option == 3:
        print("Work with Text selected.")
    elif option == 4:
        #6 Exit the program if user chooses to exit
        print("Exiting the program. Goodbye!")
        running = False

