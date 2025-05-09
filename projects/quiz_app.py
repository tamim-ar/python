import tkinter as tk
from tkinter import messagebox

questions = [
    ("Capital of France?", "Paris"),
    ("5 + 3 = ?", "8"),
    ("Python is a ___?", "language")
]

index = 0
score = 0

def check_answer():
    global index, score
    ans = answer.get()
    if ans.lower() == questions[index][1].lower():
        score += 1
    index += 1
    if index < len(questions):
        question.config(text=questions[index][0])
        answer.delete(0, tk.END)
    else:
        messagebox.showinfo("Quiz Completed", f"Your Score: {score}/{len(questions)}")
        root.destroy()

root = tk.Tk()
root.title("Quiz App")

question = tk.Label(root, text=questions[0][0], font=("Arial", 16))
question.pack(pady=10)

answer = tk.Entry(root)
answer.pack()

tk.Button(root, text="Submit", command=check_answer).pack(pady=10)

root.mainloop()
