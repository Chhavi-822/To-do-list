import tkinter as tk  # import Tkinter for GUI
from tkinter import messagebox  # import messagebox for popup messages

# Create the main application window
root = tk.Tk()
root.title("To-Do List")  # Title of the window
root.geometry("400x400")  # Size of the window

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()  # Get text from input field
    if task != "":
        tasks.append(task)  # Add task to list
        update_task_list()  # Refresh the displayed list
        task_entry.delete(0, tk.END)  # Clear the input field
    else:
        messagebox.showwarning("Warning", "You must enter a task.")  # Show warning if empty

# Function to delete selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get selected task number
        tasks.pop(selected_task_index)  # Remove from list
        update_task_list()  # Refresh displayed list
    except:
        messagebox.showwarning("Warning", "Select a task to delete.")  # Show warning if none selected

# Function to update the listbox display
def update_task_list():
    task_listbox.delete(0, tk.END)  # Clear current listbox
    for task in tasks:
        task_listbox.insert(tk.END, task)  # Insert all tasks

# GUI Widgets

# Entry widget to input tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Button to add task
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Button to delete selected task
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
