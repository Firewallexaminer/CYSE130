#Just a simple login user interface

import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "user" and password == "password":
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

window = tk.Tk()
window.title("Login")

username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(window, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2)

window.mainloop()

