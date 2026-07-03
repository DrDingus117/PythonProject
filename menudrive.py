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
    choice: str = input("Enter your choice (1-4): ").strip()

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
            print("You're wrong, but I respect your opinion.")
        else:
            print("Please answer yes or no.")

    elif option == 2:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            first_is_bigger = num1 > num2

            if num1 > num2:
                print(num1, "is greater than", num2)
            elif num1 < num2:
                print(num2, "is greater than", num1)
            else:
                print("The numbers are equal.")

            print("Is the first number greater?", first_is_bigger)

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif option == 3:
        text = input("Enter some text: ").strip()

        if text == "":
            print("You didn't enter any text.")
        else:
            print("Uppercase:", text.upper())

            if text.lower() == "python":
                print("You typed Python!")
            else:
                print("You entered:", text)

    elif option == 4:
        #6 Exit the program if user chooses to exit
        print("Exiting the program. Goodbye!")
        running = False