
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("GPA Calculator")
root.geometry("500x600")
root.configure(bg="lightpink")


subjects = []


title = tk.Label(
    root,
    text="welcome GPA CALCULATOR\nthanks for choosing",
    font=("Comic Sans MS", 22, "bold"),
    bg="pink",
    fg="blue"
)
title.pack(pady=20)


tk.Label(root, text="Subject Name",
         font=("Arial", 12),
           bg="pink").pack()

subject_entry = tk.Entry(root, font=("Comic Sans MS", 12),bg="lightblue")
subject_entry.pack(pady=5)

tk.Label(root, text="Grade Point (0-10)",
         font=("Arial", 12),
           bg="pink").pack()

grade_entry = tk.Entry(root, font=("Comic Sans MS", 12),bg="lightblue")
grade_entry.pack(pady=5)

tk.Label(root, text="Subject Credits",
         font=("Arial", 12), bg="pink").pack()

credit_entry = tk.Entry(root, font=("Comic Sans MS", 12),bg="lightblue")
credit_entry.pack(pady=5)



def add_subject():
    try:
        name = subject_entry.get().strip()
        grade = float(grade_entry.get())
        credit = float(credit_entry.get())

        if not name:
            messagebox.showerror("Error", "Enter subject name")
            return

        if grade < 0 or grade > 10 or credit <= 0:
            messagebox.showerror("Error", "Enter valid grade and credits")
            return

        subjects.append((name, grade, credit))

        subject_list.insert(
            tk.END,
            f"{name} | Grade: {grade} | Credits: {credit}"
        )

        subject_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        credit_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")



def calculate_gpa():
    if not subjects:
        messagebox.showerror("Error", "Add at least one subject")
        return

    total_points = sum(
        grade * credit for name, grade, credit in subjects
    )

    total_credits = sum(
        credit for name, grade, credit in subjects
    )

    gpa = total_points / total_credits

    result_label.config(
        text=f"Your GPA: {gpa:.2f} / 10"
    )



add_button = tk.Button(
    root,
    text="Add Subject",
    command=add_subject,
    bg="lightblue",
    fg="white",
    font=("Arial", 12, "bold")
)
add_button.pack(pady=12)


tk.Label(root, text="Added Subjects",
         font=("Arial", 12, "bold"),
         bg="pink").pack()

subject_list = tk.Listbox(root, width=48, height=7)
subject_list.pack(pady=10)



calculate_button = tk.Button(
    root,
    text="Calculate GPA",
    command=calculate_gpa,
    bg="green",
    fg="white",
    font=("Arial", 13, "bold")
)
calculate_button.pack(pady=10)


result_label = tk.Label(
    root,
    text="Your GPA: --",
    font=("Arial", 18, "bold"),
    bg="pink",
    fg="green"
)
result_label.pack(pady=15)




root.mainloop()