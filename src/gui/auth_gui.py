import tkinter as tk
from tkinter import ttk, messagebox

class AuthGUI(tk.Frame):
    """Authentication GUI for Login/Register."""
    def __init__(self, master, file_client):
        super().__init__(master, bg="#f8f9fa")
        self.file_client = file_client

        tk.Label(self, text="Welcome to File Sharing", font=("Arial", 18, "bold"), bg="#f8f9fa", fg="#343a40").pack(pady=(20, 20))

        ttk.Button(self, text="Login", command=lambda: master.switch_frame(LoginPage)).pack(pady=10, ipadx=30)
        ttk.Button(self, text="Register", command=lambda: master.switch_frame(RegisterPage)).pack(pady=10, ipadx=30)

class LoginPage(tk.Frame):
    """Login Page."""
    def __init__(self, master, file_client):
        super().__init__(master, bg="#f8f9fa")
        self.file_client = file_client
        self.master = master

        self.setup_ui()

    def setup_ui(self):
        frame = tk.Frame(self, width=350, height=350, bg="#f8f9fa")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        heading = tk.Label(frame, text='Login', fg='#57a1f8', bg='#f8f9fa', font=('', 23, 'bold'))
        heading.place(x=100, y=5)

        self.username = tk.Entry(frame, width=25, font=('', 11), border=0, bg='#f8f9fa')
        self.username.place(x=30, y=80)
        self.username.insert(0, 'Username')
        self.username.bind('<FocusIn>', self.on_focus_in)
        self.username.bind('<FocusOut>', self.on_focus_out)

        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.password = tk.Entry(frame, width=25, font=('', 11), border=0, bg='#f8f9fa')
        self.password.place(x=30, y=150)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', self.on_focus_in)
        self.password.bind('<FocusOut>', self.on_focus_out)

        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        signin_btn = tk.Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=self.login)
        signin_btn.place(x=35, y=204)

        label = tk.Label(frame, text="Don't have an account?", fg='black', bg='#f8f9fa', font=('', 9))
        label.place(x=75, y=270)
        signupNav_btn = tk.Button(frame, width=6, text='Sign up', border=0, bg='#f8f9fa', cursor='hand2', fg='#57a1f8', command=lambda: self.master.switch_frame(RegisterPage))
        signupNav_btn.place(x=215, y=270)

    def on_focus_in(self, event):
        widget = event.widget
        if widget.get() in ['Username', 'Password']:
            widget.delete(0, tk.END)
            if widget == self.password:
                widget.config(show='*')

    def on_focus_out(self, event):
        widget = event.widget
        if widget.get() == '':
            if widget == self.username:
                widget.insert(0, 'Username')
            elif widget == self.password:
                widget.insert(0, 'Password')
                widget.config(show='')

    def login(self):
        username = self.username.get()
        password = self.password.get()
        if username and password:
            result = self.file_client.login(username, password)
            if result:
                messagebox.showinfo("Login", "Login Successful")
                self.master.on_authenticated()
            else:
                messagebox.showerror("Login Error", "Login failed. Please try again.")
        else:
            messagebox.showerror("Input Error", "Please enter both username and password.")

class RegisterPage(tk.Frame):
    """Registration Page."""
    def __init__(self, master, file_client):
        super().__init__(master, bg="#f8f9fa")
        self.file_client = file_client
        self.master = master

        self.setup_ui()

    def setup_ui(self):
        frame = tk.Frame(self, width=350, height=350, bg="#f8f9fa")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        heading = tk.Label(frame, text='Sign up', fg='#57a1f8', bg='#f8f9fa', font=('', 23, 'bold'))
        heading.place(x=100, y=5)

        self.username = tk.Entry(frame, width=25, font=('', 11), border=0, bg='#f8f9fa')
        self.username.place(x=30, y=80)
        self.username.insert(0, 'Username')
        self.username.bind('<FocusIn>', self.on_focus_in)
        self.username.bind('<FocusOut>', self.on_focus_out)

        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.password = tk.Entry(frame, width=25, font=('', 11), border=0, bg='#f8f9fa')
        self.password.place(x=30, y=150)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', self.on_focus_in)
        self.password.bind('<FocusOut>', self.on_focus_out)

        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        signup_btn = tk.Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=self.register)
        signup_btn.place(x=35, y=204)

        label = tk.Label(frame, text="Already have an account", fg='black', bg='#f8f9fa', font=('', 9))
        label.place(x=90, y=270)
        signinNav_btn = tk.Button(frame, width=6, text='Sign in', border=0, bg='#f8f9fa', cursor='hand2', fg='#57a1f8', command=lambda: self.master.switch_frame(LoginPage))
        signinNav_btn.place(x=225, y=270)

    def on_focus_in(self, event):
        widget = event.widget
        if widget.get() in ['Username', 'Password']:
            widget.delete(0, tk.END)
            if widget == self.password:
                widget.config(show='*')

    def on_focus_out(self, event):
        widget = event.widget
        if widget.get() == '':
            if widget == self.username:
                widget.insert(0, 'Username')
            elif widget == self.password:
                widget.insert(0, 'Password')
                widget.config(show='')

    def register(self):
        username = self.username.get()
        password = self.password.get()
        if username and password:
            self.file_client.register(username, password)
            messagebox.showinfo("Registration", "Registration successful!")
            self.master.switch_frame(LoginPage)
        else:
            messagebox.showerror("Input Error", "Please enter both username and password.")
