import tkinter as tk

def convert():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result.config(text=f"{fahrenheit:.2f} °F")

root = tk.Tk()
root.title("Celsius to Fahrenheit")

tk.Label(root, text="Enter Celsius:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Convert", command=convert).pack()
result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()
