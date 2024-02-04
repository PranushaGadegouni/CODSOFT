from tkinter import Tk, Frame, Listbox, Scrollbar, Text, Button, messagebox

# Function to add a task
def add_task():
    # Function to handle the "Add task" button click in the pop-up window
    def add():
        task_text = text_entry.get(1.0, "end-1c")
        if not task_text.strip():
            messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert("end", task_text)
            root_add_task.destroy()

    # Create the pop-up window for adding a task
    root_add_task = Tk()
    root_add_task.title("Add task")
    text_entry = Text(root_add_task, width=40, height=4)
    text_entry.pack()
    button_add_task = Button(root_add_task, text="Add task", command=add)
    button_add_task.pack()
    root_add_task.mainloop()

# Function to delete a task
def delete_task():
    selected = listbox_task.curselection()
    if selected:
        listbox_task.delete(selected[0])

# Function to mark a task as completed
def mark_completed():
    selected = listbox_task.curselection()
    if selected:
        index = selected[0]
        task_text = listbox_task.get(index)
        updated_text = task_text + " ✔"
        listbox_task.delete(index)
        listbox_task.insert(index, updated_text)

# Function to handle key presses
def handle_key(event):
    if event.keysym == 'a':  # Press 'a' to add a task
        add_task()
    elif event.keysym == 'd':  # Press 'd' to delete a task
        delete_task()
    elif event.keysym == 'm':  # Press 'm' to mark a task as completed
        mark_completed()

# Main window
window = Tk()
window.title("To-Do List")

# Frame to hold the listbox and scrollbar
frame_task = Frame(window)
frame_task.pack()

# Listbox to display tasks
listbox_task = Listbox(frame_task, bg="lavender", fg="black", height=15, width=50, font="Helvetica")
listbox_task.pack(side="left")

# Scrollbar for the listbox
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side="right", fill="y")
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Buttons for user actions
button_add = Button(window, text="Add task", width=50, command=add_task)
button_add.pack(pady=3)

button_delete = Button(window, text="Delete selected task", width=50, command=delete_task)
button_delete.pack(pady=3)

button_mark_completed = Button(window, text="Mark as completed", width=50, command=mark_completed)
button_mark_completed.pack(pady=3)

# Bind key presses to the handle_key function
window.bind('<Key>', handle_key)

# Start the Tkinter event loop
window.mainloop()