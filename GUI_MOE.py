import tkinter as tk #importing tkinter library

class WelcomeScreen:    #First window you see

    def __init__(self, master): #must define init function when you make a class, takes parameters 'master'
                           # (which is the 'master' window, thefirst window you see...... 'self' is always there, can explain more in person
        self.master = master
        self.B_signin = tk.Button(master, text="Sign in", command=self.SignIn_Check) #Creating button, go to 'SignIn_Button' function
        self.B_signin.grid(row=4, column=2)
        self.B_signin.config(font=("Times",15, "bold"), width=7)
        self.L_uname = tk.Label(master, text="Username:", bg="white")
        self.L_uname.grid(row=2,column=1)   #creating label with text
        self.L_uname.config(font=("Times", 15, "bold", "italic"))
        self.E_uname = tk.Entry(master)    #creating entry where users enter text
        self.E_uname.grid(row=2, column=2) #placing entry in row 2 and column 2 of window
        self.E_uname.config(highlightthickness = 5)
        self.L_pass = tk.Label(master, text="Password:", bg="white")
        self.L_pass.grid(row=3,column=1)
        self.L_pass.config(font=("Times", 15, "bold", "italic"))
        self.E_pass = tk.Entry(master)
        self.E_pass.grid(row=3, column=2)
        self.E_pass.config(highlightthickness = 5)
        self.E_pass.config(show="*") #make password show up as stars not characters
        self.button2 = tk.Button(master, text="Register", command= self.Register_Instance)
        self.button2.grid(row=4, column=3)
        self.button2.config(font=("Times",15, "bold"), width=7)
        self.label = tk.Label(master, text="Welcome\nPlease sign in or register", fg="red", bg="white")
        self.label.grid(row=0,column=2)
        self.label.config(font=("Comic Sans MS", 20))
        master.wm_title("Pacemaker")
        photo = tk.PhotoImage(file="heart_Rate.gif")
        photo.configure()
        label = tk.Label(self.master, image=photo)
        label.image = photo
        #label.grid(row=5, columnspan=10)
        master.geometry("500x450")
        master.configure(background="white")


    def SignIn_Check(self):    #function called when SignIn_Button is pressed

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
                    self.SignIn_Instance() #go to this function
                    break
            if auth == False:           #if u fucked up username or password
                blank.grid(row=1, column=2)
                tk.Label(self.master, text="Wrong Username or Password\nPlease try again", fg="red").grid(row=1, column=2)


        except FileNotFoundError:   #if u try to sign in and there's no mandems registered
            tk.Label(self.master, text="No users have been registered\nplease register then sign in", fg="red").grid(row=1, column=2)


    def Register_Instance(self):                  #make a new window when register button is pressed and create an instance of the class 'Register_Window'
        window = tk.Toplevel()
        R_window = Register_Window(window)

    def SignIn_Instance(self):        #make a new window when sign in button is pressed and create an instance of the class 'SignIn_Window'
        self.master.wm_state('iconic')
        window = tk.Toplevel()
        S_window = SignIn_Window(window)


class SignIn_Window:



    def __init__(self,slave):
        tk.Label(slave, text = "Please select a pacing mode", fg ="red").grid(row=0, columnspan=3)
        tk.Label(slave, text ="").grid(row=1,columnspan=3)
        tk.Button(slave, text="AOO", fg="blue", command = self.AOO_Instance).grid(row=2, column = 0)
        tk.Button(slave, text="VOO", fg="blue", command = self.VOO_Instance).grid(row=2, column = 1)

    def LRL_Values(self): #creating list to store the allowed range of values for Lower Rate Limit
        self.values = []
        i = 30
        while i <= 45:
            self.values.append(i)
            i = i + 5
        while i <= 89:
            self.values.append(i)
            i += 1
        while i <= 175:
            self.values.append(i)
            i = i + 5
        self.default = tk.StringVar()       #declaring variable
        self.default.set(self.values[14])   #setting the nominal value (as defined in PACEMAKER document, to be displayed as a default value)

        ##all other functions do the same thing for different parameters

    def URL_Values(self):
        self.values = []
        i = 50
        while i<=175:
            self.values.append(i)
            i = i + 5
        self.default=tk.StringVar()
        self.default.set(self.values[14])

    def Amplitude(self):
        self.values = []
        for i in range(5,33):
            self.values.append(float(i)/10)
        i = 3.5
        while i<=7.0:
            self.values.append(i)
            i = i + 0.5
        self.default=tk.StringVar()
        self.default.set(self.values[28])

    def Width(self):
        self.values = []
        for i in range(1,20):
            self.values.append(float(i)/10)
        self.default=tk.StringVar()
        self.default.set(self.values[3])

    def AOO_Instance(self):
        window = tk.Toplevel()
        instance = AOO_Window(window)  #creating instance of AOO_Window ( see below )

    def VOO_Instance(self):
        window = tk.Toplevel()
        instance = VOO_Window(window)

class AOO_Window(SignIn_Window):

    def __init__(self, slave):      #self explanatory !! each block makes a label, called the function that has the labels stored in it
                                    #and creates the dropdown menu!!
        tk.Label(slave, text="Please enter parameter values", fg="green").grid(row=0, columnspan=4)
        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)\n(Default = Nominal Value)").grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2,column=2)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)\n(Default = Nominal Value)").grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4,column=2)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)\n(Default = Nominal Value)").grid(row=6, column=0)
        tk.OptionMenu(slave, self.default,"OFF", *self.values).grid(row=6,column=2)

        self.Width()
        tk.Label(slave, text="Width (ms)\n(Default = Nominal Value)").grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=8, column=2)


class VOO_Window(SignIn_Window):

    def __init__(self, slave):
            tk.Label(slave, text="Please enter parameter values", fg="green").grid(row=0, columnspan=4)
            self.LRL_Values()
            tk.Label(slave, text="Lower Rate Limit (PPM)\n(Default = Nominal Value)").grid(row=2, column=0)
            tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)

            self.URL_Values()
            tk.Label(slave, text="Upper Rate Limit (PPM)\n(Default = Nominal Value)").grid(row=4, column=0)
            tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)

            self.Amplitude()
            tk.Label(slave, text="Amplitude (V)\n(Default = Nominal Value)").grid(row=6, column=0)
            tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=6, column=2)

            self.Width()
            tk.Label(slave, text="Width (ms)\n(Default = Nominal Value)").grid(row=8, column=0)
            tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=8, column=2)

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