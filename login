import tkinter as tk


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)

        window.pack(side="top", fill="both", expand=True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginScreen, Home):
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
        E_name = tk.Entry(self)
        E_password = tk.Entry(self)
        B_login = tk.Button(self, text="Login")
        B_signup = tk.Button(self, text="Signup")
        B_remember = tk.Checkbutton(self)
        L_remtext = tk.Label(self, text="Remember Me")

        L_name.grid(row=0, column=0)
        L_password.grid(row=1, column=0)
        E_name.grid(row=0, column=1)
        E_password.grid(row=1, column=1)
        B_login.grid(row=2,column=1)
        B_signup.grid(row=2, column=2)
        B_remember.grid(row=3)
        L_remtext.grid(row=3,column=1)
    #def auth_login(self):




class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        L_welcome = tk.Label(self, text="welcome weak heart niggas")
        L_welcome.pack()


app = Main()
app.mainloop()
