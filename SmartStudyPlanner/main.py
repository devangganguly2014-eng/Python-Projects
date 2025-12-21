import tkinter as tk
from tkinter import messagebox
from logic import generate_plan

subjects = []

def add_subject():
    name = subject_entry.get().strip()
    level = level_var.get().lower()

    if not name:
        messagebox.showerror("Error", "Subject name cannot be empty")
        return

    subjects.append((name, level))
    subject_listbox.insert(tk.END, f"{name} ({level.capitalize()})")
    subject_entry.delete(0, tk.END)

def clear_subjects():
    subjects.clear()
    subject_listbox.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

def generate_timetable():
    if not subjects:
        messagebox.showerror("Error", "Add at least one subject")
        return

    try:
        total_hours = float(hours_entry.get())
        if total_hours <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter valid study hours")
        return

    plan = generate_plan(subjects, total_hours)

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "📚 ADVANCED SMART STUDY PLAN\n\n")

    for item in plan:
        hours = item["minutes"] // 60
        minutes = item["minutes"] % 60

        result_text.insert(
            tk.END,
            f"{item['subject']} ({item['level'].capitalize()})\n"
            f"Time: {hours}h {minutes}m | Slot: {item['slot']}\n\n"
        )

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Smart Study Planner - Advanced")
root.geometry("480x620")
root.resizable(False, False)

tk.Label(
    root,
    text="Smart Study Planner (Advanced)",
    font=("Arial", 16, "bold")
).pack(pady=10)

subject_entry = tk.Entry(root, width=32)
subject_entry.pack()
subject_entry.insert(0, "Enter Subject Name")

level_var = tk.StringVar(value="Weak")
tk.OptionMenu(root, level_var, "Weak", "Medium", "Strong").pack(pady=5)

tk.Button(root, text="Add Subject", width=22, command=add_subject).pack(pady=5)

subject_listbox = tk.Listbox(root, width=50, height=6)
subject_listbox.pack(pady=10)

hours_entry = tk.Entry(root, width=32)
hours_entry.pack()
hours_entry.insert(0, "Total Study Hours")

tk.Button(root, text="Generate Timetable", width=25, command=generate_timetable).pack(pady=8)
tk.Button(root, text="Clear All", width=25, command=clear_subjects).pack(pady=4)

result_text = tk.Text(root, width=55, height=14)
result_text.pack(pady=10)

root.mainloop()

