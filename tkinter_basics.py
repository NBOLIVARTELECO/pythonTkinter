# Import the tkinter library - this is the main GUI library in Python
import tkinter as tk
from tkinter import messagebox  # Import messagebox for showing popup messages

# Create the main application window
# This is the ventana window that will contain all other widgets
ventana = tk.Tk()

# Set the title of the window
ventana.title("Tkinter Basics Tutorial")

# Set the window size (width x height)
ventana.geometry("600x400")

# Set a background color for the window
ventana.configure(bg="#f0f0f0")

# Create a Label widget
# Labels are used to display text or images
label = tk.Label(
    ventana,
    text="Welcome to Tkinter Basics!",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333333"
)
# Use pack() to add the label to the window
# pack() is one of the geometry managers in Tkinter
label.pack(pady=20)

# Create a Frame widget
# Frames are used to organize and group other widgets
frame = tk.Frame(ventana, bg="#f0f0f0")
frame.pack(pady=10)

# Create an Entry widget (text input field)
# Entry widgets are used to get single-line text input from the user
entry = tk.Entry(
    frame,
    width=30,
    font=("Arial", 12)
)
entry.pack(pady=5)

# Create a Button widget
# Buttons are used to trigger actions when clicked
def button_click():
    # Get the text from the entry widget
    text = entry.get()
    if text:
        # Show a message box with the entered text
        messagebox.showinfo("Message", f"You entered: {text}")
    else:
        messagebox.showwarning("Warning", "Please enter some text!")

button = tk.Button(
    frame,
    text="Click Me!",
    command=button_click,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    padx=10,
    pady=5
)
button.pack(pady=5)

# Create a Checkbutton widget
# Checkbuttons are used for boolean (True/False) inputs
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(
    frame,
    text="I agree to the terms",
    variable=check_var,
    bg="#f0f0f0",
    font=("Arial", 12)
)
checkbutton.pack(pady=5)

# Create a Radiobutton widget
# Radiobuttons are used when you want the user to select one option from a set
radio_var = tk.StringVar()
radio_var.set("option1")  # Set default selection

radio1 = tk.Radiobutton(
    frame,
    text="Option 1",
    variable=radio_var,
    value="option1",
    bg="#f0f0f0",
    font=("Arial", 12)
)
radio1.pack()

radio2 = tk.Radiobutton(
    frame,
    text="Option 2",
    variable=radio_var,
    value="option2",
    bg="#f0f0f0",
    font=("Arial", 12)
)
radio2.pack()

# Create a Listbox widget
# Listboxes are used to display a list of items
listbox = tk.Listbox(
    frame,
    height=3,
    font=("Arial", 12)
)
listbox.pack(pady=5)

# Add items to the listbox
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)

# Start the main event loop
# This keeps the window open and handles user interactions
ventana.mainloop() 