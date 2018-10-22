import tkinter as tk
import time

class WelcomeScreen:

    def __init__(self, master):
        self.B_signin = tk.Button(master, text="Sign in", command=self.SignIn_Button).grid(row=5, column=2)
        self.L_uname = tk.Label(master, text="Username:").grid(row=2,column=1)
        self.E_uname = tk.Entry(master)
        self.E_uname.grid(row=2, column=2)
        self.L_pass = tk.Label(master, text="Password:").grid(row=3,column=1)
        self.E_pass = tk.Entry(master)
        self.E_pass.grid(row=3, column=2)
        self.E_pass.config(show="*")
        self.button2 = tk.Button(master, text="Register", command= self.Register_Button).grid(row=5, column=3)
        self.label = tk.Label(master, text="Welcome\nPlease sign in or register").grid(row=1,column=2)

    def minimize_R(self):
        self.R_window.wm_state('iconic')
    def minimize_M(self):
        master.wm_state('iconic')

    def Register_Button(self):
        self.R_window = tk.Toplevel()
        tk.Label(self.R_window, text="******REGISTRATION******", fg="green").grid(row=0)
        tk.Label(self.R_window, text = "Enter USERNAME (Must include at least one number and be at least 6 characters)").grid(row=1)
        self.E_uname = tk.Entry(self.R_window)
        self.E_uname.grid(row=1, column = 1)
        tk.Label(self.R_window, text="Enter PASSWORD (Must include at least one number and be at least 6 characters").grid(row=2)
        self.E_pass1 = tk.Entry(self.R_window)
        self.E_pass1.config(show="*")
        self.E_pass1.grid(row=2, column = 1)
        tk.Label(self.R_window, text="Re-enter password").grid(row=3)
        self.E_pass2 = tk.Entry(self.R_window)
        self.E_pass2.config(show="*")
        self.E_pass2.grid(row=3, column=1)
        tk.Button(self.R_window, text="Register",command=self.Register_Check).grid(row=4, column=1)

    def Register_Check(self):
        uname = tk.Entry.get(self.E_uname)
        pass1 = tk.Entry.get(self.E_pass1)
        pass2 = tk.Entry.get(self.E_pass2)
        blank = tk.Label(self.R_window, text="\t\t\t\t\t\t\t")
        if any(char.isdigit() for char in uname) and len(uname)>=6 and pass1==pass2:
            try:
                f = open("Registration_File.txt", "r+")
                count = 0
                for line in f:
                    count+=1
                if count >= 11:
                    blank.grid(row=4)
                    overflow = tk.Label(self.R_window, text = "Error: Too many people registered", fg="red")
                    overflow.grid(row=4)
                else:
                    f.seek(0)
                    same = False
                    for line in f:
                        split = line.split()
                        if split[0] == uname:
                            same = True
                            blank.grid(row=4)
                            tk.Label(self.R_window, text="Username is taken, try another", fg="red").grid(row=4)
                            break
                    if same == False:
                        f.close()
                        f = open("Registration_File.txt", "a+")
                        f.write("%s   %s\n" % (uname, pass1))
                        f.close()
                        blank.grid(row=4)
                        tk.Label(self.R_window, text="Registration Successful!", fg="blue").grid(row=4)
                        self.R_window.after(1000, self.minimize_R)

            except FileNotFoundError:
                f = open("Registration_File.txt", "a+")
                f.write("Username Password\n")
                f.write("%s   %s\n" % (uname, pass1))
                f.close()
                blank.grid(row=4)
                tk.Label(self.R_window, text="Registration Successful!", fg="blue").grid(row=4)
                self.R_window.after(1000, self.minimize_R)
        elif pass1!=pass2:
            blank.grid(row=4)
            tk.Label(self.R_window, text="Passwords are not the same, registration unsuccessful", fg="red").grid(row=4)
        elif len(uname)<6:
            blank.grid(row=4)
            tk.Label(self.R_window, text="Username is too short, registration unsuccessful", fg="red").grid(row=4)
        else:
            blank.grid(row=4)
            tk.Label(self.R_window, text="No digit in username, registration unsuccessful", fg="red").grid(row=4)

    def SignIn_Button(self):

        uname = tk.Entry.get(self.E_uname)
        pass1 = tk.Entry.get(self.E_pass)
        blank = tk.Label(master, text="\t\t\t\t")
        try:
            f = open("Registration_File.txt", "r+")
            auth = False
            for lines in f:
                split = lines.split()
                if split[0] == uname and split[1] == pass1:
                    auth = True
                    S_window = tk.Toplevel()
                    blank.grid(row=0)
                    tk.Label(S_window, text = "If you're reading this it's not too late to drop out").grid(row=0)
                    master.after(100, self.minimize_M)

                    break
            if auth == False:
                blank.grid(row=1,column=2)
                tk.Label(master, text="Wrong Username or Password\nPlease try again", fg="red").grid(row=1, column=2)


        except FileNotFoundError:
            blank.grid(row=1)
            tk.Label(master, text="No users have been registered\nplease register then sign in", fg="red").grid(row=1,column=2)



master = tk.Tk()
x = WelcomeScreen(master)
master.mainloop()