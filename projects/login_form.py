import tkinter as tk
from tkinter import messagebox

def login():
    user = username.get()
    pwd = password.get()
    if user == "admin" and pwd == "123":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Credentials")

root = tk.Tk()
root.title("Login Form")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
