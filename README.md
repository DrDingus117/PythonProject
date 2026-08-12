## How to run each App: Press the Play (sideways triangle) to start.

Calculator: Allows you to Add, Subtract, Multiply, and Divide (unless it's by Zero, cause it'll tell you that's impossible). 

Greeter: Simple greeting tool, where you can input a name (examples Marcus, Milton, Eyerok (from Mario 64), just any name you want). Press enter, it shows the name.

Menu: 1: Asks a yes or no question, 2: Put in two numbers, it'll tell you if it's greater, 3: Put in any text you want, 4: Exit

Fizzbuzz: Inpur a number between 1 to 10, if a number matches what's in the code it'll say "Fizz" and "Buzz"

Number Guess: Put in a number between 1 and 10, if right you win, but if wrong it'll tell you "Too High!" and "Too Low!"

Vowel Game: Spell a word with A, E, I, O, or U, you win, if you put in any other letter though it'll list what is and isn't a vowel.

Paragraph Game: Counts the total words and word length 

Frequency analysis: Edit the list to have as many items as you need, save, press the start button, and it'll show what you have.

## Finals

Student Record Manager

## Menu Options

**1. Add Student**
Prompts the user to enter a student's ID, name, age, major, and GPA.
Creates a new student record and stores it in the program.

**2. View Students**
 Displays all student records currently stored in the program.

**3. Search Student**
 Searches for a student by their student ID and displays their information if found.

**4. Update Student**
 Allows the user to modify an existing student's name, major, or GPA by entering their student ID.

**5. Delete Student**
 Removes a student record from the program using the student's ID.

**6. Save Students**
 Saves all current student records to `students.txt` so they can be used again later.

**7. Load Students**
 Loads student records from `students.txt` into the program.

**8. Exit**
 Closes the program.

 ## Issues i ran into
VS Code trying to fight me

extra spaces before def edit_student():

no code underneath if student.student_id == student_id: to change info

if someone puts twenty three instead of 23 it would crash. Added validation

If there were no students, it would show a blank list.