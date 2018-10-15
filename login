import tkinter as tk


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)

        window.pack(side="top", fill="both", expand=True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginScreen, SignupScreen, Home):
            frame = F(window, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginScreen)

    def show_frame(self, wind):
        frame = self.frames[wind]
        frame.tkraise()


class LoginScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        L_name = tk.Label(self, text="Name")
        L_password = tk.Label(self, text="Password")
        self.E_name = tk.Entry(self)
        self.E_password = tk.Entry(self)
        B_login = tk.Button(self, text="Login")
        B_signup = tk.Button(self, text="Signup", command=lambda : controller.show_frame(SignupScreen))
        B_remember = tk.Checkbutton(self)
        L_remtext = tk.Label(self, text="Remember Me")

        L_name.grid(row=0, column=0)
        L_password.grid(row=1, column=0)
        self.E_name.grid(row=0, column=1)
        self.E_password.grid(row=1, column=1)
        B_login.grid(row=2,column=1)
        B_signup.grid(row=2, column=2)
        B_remember.grid(row=3)
        L_remtext.grid(row=3,column=1)

    def auth_login(self):
        authName = self.E_name.get() + "," + self.E_password.get()
        file = open("logins", "r")

        file.close()

class SignupScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.L_name = tk.Label(self, text = "Name")
        self.L_password = tk.Label(self, text="Password")
        self.L_password2 = tk.Label(self, text="Confirm Password")
        self.E_name = tk.Entry(self)
        self.E_password = tk.Entry(self)
        self.E_password2 = tk.Entry(self)
        self.B_login = tk.Button(self, text="Register", command = self.check)

        self.L_name.grid(row=0)
        self.L_password.grid(row=1)
        self.L_password2.grid(row=2)
        self.E_name.grid(row =0, column=1)
        self.E_password.grid(row=1, column=1)
        self.E_password2.grid(row=2, column=1)
        self.B_login.grid(row=3, column=1)

    def save_user(self):
        file = open("logins", "w")
        file.write(self.E_name.get() + "," + self.E_password.get())
        file.close()

    def check(self):
        name = self.E_name.get()
        password = self.E_password.get()
        password2 = self.E_password2.get()

        if(len(name)<3):
            L_nameTooShort = tk.Label(self, "Username too short, please try again")
            L_nameTooShort.grid(row=4)
        else:
            if(password != password2):
                L_passDontMatch = tk.Label(self, "Passwords dont match, please try again")
                L_passDontMatch.grid(row=4)
            else:
                if(len(password) < 6):
                    L_passTooShort= tk.Label(self, "Password too short, please try again")
                    L_passTooShort.grid(row=4)
                else:
                    self.save_user()
                    self.controller.show_frame(Home)


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        L_welcome = tk.Label(self, text="welcome weak heart niggas")
        L_welcome.pack()


app = Main()
app.mainloop()
