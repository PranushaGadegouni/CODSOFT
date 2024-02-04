from tkinter import *

# globally declare the expression variable
expression = ""

# Function to handle button presses and update the expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    gui.configure(background="white")
    gui.title("Calculator")
    gui.geometry("300x400")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font=('Arial', 14))
    expression_field.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

    # Buttons for numbers and operators
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'  # 'C' for clear
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        # Create buttons with specified properties
        btn = Button(gui, text=button, fg='black', bg='light blue' if button != '=' else 'cadetblue2', font=('Arial', 12),
                     command=lambda b=button: press(b) if b != '=' else equal_press() if b != 'C' else clear())
        # Place buttons in the grid
        btn.grid(row=row_val, column=col_val, sticky='nsew', ipadx=10, ipady=10)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    # Make the grid responsive
    gui.grid_rowconfigure(0, weight=1)
    gui.grid_columnconfigure(0, weight=1)

    # start the GUI
    gui.mainloop()
