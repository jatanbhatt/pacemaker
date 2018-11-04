import tkinter as tk #importing tkinter library

class WelcomeScreen:    #First window you see

    def __init__(self, master): #must define init function when you make a class, takes parameters 'master'
                           # (which is the 'master' window, the first window that appears)
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
        self.label.config(font=("Times", 20))
        master.wm_title("Pacemaker")
        photo = tk.PhotoImage(file="heart_Rate.gif")     #This code is not required and is used for demonstration purposes during the lab (requires a local file)
        photo.configure()
        label = tk.Label(self.master, image=photo)
        label.image = photo
        label.grid(row=5, columnspan=10)
        master.geometry("500x450")
        master.configure(background="white")


    def SignIn_Check(self):    #function called when SignIn_Button is pressed

        uname = tk.Entry.get(self.E_uname)  #get user entry and store in 'uname'
        pass1 = tk.Entry.get(self.E_pass)
        blank = tk.Label(self.master, text="\t\t\t\t")  #blank text to get rid of any previous text, you'll see it's use below

        try:
            f = open("Registration_File.txt", "r+")     #try to open the file if it exists
            auth = False    #initialized to false, which is default authorization until uname and pass are proven to be correct
            for lines in f: #read file line by line
                split = lines.split()   #split lines word by word, now they're stored in a list
                if split[0] == uname and split[1] == pass1: #check if user entry is the same as what is saved in the file
                    auth = True                             #authentication is verified
                    self.SignIn_Instance() #go to this function
                    break
            if auth == False:           #if username or password is incorrect
                blank.grid(row=1, column=2)
                tk.Label(self.master, text="Wrong Username or Password\nPlease try again", fg="red").grid(row=1, column=2)


        except FileNotFoundError:   #if file is not found, no users have been registered
            tk.Label(self.master, text="No users have been registered\nplease register then sign in", fg="red").grid(row=1, column=2)


    def Register_Instance(self):      #make a new window when register button is pressed and create an instance of the class 'Register_Window'
        window = tk.Toplevel()
        R_window = Register_Window(window)

    def SignIn_Instance(self):        #make a new window when sign in button is pressed and create an instance of the class 'SignIn_Window'
        self.master.wm_state('iconic')
        window = tk.Toplevel()
        S_window = SignIn_Window(window)

class Register_Window:
    def __init__(self,slave): #slave is not the master window, it's a sub-window or a slave-window

        self.slave = slave
        L_title = tk.Label(slave, text="******REGISTRATION******", fg="green")
        L_title.grid(row=0)
        L_title.configure(font=("Times", 15, "bold", "italic"))
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
        L_button = tk.Button(slave, text="Register", fg="red", command=self.Register_Check)
        L_button.grid(row=4, column=1)
        L_button.configure(font=("Times", 15, "bold"))

    def minimize_R(self):
        self.slave.wm_state('iconic')

    def Register_Check(self):
        uname = tk.Entry.get(self.E_uname)              #initializing variables based on user entry
        pass1 = tk.Entry.get(self.E_pass1)
        pass2 = tk.Entry.get(self.E_pass2)
        blank = tk.Label(self.slave, text="\t\t\t\t\t\t\t")
        if any(char.isdigit() for char in uname) and len(uname)>=6 and pass1==pass2 and len(pass1)>=6 and any(char.isdigit() for char in pass1):      #requirements to register
            try:
                f = open("Registration_File.txt", "r+")
                count = 0
                for line in f:
                    count+=1                #entire for loop first checks if too many user are registered
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
                f = open("Registration_File.txt", "a+")     #if file is not found, create the registraion file and write uname and pass to file
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
        elif len(pass1)<6:
            blank.grid(row=4)
            tk.Label(self.slave, text="Password is too short, registration unsuccessful", fg="red").grid(row=4)
        elif any(char.isdigit() for char in uname) != True:
            blank.grid(row=4)
            tk.Label(self.slave, text="No digit in username, registration unsuccessful", fg="red").grid(row=4)
        else:
            blank.grid(row=4)
            tk.Label(self.slave, text="No digit is password, registration unsuccessful", fg="red").grid(row=4)

class SignIn_Window:

    def __init__(self,slave):
        L_title = tk.Label(slave, text = "Please select a pacing mode", fg ="red")
        L_title.grid(row=0, columnspan=3)
        L_title.configure(font=("Times", 15, "bold", "italic"))
        tk.Label(slave, text="").grid(row=1)
        tk.Button(slave, text="AOO", fg="blue", command=self.AOO_Instance).grid(row=2, column=0)
        tk.Button(slave, text="VOO", fg="blue", command=self.VOO_Instance).grid(row=2, column=1)
        tk.Button(slave, text="AAT", fg="blue", command=self.AAT_Instance).grid(row=2, column=2)
        tk.Label(slave, text="").grid(row=3)
        tk.Button(slave, text="VVT", fg="blue", command=self.VVT_Instance).grid(row=4, column=0)
        tk.Button(slave, text="AAI", fg="blue", command=self.AAI_Instance).grid(row=4, column=1)
        tk.Button(slave, text="VVI", fg="blue", command=self.VVI_Instance).grid(row=4, column=2)
        tk.Label(slave, text="").grid(row=5)
        tk.Button(slave, text="VDD", fg="blue", command=self.VDD_Instance).grid(row=6, column=0)
        tk.Button(slave, text="DOO", fg="blue", command=self.DOO_Instance).grid(row=6, column=1)
        tk.Button(slave, text="DDI", fg="blue", command=self.DDI_Instance).grid(row=6, column=2)
        tk.Label(slave, text="").grid(row=7)
        tk.Button(slave, text="DDD", fg="blue", command=self.DDD_Instance).grid(row=8, column=0)
        tk.Button(slave, text="AOOR", fg="blue", command=self.AOOR_Instance).grid(row=8, column=1)
        tk.Button(slave, text="AAIR", fg="blue", command=self.AAIR_Instance).grid(row=8, column=2)
        tk.Label(slave, text="").grid(row=9)
        tk.Button(slave, text="VOOR", fg="blue", command=self.VOOR_Instance).grid(row=10, column=0)
        tk.Button(slave, text="VVIR", fg="blue", command=self.VVIR_Instance).grid(row=10, column=1)
        tk.Button(slave, text="VDDR", fg="blue", command=self.VDDR_Instance).grid(row=10, column=2)
        tk.Label(slave, text="").grid(row=11)
        tk.Button(slave, text="DOOR", fg="blue", command=self.DOOR_Instance).grid(row=12, column=0)
        tk.Button(slave, text="DDIR", fg="blue", command=self.DDIR_Instance).grid(row=12, column=1)
        tk.Button(slave, text="DDDR", fg="blue", command=self.DDDR_Instance).grid(row=12, column=2)




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

    def Sensitivity(self):
        self.values = [0.25, 0.5, 0.75]
        i=1.0
        while i<=10.0:
            self.values.append(i)
            i = i + 0.5
        self.A_default=tk.StringVar()
        self.A_default.set(self.values[2])
        self.V_default=tk.StringVar()
        self.V_default.set(self.values[6])

    def Refractory(self):
        self.values = []
        i=150
        while i <=500:
            self.values.append(i)
            i = i + 10
        self.A_default=tk.StringVar()
        self.A_default.set(self.values[10])
        self.V_default=tk.StringVar()
        self.V_default.set(self.values[17])

    def PVARP(self):
        self.values = []
        i = 150
        while i <= 500:
            self.values.append(i)
            i = i + 10
        self.default = tk.StringVar()
        self.default.set(self.values[10])

    def Hysteresis(self):
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
        self.default = tk.StringVar()
        self.default.set("OFF")

    def Smoothing(self):
        self.values = []
        i=3
        while i<=21:
            self.values.append(i)
            i = i + 3
        self.values.append(25)
        self.default = tk.StringVar()
        self.default.set("OFF")

    def F_Delay(self):
        self.values = []
        i=70
        while i<=300:
            self.values.append(i)
            i = i + 10
        self.default = tk.StringVar()
        self.default.set(self.values[8])

    def D_Delay(self):
        self.values = ["OFF", "ON"]
        self.default = tk.StringVar()
        self.default.set(self.values[0])

    def PVARP_E(self):
        self.values = ["OFF"]
        i = 50
        while i<=400:
            self.values.append(i)
            i = i + 50
        self.default = tk.StringVar()
        self.default.set(self.values[0])

    def ATR_Duration(self):
        self.values = [10]
        i = 20
        while i<=80:
            self.values.append(i)
            i = i + 20
        i = 100
        while i<=2000:
            self.values.append(i)
            i = i + 100

        self.default = tk.StringVar()
        self.default.set(self.values[1])

    def ATR_Fallback_Mode(self):
        self.values = ["OFF", "ON"]

        self.default = tk.StringVar()
        self.default.set(self.values[0])

    def ATR_Fallback_Time(self):
        self.values = [1,2,3,4,5]

        self.default = tk.StringVar()
        self.default.set(self.values[0])

    def S_Delay_Offset(self):
        self.values = ["OFF"]
        i = -10
        while i>=-100:
            self.values.append(i)
            i = i - 10
        self.default = tk.StringVar()
        self.default.set(self.values[1])

    def Max_Sensor_Rate(self):
        self.values = []
        i=50
        while i<=175:
            self.values.append(i)
            i = i + 5
        self.default = tk.StringVar()
        self.default.set(self.values[14])

    def Threshold(self):
        self.values = ["V-Low", "Low", "Med-Low", "Med", "Med-High","High", "V-High"]
        self.default = tk.StringVar()
        self.default.set(self.values[3])

    def Reaction_Time(self):
        self.values = [10,20,30,40,50]

        self.default = tk.StringVar()
        self.default.set(self.values[2])

    def R_Factor(self):
        self.values = []
        i=1
        while i<=16:
            self.values.append(i)
            i = i + 1

        self.default = tk.StringVar()
        self.default.set(self.values[7])

    def Recovery_Time(self):
        self.values = []
        i = 2
        while i<=16:
            self.values.append(i)
            i = i + 1

        self.default = tk.StringVar()
        self.default.set(self.values[3])






    def AOO_Instance(self):
        window = tk.Toplevel()
        instance = AOO_Window(window)  #creating instance of AOO_Window ( see below )

    def VOO_Instance(self):
        window = tk.Toplevel()
        instance = VOO_Window(window)  #creating instance of VOO_Window ( see below )

    def AAT_Instance(self):
        window = tk.Toplevel()
        instance = AAT_Window(window)  #creating instance of AAT Window ( see below )

    def VVT_Instance(self):
        window = tk.Toplevel()
        instance = VVT_Window(window)

    def AAI_Instance(self):
        window = tk.Toplevel()
        instance = AAI_Window(window)

    def VVI_Instance(self):
        window = tk.Toplevel()
        instance = VVI_Window(window)

    def VDD_Instance(self):
        window = tk.Toplevel()
        instance = VDD_Window(window)

    def DOO_Instance(self):
        window = tk.Toplevel()
        instance = DOO_Window(window)

    def DDI_Instance(self):
        window = tk.Toplevel()
        instance = DDI_Window(window)

    def DDD_Instance(self):
        window = tk.Toplevel()
        instance = DDD_Window(window)

    def AOOR_Instance(self):
        window = tk.Toplevel()
        instance = AOOR_Window(window)

    def AAIR_Instance(self):
        window = tk.Toplevel()
        instance = AAIR_Window(window)

    def VOOR_Instance(self):
        window = tk.Toplevel()
        instance = VOOR_Window(window)

    def VVIR_Instance(self):
        window = tk.Toplevel()
        instance = VVIR_Window(window)

    def VDDR_Instance(self):
        window = tk.Toplevel()
        instance = VDDR_Window(window)

    def DOOR_Instance(self):
        window = tk.Toplevel()
        instance = DOOR_Window(window)

    def DDIR_Instance(self):
        window = tk.Toplevel()
        instance = DDIR_Window(window)

    def DDDR_Instance(self):
        window = tk.Toplevel()
        instance = DDDR_Window(window)




class AOO_Window(SignIn_Window):

    def __init__(self, slave):      #each block makes a label, calls the function that contains the appropriate list
                                    #and creates a dropdown menu
        L_title = tk.Label(slave, text="Please enter parameter values for AOO pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default,"OFF", *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=8, column=2)

        tk.Label(slave, text="\t\t\t\t").grid(row=9)
        cur_device = tk.Label(slave, text="Current pacemaker device: PACEMAKER")
        cur_device.grid(row=10, columnspan=3)
        cur_device.config(font=("Helvetica", "12", "bold", "italic", "underline"))
        comm = tk.Label(slave, text="No communication with PACEMAKER device")
        comm.grid(row=12, columnspan=3)
        comm.config(font=("Helvetica", "12", "bold", "italic", "underline"))

class VOO_Window(SignIn_Window):

    def __init__(self, slave):
            L_title = tk.Label(slave, text="Please enter parameter values for VOO pacing mode\n(Default = Nominal Value)", fg="green")
            L_title.grid(row=0, columnspan=4)
            L_title.configure(font=("Times", 15, "bold", "italic"))

            self.LRL_Values()
            tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
            tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
            tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

            self.URL_Values()
            tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
            tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
            tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

            self.Amplitude()
            tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
            tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=6, column=2)
            tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

            self.Width()
            tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
            tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=8, column=2)

            tk.Label(slave, text="\t\t\t\t").grid(row=9)
            cur_device = tk.Label(slave, text="Current pacemaker device: PACEMAKER")
            cur_device.grid(row=10, columnspan=3)
            cur_device.config(font=("Helvetica", "12", "bold", "italic", "underline"))
            comm = tk.Label(slave, text="No communication with PACEMAKER device")
            comm.grid(row=12, columnspan=3)
            comm.config(font=("Helvetica", "12", "bold", "italic", "underline"))

class AAT_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for AAT pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height = 1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Sensitivity()
        tk.Label(slave, text="Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Refractory()
        tk.Label(slave, text="Atrial Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.PVARP()
        tk.Label(slave, text="PVARP (ms)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=2)

class VVT_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for VVT pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Sensitivity()
        tk.Label(slave, text="Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Refractory()
        tk.Label(slave, text="Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=12, column=2)

class AAI_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for AAI pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Sensitivity()
        tk.Label(slave, text="Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Refractory()
        tk.Label(slave, text="Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.PVARP()
        tk.Label(slave, text="PVARP (ms)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Hysteresis()
        tk.Label(slave, text="Hysteresis (PPM)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.Smoothing()
        tk.Label(slave, text="Rate Smoothing (%)", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=18, column=2)

class VVI_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for VVI pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Sensitivity()
        tk.Label(slave, text="Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Refractory()
        tk.Label(slave, text="Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Hysteresis()
        tk.Label(slave, text="Hysteresis (PPM)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Smoothing()
        tk.Label(slave, text="Rate Smoothing (%)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=16, column=2)

class VDD_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for VDD pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.F_Delay()
        tk.Label(slave, text="Fixed Delay (ms)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.D_Delay()
        tk.Label(slave, text="Dynamic Delay", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Sensitivity()
        tk.Label(slave, text="Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Refractory()
        tk.Label(slave, text="Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.PVARP_E()
        tk.Label(slave, text="PVARP Extension (ms)", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=18, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=19)

        self.Smoothing()
        tk.Label(slave, text="Rate Smoothing (%)", font=("Helvetica", 10, "bold")).grid(row=20, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=20, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=21)

        self.ATR_Duration()
        tk.Label(slave, text="ATR Duration (cardiac cycles)", font=("Helvetica", 10, "bold")).grid(row=22, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=22, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=23)

        self.ATR_Fallback_Mode()
        tk.Label(slave, text="ATR Fallback Mode", font=("Helvetica", 10, "bold")).grid(row=24, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=24, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=25)

        self.ATR_Fallback_Time()
        tk.Label(slave, text="ATR Fallback Time (min)", font=("Helvetica", 10, "bold")).grid(row=26, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=26, column=2)

class DOO_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for DOO pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.F_Delay()
        tk.Label(slave, text="Fixed Delay (ms)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Amplitude()
        tk.Label(slave, text="Atrial Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Width()
        tk.Label(slave, text="Atrial Width (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Amplitude()
        tk.Label(slave, text="Ventrical Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Width()
        tk.Label(slave, text="Ventrical Width (ms)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=14, column=2)

class DDI_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for DDI pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.F_Delay()
        tk.Label(slave, text="Fixed Delay (ms)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Amplitude()
        tk.Label(slave, text="Atrial Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Width()
        tk.Label(slave, text="Atrial Width (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Amplitude()
        tk.Label(slave, text="Ventrical Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Width()
        tk.Label(slave, text="Ventrical Width (ms)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Sensitivity()
        tk.Label(slave, text="Atrial Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.Refractory()
        tk.Label(slave, text="Atrial Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=18, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=19)

        self.Sensitivity()
        tk.Label(slave, text="Ventrical Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=20, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=20, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=21)

        self.Refractory()
        tk.Label(slave, text="Ventrical Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=22, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=22, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=23)

        self.PVARP()
        tk.Label(slave, text="PVARP (ms)", font=("Helvetica", 10, "bold")).grid(row=24, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=24, column=2)

class DDD_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for DDD pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.F_Delay()
        tk.Label(slave, text="Fixed Delay (ms)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.D_Delay()
        tk.Label(slave, text="Dynamic Delay", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.S_Delay_Offset()
        tk.Label(slave, text="Sensed Delay Offset (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Amplitude()
        tk.Label(slave, text="Atrial Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Width()
        tk.Label(slave, text="Atrial Width (ms)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Amplitude()
        tk.Label(slave, text="Ventrical Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.Width()
        tk.Label(slave, text="Ventrical Width (ms)", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=18, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=19)

        self.Sensitivity()
        tk.Label(slave, text="Atrial Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=20, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=20, column=2)

        self.Refractory()
        tk.Label(slave, text="Atrial Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=2, column=3)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=2, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3, column=3)

        self.Sensitivity()
        tk.Label(slave, text="Ventrical Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=4, column=3)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=4, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5, column=3)

        self.Refractory()
        tk.Label(slave, text="Ventrical Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=6, column=3)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=6, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7, column=3)

        self.PVARP()
        tk.Label(slave, text="PVARP (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9, column=3)

        self.PVARP_E()
        tk.Label(slave, text="PVARP Extension (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=10, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11, column=3)

        self.Hysteresis()
        tk.Label(slave, text="Hysteresis (PPM)", font=("Helvetica", 10, "bold")).grid(row=12, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=12, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13, column=3)

        self.Smoothing()
        tk.Label(slave, text="Rate Smoothing (%)", font=("Helvetica", 10, "bold")).grid(row=14, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=14, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15, column=3)

        self.ATR_Duration()
        tk.Label(slave, text="ATR Duration (cardiac cycles)", font=("Helvetica", 10, "bold")).grid(row=16, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=16, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17, column=3)

        self.ATR_Fallback_Mode()
        tk.Label(slave, text="ATR Fallback Mode", font=("Helvetica", 10, "bold")).grid(row=18, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=18, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=19, column=3)

        self.ATR_Fallback_Time()
        tk.Label(slave, text="ATR Fallback Time (min)", font=("Helvetica", 10, "bold")).grid(row=20, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=20, column=5)

class AOOR_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for AOOR pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Max_Sensor_Rate()
        tk.Label(slave, text="Maximum Sensor Rate (PPM)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Threshold()
        tk.Label(slave, text="Activity Threshold", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Reaction_Time()
        tk.Label(slave, text="Reaction Time (sec)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.R_Factor()
        tk.Label(slave, text="Response Factor", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.Recovery_Time()
        tk.Label(slave, text="Recovery Time (min)", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=18, column=2)

class AAIR_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for AAIR pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Max_Sensor_Rate()
        tk.Label(slave, text="Maximum Sensor Rate (PPM)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Sensitivity()
        tk.Label(slave, text="Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Refractory()
        tk.Label(slave, text="Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=14, column=2)

        self.PVARP()
        tk.Label(slave, text="PVARP (ms)", font=("Helvetica", 10, "bold")).grid(row=2, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3, column=3)

        self.Hysteresis()
        tk.Label(slave, text="Hysteresis (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=4, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5, column=3)

        self.Smoothing()
        tk.Label(slave, text="Rate Smoothing (%)", font=("Helvetica", 10, "bold")).grid(row=6, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=6, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7, column=3)

        self.Threshold()
        tk.Label(slave, text="Activity Threshold", font=("Helvetica", 10, "bold")).grid(row=8, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9, column=3)

        self.Reaction_Time()
        tk.Label(slave, text="Reaction Time (sec)", font=("Helvetica", 10, "bold")).grid(row=10, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=10, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11, column=3)

        self.R_Factor()
        tk.Label(slave, text="Response Factor", font=("Helvetica", 10, "bold")).grid(row=12, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=12, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13, column=3)

        self.Recovery_Time()
        tk.Label(slave, text="Recovery Time (min)", font=("Helvetica", 10, "bold")).grid(row=14, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=5)

class VOOR_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for VOOR pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Max_Sensor_Rate()
        tk.Label(slave, text="Maximum Sensor Rate (PPM)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Threshold()
        tk.Label(slave, text="Activity Threshold", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Reaction_Time()
        tk.Label(slave, text="Reaction Time (sec)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.R_Factor()
        tk.Label(slave, text="Response Factor", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.Recovery_Time()
        tk.Label(slave, text="Recovery Time (min)", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=18, column=2)

class VVIR_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for VVIR pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Max_Sensor_Rate()
        tk.Label(slave, text="Maximum Sensor Rate (PPM)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Sensitivity()
        tk.Label(slave, text="Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Recovery_Time()
        tk.Label(slave, text="Recovery Time (min)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=2)

        self.Refractory()
        tk.Label(slave, text="Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=2, column=3)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=2, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3, column=3)

        self.Hysteresis()
        tk.Label(slave, text="Hysteresis (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=4, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5, column=3)

        self.Smoothing()
        tk.Label(slave, text="Rate Smoothing (%)", font=("Helvetica", 10, "bold")).grid(row=6, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=6, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7, column=3)

        self.Threshold()
        tk.Label(slave, text="Activity Threshold", font=("Helvetica", 10, "bold")).grid(row=8, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9, column=3)

        self.Reaction_Time()
        tk.Label(slave, text="Reaction Time (sec)", font=("Helvetica", 10, "bold")).grid(row=10, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=10, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11, column=3)

        self.R_Factor()
        tk.Label(slave, text="Response Factor", font=("Helvetica", 10, "bold")).grid(row=12, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=12, column=5)

class VDDR_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for VDDR pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Max_Sensor_Rate()
        tk.Label(slave, text="Maximum Sensor Rate (PPM)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.F_Delay()
        tk.Label(slave, text="Fixed Delay (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.D_Delay()
        tk.Label(slave, text="Dynamic Delay", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Amplitude()
        tk.Label(slave, text="Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Width()
        tk.Label(slave, text="Width (ms)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Sensitivity()
        tk.Label(slave, text="Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.Refractory()
        tk.Label(slave, text="Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=18, column=2)

        self.PVARP_E()
        tk.Label(slave, text="PVARP Extension (ms)", font=("Helvetica", 10, "bold")).grid(row=2, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3, column=3)

        self.Smoothing()
        tk.Label(slave, text="Rate Smoothing (%)", font=("Helvetica", 10, "bold")).grid(row=4, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=4, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5, column=3)

        self.ATR_Duration()
        tk.Label(slave, text="ATR Duration (cardiac cycles)", font=("Helvetica", 10, "bold")).grid(row=6, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7, column=3)

        self.ATR_Fallback_Mode()
        tk.Label(slave, text="ATR Fallback Mode", font=("Helvetica", 10, "bold")).grid(row=8, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9, column=3)

        self.ATR_Fallback_Time()
        tk.Label(slave, text="ATR Fallback Time (min)", font=("Helvetica", 10, "bold")).grid(row=10, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=10, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11, column=3)

        self.Threshold()
        tk.Label(slave, text="Activity Threshold", font=("Helvetica", 10, "bold")).grid(row=12, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=12, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13, column=3)

        self.Reaction_Time()
        tk.Label(slave, text="Reaction Time (sec)", font=("Helvetica", 10, "bold")).grid(row=14, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15, column=3)

        self.R_Factor()
        tk.Label(slave, text="Response Factor", font=("Helvetica", 10, "bold")).grid(row=16, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=16, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17, column=3)

        self.Recovery_Time()
        tk.Label(slave, text="Recovery Time (min)", font=("Helvetica", 10, "bold")).grid(row=18, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=18, column=5)

class DOOR_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for DOOR pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Max_Sensor_Rate()
        tk.Label(slave, text="Maximum Sensor Rate (PPM)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.F_Delay()
        tk.Label(slave, text="Fixed Delay (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Amplitude()
        tk.Label(slave, text="Atrial Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Width()
        tk.Label(slave, text="Atrial Width (ms)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Amplitude()
        tk.Label(slave, text="Ventrical Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Width()
        tk.Label(slave, text="Ventrical Width (ms)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.Threshold()
        tk.Label(slave, text="Activity Threshold", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=18, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=19)

        self.Reaction_Time()
        tk.Label(slave, text="Reaction Time (sec)", font=("Helvetica", 10, "bold")).grid(row=20, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=20, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=21)

        self.R_Factor()
        tk.Label(slave, text="Response Factor", font=("Helvetica", 10, "bold")).grid(row=22, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=22, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=23)

        self.Recovery_Time()
        tk.Label(slave, text="Recovery Time (min)", font=("Helvetica", 10, "bold")).grid(row=24, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=24, column=2)

class DDIR_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for DDIR pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Max_Sensor_Rate()
        tk.Label(slave, text="Maximum Sensor Rate (PPM)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.F_Delay()
        tk.Label(slave, text="Fixed Delay (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.Amplitude()
        tk.Label(slave, text="Atrial Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Width()
        tk.Label(slave, text="Atrial Width (ms)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Amplitude()
        tk.Label(slave, text="Ventrical Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Width()
        tk.Label(slave, text="Ventrical Width (ms)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=16, column=2)

        self.Sensitivity()
        tk.Label(slave, text="Atrial Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=2, column=3)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=2, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3, column=3)

        self.Refractory()
        tk.Label(slave, text="Atrial Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=4, column=3)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=4, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5, column=3)

        self.Sensitivity()
        tk.Label(slave, text="Ventrical Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=6, column=3)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=6, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7, column=3)

        self.Refractory()
        tk.Label(slave, text="Ventrical Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=8, column=3)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=8, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9, column=3)

        self.PVARP()
        tk.Label(slave, text="PVARP (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=10, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11, column=3)

        self.Threshold()
        tk.Label(slave, text="Activity Threshold", font=("Helvetica", 10, "bold")).grid(row=12, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=12, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13, column=3)

        self.Reaction_Time()
        tk.Label(slave, text="Reaction Time (sec)", font=("Helvetica", 10, "bold")).grid(row=14, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15, column=3)

        self.R_Factor()
        tk.Label(slave, text="Response Factor", font=("Helvetica", 10, "bold")).grid(row=16, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=16, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17, column=3)

        self.Recovery_Time()
        tk.Label(slave, text="Recovery Time (min)", font=("Helvetica", 10, "bold")).grid(row=18, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=18, column=5)

class DDDR_Window(SignIn_Window):

    def __init__(self, slave):
        L_title = tk.Label(slave, text="Please enter parameter values for DDDR pacing mode\n(Default = Nominal Value)", fg="green")
        L_title.grid(row=0, columnspan=4)
        L_title.configure(font=("Times", 15, "bold", "italic"))

        self.LRL_Values()
        tk.Label(slave, text="Lower Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=2, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3)

        self.URL_Values()
        tk.Label(slave, text="Upper Rate Limit (PPM)", font=("Helvetica", 10, "bold")).grid(row=4, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5)

        self.Max_Sensor_Rate()
        tk.Label(slave, text="Maximum Sensor Rate (PPM)", font=("Helvetica", 10, "bold")).grid(row=6, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7)

        self.D_Delay()
        tk.Label(slave, text="Dynamic Delay", font=("Helvetica", 10, "bold")).grid(row=8, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=8, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9)

        self.S_Delay_Offset()
        tk.Label(slave, text="Sensed Delay Offset (ms)", font=("Helvetica", 10, "bold")).grid(row=10, column=0)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=10, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11)

        self.Amplitude()
        tk.Label(slave, text="Atrial Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=12, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=12, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13)

        self.Width()
        tk.Label(slave, text="Atrial Width (ms)", font=("Helvetica", 10, "bold")).grid(row=14, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=14, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15)

        self.Amplitude()
        tk.Label(slave, text="Ventrical Amplitude (V)", font=("Helvetica", 10, "bold")).grid(row=16, column=0)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=16, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17)

        self.Width()
        tk.Label(slave, text="Ventrical Width (ms)", font=("Helvetica", 10, "bold")).grid(row=18, column=0)
        tk.OptionMenu(slave, self.default, "0.05", *self.values).grid(row=18, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=19)

        self.Sensitivity()
        tk.Label(slave, text="Atrial Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=20, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=20, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=21)

        self.Refractory()
        tk.Label(slave, text="Atrial Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=22, column=0)
        tk.OptionMenu(slave, self.A_default, *self.values).grid(row=22, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=23)

        self.Sensitivity()
        tk.Label(slave, text="Ventrical Sensitivity (mV)", font=("Helvetica", 10, "bold")).grid(row=24, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=24, column=2)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=25)

        self.Refractory()
        tk.Label(slave, text="Ventrical Refractory Period (ms)", font=("Helvetica", 10, "bold")).grid(row=26, column=0)
        tk.OptionMenu(slave, self.V_default, *self.values).grid(row=26, column=2)

        self.F_Delay()
        tk.Label(slave, text="Fixed Delay (ms)", font=("Helvetica", 10, "bold")).grid(row=2, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=2, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=3, column=3)

        self.PVARP()
        tk.Label(slave, text="PVARP (ms)", font=("Helvetica", 10, "bold")).grid(row=4, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=4, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=5, column=3)

        self.PVARP_E()
        tk.Label(slave, text="PVARP Extension (ms)", font=("Helvetica", 10, "bold")).grid(row=6, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=6, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=7, column=3)

        self.Hysteresis()
        tk.Label(slave, text="Hysteresis (PPM)", font=("Helvetica", 10, "bold")).grid(row=8, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=8, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=9, column=3)

        self.Smoothing()
        tk.Label(slave, text="Rate Smoothing (%)", font=("Helvetica", 10, "bold")).grid(row=10, column=3)
        tk.OptionMenu(slave, self.default, "OFF", *self.values).grid(row=10, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=11, column=3)

        self.ATR_Duration()
        tk.Label(slave, text="ATR Duration (cardiac cycles)", font=("Helvetica", 10, "bold")).grid(row=12, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=12, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=13, column=3)

        self.ATR_Fallback_Mode()
        tk.Label(slave, text="ATR Fallback Mode", font=("Helvetica", 10, "bold")).grid(row=14, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=14, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=15, column=3)

        self.ATR_Fallback_Time()
        tk.Label(slave, text="ATR Fallback Time (min)", font=("Helvetica", 10, "bold")).grid(row=16, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=16, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=17, column=3)

        self.Threshold()
        tk.Label(slave, text="Activity Threshold", font=("Helvetica", 10, "bold")).grid(row=18, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=18, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=19, column=3)

        self.Reaction_Time()
        tk.Label(slave, text="Reaction Time (sec)", font=("Helvetica", 10, "bold")).grid(row=20, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=20, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=21, column=3)

        self.R_Factor()
        tk.Label(slave, text="Response Factor", font=("Helvetica", 10, "bold")).grid(row=22, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=22, column=5)
        tk.Frame(slave, height=1, width=400, bg="green").grid(row=23, column=3)

        self.Recovery_Time()
        tk.Label(slave, text="Recovery Time (min)", font=("Helvetica", 10, "bold")).grid(row=24, column=3)
        tk.OptionMenu(slave, self.default, *self.values).grid(row=24, column=5)



def main():
    master = tk.Tk()
    x = WelcomeScreen(master)
    master.mainloop()

main()