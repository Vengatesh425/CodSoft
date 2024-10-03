import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length   :")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = ttk.Entry(root, width=15)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.password_label = ttk.Label(root, text="Your Password    :")
        self.password_label.grid(row=2, column=0, padx=10, pady=10)

        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(root, textvariable=self.password_var, state='readonly', width=40)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showwarning("Warning", "Password length must be greater than zero.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        self.password_var.set(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
    
    
