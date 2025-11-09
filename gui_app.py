import tkinter as tk
from tkinter import ttk, messagebox
from main import generate_password
from strength_checker import check_password_strength

# --- Functions ---
def generate():
    try:
        length = int(length_var.get())
        if length < 4:
            messagebox.showwarning("Too short", "Use length ≥ 4 for a decent password.")
            return
        pwd = generate_password(length=length)
        strength = check_password_strength(pwd)

        output.configure(state="normal")
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Generated Password:\n{pwd}\n\nStrength: {strength}")
        output.configure(state="disabled")

        copy_btn.configure(state="normal")
        window.clipboard_clear()
        window.clipboard_append(pwd)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")

def clear_output():
    output.configure(state="normal")
    output.delete("1.0", tk.END)
    output.configure(state="disabled")
    copy_btn.configure(state="disabled")

def copy_to_clipboard():
    text = output.get("1.0", "3.0").strip()
    if "Generated Password:" in text:
        pwd = text.split("Generated Password:", 1)[1].splitlines()[0].strip()
        window.clipboard_clear()
        window.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Nothing to copy", "Generate a password first.")

# --- Window Setup ---
window = tk.Tk()
window.title("Password Generator + Strength Checker")
window.geometry("550x420")
window.resizable(False, False)

# Optional: Add custom app icon if icon.png exists
try:
    window.iconphoto(False, tk.PhotoImage(file="icon.png"))
except Exception:
    pass

# --- Gradient Background ---
gradient = tk.Canvas(window, width=550, height=420, highlightthickness=0)
gradient.pack(fill="both", expand=True)

# Create vertical gradient (top → bottom)
for i in range(0, 420):
    r = int(20 + i * 0.1)
    g = int(22 + i * 0.25)
    b = int(30 + i * 0.35)
    color = f"#{r:02x}{g:02x}{b:02x}"
    gradient.create_line(0, i, 550, i, fill=color)

# --- ttk Styling ---
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#1e1f22")
style.configure("TLabel", background="#1e1f22", foreground="white", font=("Poppins", 11))
style.configure("TEntry", fieldbackground="#2f3136", foreground="white", padding=5)
style.map("TEntry", fieldbackground=[("focus", "#40444b")])

style.configure("Accent.TButton", font=("Poppins", 11, "bold"), padding=8)
style.map("Accent.TButton", background=[("active", "#7289da"), ("!disabled", "#5865f2")], foreground=[("!disabled", "white")])

style.configure("Danger.TButton", font=("Poppins", 11, "bold"), padding=8)
style.map("Danger.TButton", background=[("active", "#ff4b4b"), ("!disabled", "#f04747")], foreground=[("!disabled", "white")])

style.configure("Success.TButton", font=("Poppins", 11, "bold"), padding=8)
style.map("Success.TButton", background=[("active", "#43b581"), ("!disabled", "#3ba55d")], foreground=[("!disabled", "white")])

# --- Layout Frame on Top of Gradient ---
container = ttk.Frame(window, padding=20)
container.place(relx=0.5, rely=0.5, anchor="center")

# --- Title ---
title = ttk.Label(container, text="🔐 Password Generator + Strength Checker",
                  font=("Poppins", 15, "bold"), foreground="#ffcc00")
title.pack(pady=(5, 15))

# --- Input ---
length_row = ttk.Frame(container)
length_row.pack(pady=5)
ttk.Label(length_row, text="Enter Password Length:", font=("Poppins", 11, "bold")).pack(side="left", padx=(0, 8))
length_var = tk.StringVar(value="12")
length_entry = ttk.Entry(length_row, textvariable=length_var, width=8)
length_entry.pack(side="left")

# --- Buttons ---
btn_frame = ttk.Frame(container)
btn_frame.pack(pady=15)
generate_btn = ttk.Button(btn_frame, text="Generate Password", style="Accent.TButton", command=generate)
generate_btn.pack(side="left", padx=8)
clear_btn = ttk.Button(btn_frame, text="Clear", style="Danger.TButton", command=clear_output)
clear_btn.pack(side="left", padx=8)
copy_btn = ttk.Button(btn_frame, text="Copy Password", style="Success.TButton", command=copy_to_clipboard, state="disabled")
copy_btn.pack(side="left", padx=8)

# --- Output ---
output = tk.Text(container, height=8, width=60, font=("Courier", 11),
                 bg="#2f3136", fg="#ffffff", wrap="word", relief="flat", padx=10, pady=10)
output.pack(pady=10)
output.configure(state="disabled")

length_entry.focus()
window.mainloop()

