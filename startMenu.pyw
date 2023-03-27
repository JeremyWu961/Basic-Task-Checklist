import tkinter as tk
from tkinter import ttk
from tkinter import font
import os
import subprocess

taskLists = []

def getTxtFiles():
    # Get current directory
    currentDir = os.getcwd()

    # Get list of files in directory
    file_list = os.listdir(currentDir)
    for file_name in file_list:
        # Check if the file has a .txt extension using os.path.splitext()
        _, file_extension = os.path.splitext(file_name) 
        # _ in above line indicates we don't need the first value returned
        # os.path.splittext() returns a tuple with 2 values
        # the first value is the filename, the second is the file extension
    
        if file_extension == '.txt':
        # The file has a .txt extension, add it to the list
            taskLists.append(file_name)
        
getTxtFiles()

def submit():
    selected_value = input_var.get()
    window.destroy() # Close the window
    subprocess.call(['python', 'listGenerator.pyw', selected_value],  creationflags=subprocess.CREATE_NO_WINDOW) # Call main script with the selected value as an argument

# Create the window
window = tk.Tk()
window.title("Title")
window.option_add("*Font", "TkDefaultFont 20")

# Adding widgets to the window here
label = tk.Label(window, text="This program only works correctly if the \ntext files are formatted correctly")
label.pack(pady=5)
label2 = tk.Label(window, text="Select an option to create a checklist:")
label2.pack(pady=5)

# Create a dropdown menu in window
input_var = tk.StringVar()
input_dropdown = ttk.Combobox(window, textvariable=input_var, values=taskLists)
input_dropdown.pack(pady=5)

# Add a button to submit the input
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(pady=5)

# Start the main event loop to display the window
window.mainloop()