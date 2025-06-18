# Import the tkinter library - this is the main GUI library in Python
import tkinter as tk
from tkinter import messagebox, ttk, filedialog, colorchooser, simpledialog
from datetime import datetime

# Create the main application window
# This is the ventana window that will contain all other widgets
ventana = tk.Tk()

# Set the title of the window
ventana.title("Tkinter Complete Tutorial - Widgets Collection")

# Set the window size (width x height)
ventana.geometry("800x700")

# Set a background color for the window
ventana.configure(bg="#f0f0f0")

# Make window resizable
ventana.resizable(True, True)

# Create a main title label
main_title = tk.Label(
    ventana,
    text="🐍 Complete Tkinter Widgets Tutorial 🐍",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
main_title.pack(pady=10)

# Create a Notebook (tabs) for better organization
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# ==================== TAB 1: BASIC WIDGETS ====================
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Basic Widgets")

# Create a scrollable frame for tab1
canvas1 = tk.Canvas(tab1, bg="#f0f0f0")
scrollbar1 = ttk.Scrollbar(tab1, orient="vertical", command=canvas1.yview)
scrollable_frame1 = ttk.Frame(canvas1)

scrollable_frame1.bind(
    "<Configure>",
    lambda e: canvas1.configure(scrollregion=canvas1.bbox("all"))
)

canvas1.create_window((0, 0), window=scrollable_frame1, anchor="nw")
canvas1.configure(yscrollcommand=scrollbar1.set)

canvas1.pack(side="left", fill="both", expand=True)
scrollbar1.pack(side="right", fill="y")

# Basic widgets section
basic_frame = tk.LabelFrame(scrollable_frame1, text="Basic Input Widgets", font=("Arial", 12, "bold"))
basic_frame.pack(fill="x", padx=10, pady=5)

# Entry widget with validation
tk.Label(basic_frame, text="Text Entry:", font=("Arial", 10)).pack(anchor="w", padx=5)
entry = tk.Entry(basic_frame, width=40, font=("Arial", 12))
entry.pack(pady=5, padx=5)
entry.insert(0, "Type something here...")

# Text widget (multi-line)
tk.Label(basic_frame, text="Multi-line Text:", font=("Arial", 10)).pack(anchor="w", padx=5)
text_widget = tk.Text(basic_frame, height=4, width=50, font=("Arial", 10))
text_widget.pack(pady=5, padx=5)
text_widget.insert("1.0", "This is a multi-line text widget.\nYou can type multiple lines here!")

# Button with enhanced functionality
def enhanced_button_click():
    entry_text = entry.get()
    text_content = text_widget.get("1.0", tk.END).strip()
    
    if entry_text and text_content:
        result = f"Entry: {entry_text}\n\nText Area:\n{text_content}"
        messagebox.showinfo("Form Data", result)
    else:
        messagebox.showwarning("Warning", "Please fill in both fields!")

button = tk.Button(
    basic_frame,
    text="📝 Process Form Data",
    command=enhanced_button_click,
    bg="#3498db",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=8,
    relief="raised"
)
button.pack(pady=10)

# ==================== SELECTION WIDGETS ====================
selection_frame = tk.LabelFrame(scrollable_frame1, text="Selection Widgets", font=("Arial", 12, "bold"))
selection_frame.pack(fill="x", padx=10, pady=5)

# Checkbuttons with variables
check_vars = {}
checkboxes = ["Python", "JavaScript", "Java", "C++", "Go"]

tk.Label(selection_frame, text="Programming Languages (select multiple):", font=("Arial", 10)).pack(anchor="w", padx=5)
check_frame = tk.Frame(selection_frame)
check_frame.pack(pady=5)

for i, lang in enumerate(checkboxes):
    check_vars[lang] = tk.BooleanVar()
    cb = tk.Checkbutton(
        check_frame,
        text=lang,
        variable=check_vars[lang],
        font=("Arial", 10)
    )
    cb.grid(row=i//3, column=i%3, sticky="w", padx=10)

# Radiobuttons
tk.Label(selection_frame, text="Experience Level:", font=("Arial", 10)).pack(anchor="w", padx=5, pady=(10,0))
radio_var = tk.StringVar(value="beginner")
radio_frame = tk.Frame(selection_frame)
radio_frame.pack(pady=5)

levels = [("Beginner", "beginner"), ("Intermediate", "intermediate"), ("Advanced", "advanced"), ("Expert", "expert")]
for text, value in levels:
    tk.Radiobutton(
        radio_frame,
        text=text,
        variable=radio_var,
        value=value,
        font=("Arial", 10)
    ).pack(side="left", padx=10)

# Listbox with scrollbar
tk.Label(selection_frame, text="Favorite Frameworks:", font=("Arial", 10)).pack(anchor="w", padx=5, pady=(10,0))
listbox_frame = tk.Frame(selection_frame)
listbox_frame.pack(pady=5, padx=5)

listbox = tk.Listbox(listbox_frame, height=4, selectmode="multiple", font=("Arial", 10))
listbox_scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
listbox.config(yscrollcommand=listbox_scrollbar.set)
listbox_scrollbar.config(command=listbox.yview)

frameworks = ["Django", "Flask", "FastAPI", "React", "Vue.js", "Angular", "Spring Boot", "Express.js"]
for framework in frameworks:
    listbox.insert(tk.END, framework)

listbox.pack(side="left", fill="both", expand=True)
listbox_scrollbar.pack(side="right", fill="y")

# ==================== TAB 2: ADVANCED WIDGETS ====================
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Advanced Widgets")

# Advanced widgets frame
advanced_frame = tk.LabelFrame(tab2, text="Advanced Controls", font=("Arial", 12, "bold"))
advanced_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Scale widget
tk.Label(advanced_frame, text="Adjust Value (Scale):", font=("Arial", 10)).pack(anchor="w", padx=5)
scale_var = tk.DoubleVar()
scale = tk.Scale(
    advanced_frame,
    from_=0,
    to=100,
    orient="horizontal",
    variable=scale_var,
    length=300,
    font=("Arial", 10)
)
scale.pack(pady=5)

# Scale value display
scale_label = tk.Label(advanced_frame, text="Value: 0", font=("Arial", 10))
scale_label.pack()

def update_scale_label(val):
    scale_label.config(text=f"Value: {float(val):.1f}")

scale.config(command=update_scale_label)

# Spinbox
tk.Label(advanced_frame, text="Age (Spinbox):", font=("Arial", 10)).pack(anchor="w", padx=5, pady=(10,0))
spinbox = tk.Spinbox(
    advanced_frame,
    from_=0,
    to=120,
    width=10,
    font=("Arial", 12)
)
spinbox.pack(pady=5)

# Progressbar
tk.Label(advanced_frame, text="Progress Bar:", font=("Arial", 10)).pack(anchor="w", padx=5, pady=(10,0))
progress = ttk.Progressbar(
    advanced_frame,
    length=300,
    mode='determinate'
)
progress.pack(pady=5)

def start_progress():
    import threading
    def update_progress():
        for i in range(101):
            progress['value'] = i
            ventana.update_idletasks()
            ventana.after(50)
        messagebox.showinfo("Complete", "Progress completed!")
        progress['value'] = 0
    
    threading.Thread(target=update_progress, daemon=True).start()

tk.Button(
    advanced_frame,
    text="▶️ Start Progress",
    command=start_progress,
    bg="#e74c3c",
    fg="white",
    font=("Arial", 10, "bold")
).pack(pady=5)

# Combobox (TTK)
tk.Label(advanced_frame, text="Country (Combobox):", font=("Arial", 10)).pack(anchor="w", padx=5, pady=(10,0))
countries = ["USA", "Canada", "Mexico", "Brazil", "Argentina", "Spain", "France", "Germany", "Italy", "Japan", "China", "India"]
combo = ttk.Combobox(
    advanced_frame,
    values=countries,
    state="readonly",
    font=("Arial", 12)
)
combo.pack(pady=5)
combo.set("Select a country")

# ==================== TAB 3: DIALOG & FILE OPERATIONS ====================
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Dialogs & Files")

dialog_frame = tk.LabelFrame(tab3, text="Dialog Examples", font=("Arial", 12, "bold"))
dialog_frame.pack(fill="both", expand=True, padx=10, pady=10)

# File operations
file_label = tk.Label(dialog_frame, text="No file selected", bg="white", relief="sunken", height=2)
file_label.pack(fill="x", padx=10, pady=5)

def open_file():
    filename = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
    )
    if filename:
        file_label.config(text=f"Selected: {filename}")

def save_file():
    filename = filedialog.asksaveasfilename(
        title="Save file as",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filename:
        with open(filename, 'w') as f:
            f.write("Hello from Tkinter!")
        messagebox.showinfo("Success", f"File saved as: {filename}")

tk.Button(dialog_frame, text="📁 Open File", command=open_file, bg="#27ae60", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5, pady=10)
tk.Button(dialog_frame, text="💾 Save File", command=save_file, bg="#2980b9", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5, pady=10)

# Color chooser
color_label = tk.Label(dialog_frame, text="Selected Color", bg="white", width=20, height=2)
color_label.pack(pady=10)

def choose_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[1]:  # color[1] is the hex value
        color_label.config(bg=color[1], text=f"Color: {color[1]}")

tk.Button(dialog_frame, text="🎨 Choose Color", command=choose_color, bg="#9b59b6", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# Simple dialogs
def ask_question():
    answer = simpledialog.askstring("Question", "What's your favorite programming language?")
    if answer:
        messagebox.showinfo("Answer", f"You said: {answer}")

def ask_number():
    number = simpledialog.askinteger("Number", "Enter your age:", minvalue=0, maxvalue=150)
    if number is not None:
        messagebox.showinfo("Age", f"You are {number} years old")

tk.Button(dialog_frame, text="❓ Ask Question", command=ask_question, bg="#f39c12", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5, pady=10)
tk.Button(dialog_frame, text="🔢 Ask Number", command=ask_number, bg="#e67e22", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=5, pady=10)

# ==================== SUMMARY SECTION ====================
def show_summary():
    selected_langs = [lang for lang, var in check_vars.items() if var.get()]
    level = radio_var.get()
    selected_frameworks = [frameworks[i] for i in listbox.curselection()]
    scale_value = scale_var.get()
    age = spinbox.get()
    country = combo.get()
    
    summary = f"""
📊 FORM SUMMARY 📊

Entry Text: {entry.get()}
Experience Level: {level.title()}
Programming Languages: {', '.join(selected_langs) if selected_langs else 'None selected'}
Favorite Frameworks: {', '.join(selected_frameworks) if selected_frameworks else 'None selected'}
Scale Value: {scale_value:.1f}
Age: {age}
Country: {country}

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """
    
    messagebox.showinfo("Complete Summary", summary)

# Summary button at the bottom
summary_button = tk.Button(
    ventana,
    text="📋 Show Complete Summary",
    command=show_summary,
    bg="#34495e",
    fg="white",
    font=("Arial", 14, "bold"),
    padx=20,
    pady=10
)
summary_button.pack(pady=10)

# Status bar at the bottom
status_frame = tk.Frame(ventana, relief="sunken", bd=1)
status_frame.pack(side="bottom", fill="x")

status_label = tk.Label(
    status_frame,
    text="🚀 Tkinter Complete Tutorial - Ready for interaction!",
    font=("Arial", 10),
    anchor="w"
)
status_label.pack(side="left", padx=5)

time_label = tk.Label(
    status_frame,
    text="",
    font=("Arial", 10),
    anchor="e"
)
time_label.pack(side="right", padx=5)

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    ventana.after(1000, update_time)

update_time()

# Start the main event loop
# This keeps the window open and handles user interactions
print("🐍 Tkinter Complete Tutorial started successfully!")
print("Explore all tabs to see different widgets in action!")
ventana.mainloop()
