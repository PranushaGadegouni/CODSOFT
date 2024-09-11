Simple Calculator with Tkinter:-

This is a basic calculator application built using Python's Tkinter library. It provides a simple GUI for performing arithmetic operations.

Features:
* Arithmetic Operations: Supports addition, subtraction, multiplication, and division.
* Clear Functionality: Allows users to reset the input.
* Error Handling: Displays an error message if the expression is invalid.

Usage:
1) Running the Application:
* Ensure you have Python and Tkinter installed on your system.
* Run the script using Python. The GUI window will open with the calculator interface.
2) Using the Calculator:
* Click on the numeric buttons (0-9) and operator buttons (+, -, *, /) to input numbers and perform operations.
* Press the = button to calculate the result.
* Press the C button to clear the current input.

Code Overview:
* press(num): Updates the expression shown in the input field with the clicked button's value.
* equal_press(): Evaluates the current expression and displays the result.
* clear(): Clears the current expression from the input field.
* GUI Layout: Utilizes Tkinter to create a grid of buttons and an entry field for user interaction.

Requirements:
* Python 3.x
* Tkinter (usually included with Python)


Contact Book Application:-

This is a Contact Book application built using Python's Tkinter library. The app provides a graphical interface for managing contacts, allowing users to add, view, edit, delete, and search for contact information.

Features:
* Add Contact: Input and save a new contact with fields for Name, Phone, Email, and Address.
* Show Contacts: Display all saved contacts in a scrollable list.
* Edit Contact: Modify the details of an existing contact.
* Delete Contact: Remove a selected contact from the list.
* Search Contacts: Find contacts by name or phone number.

Usage:
1) Running the Application:
* Ensure you have Python installed on your system.
* Run the script using Python. The application window will open with the contact book interface.
2) Adding a Contact:
* Fill in the Name, Phone, Email, and Address fields.
* Click the "Add Contact" button to save the contact.
3) Viewing Contacts:
* Click the "Show Contacts" button to view all saved contacts in the listbox.
4) Editing a Contact:
* Select a contact from the listbox.
* Click the "Edit Contact" button to populate the entry fields with the selected contact's information. Modify the details and click "Add Contact" to save changes.
5) Deleting a Contact:
* Select a contact from the listbox.
* Click the "Delete Contact" button to remove the contact from the list.
6) Searching for Contacts:
* Click the "Search Contacts" button and enter the name or phone number to search for. The app will display matching contacts.
7) Code Overview:
* create_widgets(): Sets up the GUI layout, including labels, entry fields, listbox, and buttons.
* add_contact(): Adds a new contact to the list and displays a confirmation message.
* show_contacts(): Displays all saved contacts in the listbox.
* edit_contact(): Allows modification of selected contact details.
* delete_contact(): Removes a selected contact from the list.
* search_contacts(): Searches for contacts based on a user-provided search term.
* clear_entry_fields(): Clears all entry fields.
* update_contacts_listbox(): Refreshes the listbox with the current contacts.

Requirements:
* Python 3.x
* Tkinter (usually included with Python)


Random Password Generator:-

This is a simple Python script that generates a random password based on user-specified length. It uses a combination of letters, digits, and special characters to create a secure and unpredictable password.

Features:
* Customizable Length: Allows the user to specify the desired length of the generated password.
* Diverse Character Set: Includes uppercase and lowercase letters, digits, and special characters for strong password creation.

Usage:
1) Running the Script:
* Ensure you have Python installed on your system.
* Run the script using Python.
2) Generating a Password:
* When prompted, enter the desired length for the password.
* The script will generate and display a random password with the specified length.

Code Overview:
* Character Set: Uses a list of characters consisting of uppercase and lowercase letters, digits, and special characters.
* generate_random_password():
  -Prompts the user for the password length.
  -Shuffles the characters and selects random ones to form the password.
  -Shuffles the resulting password for added randomness.
  Prints the generated password.

Requirements:
* Python 3.x


Rock, Paper, Scissors Game:-

This is a simple command-line Rock, Paper, Scissors game implemented in Python. The game allows the user to play against the computer, providing a fun and interactive way to enjoy the classic game.

Features:
* User Input: Prompts the user to choose Rock, Paper, or Scissors.
* Computer Choice: The computer randomly selects its choice from Rock, Paper, or Scissors.
* Determine Winner: Determines the outcome of the game based on the rules of Rock, Paper, Scissors.
* Play Again Option: Asks the user if they want to play another round.

Usage:
1) Running the Game:
* Ensure you have Python installed on your system.
* Run the script using Python.
2) Playing the Game:
* Follow the prompts to choose Rock, Paper, or Scissors.
* The computer will randomly select its choice.
* The game will display the result of the round (win, lose, or tie).
* You will be asked if you want to play another round. Type "yes" to continue or "no" to exit.

Code Overview:
* get_user_choice():
   -Prompts the user to input their choice.
   -Validates the input and ensures it is one of the accepted options.
* get_computer_choice():
   -Randomly selects a choice for the computer.
   -determine_winner(user_choice, computer_choice):
   -Determines the winner based on user and computer choices using predefined win conditions.
* main():
   -Orchestrates the game flow, including user interaction, computer choice, result display, and replay option.

Requirements:
* Python 3.x


