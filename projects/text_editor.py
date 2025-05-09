import tkinter as tk
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename()
    if path:
        with open(path, 'r') as f:
            text.delete(1.0, tk.END)
            text.insert(tk.END, f.read())

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, 'w') as f:
            f.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root, wrap='word')
text.pack(expand=True, fill='both')

tk.Button(root, text="Open", command=open_file).pack(side='left')
tk.Button(root, text="Save", command=save_file).pack(side='left')

root.mainloop()
