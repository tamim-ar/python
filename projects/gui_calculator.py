import tkinter as tk

def press(num): entry.insert(tk.END, str(num))
def clear(): entry.delete(0, tk.END)
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except: entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 20), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 1
col = 0
for b in buttons:
    action = lambda x=b: press(x) if x != '=' else equal()
    if b == '=': btn = tk.Button(root, text=b, width=10, height=2, command=equal)
    else: btn = tk.Button(root, text=b, width=5, height=2, command=action)
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', width=20, height=2, command=clear).grid(row=5, column=0, columnspan=4)

root.mainloop()
