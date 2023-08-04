import tkinter as tk

def file_new():
    # Add code here to handle the "New" menu item action
    print("New File")

def file_open():
    # Add code here to handle the "Open" menu item action
    print("Open File")

def file_save():
    # Add code here to handle the "Save" menu item action
    print("Save File")

def edit_cut():
    print("Cut")

def edit_copy():
    print("Copy")

def edit_paste():
    print("Paste")

def file_exit():
    root.quit()

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Practice")

window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(anchor="w")

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(anchor="w")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0) # what is tearoff?
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu items to the "File" menu
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Save", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=file_exit)

# Create a "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add menu items to the "Edit" menu
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=edit_copy)
edit_menu.add_command(label="Paste", command=edit_paste)

root.mainloop()