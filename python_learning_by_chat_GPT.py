import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Tkinter Basics")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()

root.mainloop()