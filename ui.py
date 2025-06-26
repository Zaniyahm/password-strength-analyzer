import tkinter as tk
from analyzer import analyze_password
from wordlist_generator import generate_wordlist

def run_analysis():
    pwd = password_entry.get()
    analyze_password(pwd)

def run_wordlist():
    generate_wordlist(name_entry.get(), birth_entry.get(), pet_entry.get())

root = tk.Tk()
root.title("Password Analyzer Tool")
root.geometry("400x300")

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

tk.Button(root, text="Analyze", command=run_analysis).pack(pady=5)

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Birth Year:").pack()
birth_entry = tk.Entry(root)
birth_entry.pack()

tk.Label(root, text="Pet Name:").pack()
pet_entry = tk.Entry(root)
pet_entry.pack()

tk.Button(root, text="Generate Wordlist", command=run_wordlist).pack(pady=5)

root.mainloop()
