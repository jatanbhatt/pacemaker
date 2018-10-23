#if something is not commented, it was commenting earlier in a similar format so check the code!!


import tkinter as tk    #importing tkinter library


class WelcomeScreen:    #First window you see

    def __init__(self, master): #must define init function when you make a class, takes parameters 'master'
                            # (which is the 'master' window, thefirst window you see...... 'self' is always there, can explain more in person
        self.master = master
        self.B_signin = tk.Button(master, text="Sign in", command=self.SignIn_Button).grid(row=5, column=2) #Creating button, go to 'SignIn_Button' function
                                                                                                            # when pressed
        self.L_uname = tk.Label(master, text="Username:").grid(row=2,column=1)   #creating label with text
        self.E_uname = tk.Entry(master)    #creating entry where users enter text
        self.E_uname.grid(row=2, column=2) #placing entry in row 2 and column 3 of window
        self.L_pass = tk.Label(master, text="Password:").grid(row=3,column=1)
        self.E_pass = tk.Entry(master)
        self.E_pass.grid(row=3, column=2)
        self.E_pass.config(show="*") #make password show up as stars not characters
        self.button2 = tk.Button(master, text="Register", command= self.Register_Button).grid(row=5, column=3)
        self.label = tk.Label(master, text="Welcome\nPlease sign in or register").grid(row=1,column=2)

    def SignIn_Button(self):    #function called when SignIn_Button is pressed

        uname = tk.Entry.get(self.E_uname)  #get user entry and store in 'uname'
        pass1 = tk.Entry.get(self.E_pass)
        blank = tk.Label(self.master, text="\t\t\t\t")  #blank text to get rid of any previous text, you'll see it's use below
        try:
            f = open("Registration_File.txt", "r+")     #try to open the file if it exists
            auth = False    #initialize this to false, you'll see why a few lines down
            for lines in f: #read file line by line
                split = lines.split()   #split lines word by word, now they're stored in a list
                if split[0] == uname and split[1] == pass1: #check if user entry is the same as what is saved in the file
                    auth = True                             #authentication is verified
                    #S_window = tk.Toplevel()
                    #blank.grid(row=0)
                    #tk.Label(S_window, text="If you're reading this it's not too late to drop out").grid(row=0)
                    #self.master.after(100, self.minimize_M)
                    SignIn_Button() #go to this function
                    break
            if auth == False:           #if u fucked up username or password
                blank.grid(row=1, column=2)
                tk.Label(self.master, text="Wrong Username or Password\nPlease try again", fg="red").grid(row=1, column=2)


        except FileNotFoundError:   #if u try to sign in and there's no mandems registered
            blank.grid(row=1)
            tk.Label(self.master, text="No users have been registered\nplease register then sign in", fg="red").grid(row=1, column=2)


    def Register_Button(self):                  #make a new window when register button is pressed and create an instance of the class 'Register_Window'
        window = tk.Toplevel()
        R_window = Register_Window(window)

    def SignIn_Button(self):        #make a new window when sign in button is pressed and create an instance of the class 'SignIn_Window'
        window = tk.Toplevel()
        S_window = SignIn_Window(window)


class SignIn_Window:
    def __init__(self, slave):
        blank = tk.Label(slave, text="\t\t\t\t\t\t\t")      #blank
        blank.grid(row=0)
        tk.Label(slave, text="If you're reading this it's not too late to drop out").grid(row=0) #for now it just displays this
        #self.master.after(100, self.minimize_M)


class Register_Window:
    def __init__(self,slave): #slave is just not the master window, it's a sub-window or a slave-window
                                #everything is explained above this should be self explanatory
        self.slave = slave
        tk.Label(slave, text="******REGISTRATION******", fg="green").grid(row=0)
        tk.Label(slave, text = "Enter USERNAME (Must include at least one number and be at least 6 characters)").grid(row=1)
        self.E_uname = tk.Entry(slave)
        self.E_uname.grid(row=1, column = 1)
        tk.Label(slave, text="Enter PASSWORD (Must include at least one number and be at least 6 characters").grid(row=2)
        self.E_pass1 = tk.Entry(slave)
        self.E_pass1.config(show="*")
        self.E_pass1.grid(row=2, column = 1)
        tk.Label(slave, text="Re-enter password").grid(row=3)
        self.E_pass2 = tk.Entry(slave)
        self.E_pass2.config(show="*")
        self.E_pass2.grid(row=3, column=1)
        tk.Button(slave, text="Register",command=self.Register_Check).grid(row=4, column=1)

    def minimize_R(self):
        self.slave.wm_state('iconic')

    def Register_Check(self):
        uname = tk.Entry.get(self.E_uname)              #initializing variables based on user entry
        pass1 = tk.Entry.get(self.E_pass1)
        pass2 = tk.Entry.get(self.E_pass2)
        blank = tk.Label(self.slave, text="\t\t\t\t\t\t\t")
        if any(char.isdigit() for char in uname) and len(uname)>=6 and pass1==pass2:        #requirements to register
            try:
                f = open("Registration_File.txt", "r+")
                count = 0
                for line in f:
                    count+=1                #this entire for loop first checks if too many manz are registered
                                            #then checks if username is available
                                            #if all is good, register
                if count >= 11:
                    blank.grid(row=4)
                    overflow = tk.Label(self.slave, text = "Error: Too many people registered", fg="red")
                    overflow.grid(row=4)
                else:
                    f.seek(0)
                    same = False
                    for line in f:
                        split = line.split()
                        if split[0] == uname:
                            same = True
                            blank.grid(row=4)
                            tk.Label(self.slave, text="Username is taken, try another", fg="red").grid(row=4)
                            break
                    if same == False:
                        f.close()
                        f = open("Registration_File.txt", "a+")
                        f.write("%s   %s\n" % (uname, pass1))
                        f.close()
                        blank.grid(row=4)
                        tk.Label(self.slave, text="Registration Successful!", fg="blue").grid(row=4)
                        self.slave.after(1000, self.minimize_R)

            except FileNotFoundError:
                f = open("Registration_File.txt", "a+")     #if file is not found, open it and register and print to "Registration_File" to save uname and pass
                f.write("Username Password\n")
                f.write("%s   %s\n" % (uname, pass1))
                f.close()
                blank.grid(row=4)
                tk.Label(self.slave, text="Registration Successful!", fg="blue").grid(row=4)
                self.slave.after(1000, self.minimize_R)
        elif pass1!=pass2:
            blank.grid(row=4)
            tk.Label(self.slave, text="Passwords are not the same, registration unsuccessful", fg="red").grid(row=4)
        elif len(uname)<6:
            blank.grid(row=4)
            tk.Label(self.slave, text="Username is too short, registration unsuccessful", fg="red").grid(row=4)
        else:
            blank.grid(row=4)
            tk.Label(self.slave, text="No digit in username, registration unsuccessful", fg="red").grid(row=4)





def main():
    master = tk.Tk()
    x = WelcomeScreen(master)
    master.mainloop()

main()