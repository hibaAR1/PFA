from tkinter import *
from tkinter import messagebox
from data_base.connectDB import createTables, gestionEmployee
from tkinter.messagebox import askyesno

from tkinter import ttk



gestEmpl = gestionEmployee()


class Login:
    def __init__(self):
        createTables()
        self.root = Tk()
        self.style = ttk.Style()
        
        
        self.height = 650
        self.width = 1120
        self.x = (self.root.winfo_screenwidth() // 2) - \
            (self.width // 2)
        self.y = (self.root.winfo_screenheight() // 4) - \
            (self.height // 4)
        self.root.geometry('{}x{}+{}+{}'.format(self.width,
                                            self.height, self.x, self.y))
        
        self.root.resizable(False, False)
        
        iconImage = PhotoImage(file="./images/logo.png")
        self.root.iconphoto(False, iconImage)
        self.root.title("Ar_Vet")

# ================cancel ====================
        self.root.protocol("WM_DELETE_WINDOW", self.confirm)

    # ======================logo===================================
        self.logo_back = PhotoImage(file="./images/LoginLogo.png")
        self.logo = Label(
            self.root, 
            image=self.logo_back
        )
        self.logo.place(x=516, y=27)
    # ============================================================

    # ================ LOGIN TO ACCOUNT HEADER ====================
        self.loginAccount_header = Label(
            
            text="Login",
            fg="black",
            font=("yu gothic ui Bold", 15),
        )
        self.loginAccount_header.place(x=540, y=160)

    # ================ Email Name Section ====================
        
        
        self.frame = Frame(self.root, bg="#5393cf")
        self.frame.pack(pady=250)

       # Create the Entry with a gray background and Arial font of size 12
        self.Login_emailName_entry = Entry(self.frame,bd=0,  font=("Arial", 12), width=30, bg="#f0f0f0")

# Add padding to the top and bottom of the Entry widget within the Frame
        self.Login_emailName_entry.pack(pady=[0,2])
        # Insert placeholder text
        self.Login_emailName_entry.insert(0, "Username")

        # Bind function to clear text on focus
        self.Login_emailName_entry.bind("<FocusIn>", self.clear_text)
        
        
        self.Login_emailName_icon = PhotoImage(file="./images/email-icon.png")
        
        self.Login_emailName_icon_Label = Label(

            image=self.Login_emailName_icon,
            bg="#f0f0f0")
        self.Login_emailName_icon_Label.place(x=698, y=250)
        
    # ================ Password Name Section ====================

        # Create a Frame with a blue background
        self.frame2 = Frame(self.root, bg="#5393cf")
        self.frame2.place(x=420 , y=350)

# Create the Entry with a gray background and Arial font of size 12
        self.Login_passwordName_entry = Entry(self.frame2,bd=0,  font=("Arial", 12), width=30, bg="#f0f0f0")

# Add padding to the top and bottom of the Entry widget within the Frame
        self.Login_passwordName_entry.pack(pady=[0,2])
        # Insert placeholder text
        self.Login_passwordName_entry.insert(0, "Password")
        # Bind function to clear text on focus
        self.Login_passwordName_entry.bind("<FocusIn>", self.clear_text)
       
        
        
        self.Login_passwordName_icon = PhotoImage(file="./images/pass-icon.png")
        
        self.Login_passwordName_Label = Label(

            image=self.Login_passwordName_icon,
            bg="#f0f0f0")
        self.Login_passwordName_Label.place(x=694, y=343)


    # =============== Submit Button ====================
        self.Login_button_image_1 = PhotoImage(file="./images/image.png")
        self.Login_button_1 = Button(
            
            bg="#f0f0f0",
            bd=0,
            image=self.Login_button_image_1,
            cursor="hand2",
            command=self.login
        )
        self.Login_button_1.place(x=459, y=439, width=207, height=51)



    # ================ NOT A MEMBER TEXT ====================
        self.loginText = Label(
            
            text="Not a member?",
            fg="black",
            font=("yu gothic ui Regular", 10),
            bg="#f0f0f0"
        )
        self.loginText.place(x=474, y=515)

    # ================ GO TO SIGN UP ====================
        self.switchSignup = Button(
            
            text=" Sign Up ",
            fg="black",
            font=("yu gothic ui Bold", 10),
            bg="#f0f0f0",
            bd=0,
            cursor="hand2",
            command=self.SignUp
        )
        self.switchSignup.place(x=570, y=515, width=50, height=25)
        
        
        self.root.mainloop()

    def login(self):
        if self.Login_emailName_entry.get() != '' and self.Login_passwordName_entry.get() != '':
            if self.Login_passwordName_entry.get() == gestEmpl.selectUsername(self.Login_emailName_entry.get())[0][3]:
                
                messagebox.showinfo(title="Ar_Vet", message="Connected")
                self.root.destroy()
                from dashbord import dashbord
                dashbord()

            else:
                messagebox.showerror(message="Wrong password")
        else:
            messagebox.showerror(message="fill all the fields !")

    def SignUp(self):
        self.root.destroy()
        from signup import SignUp
        SignUp()

    
    

    

    def confirm(self):
        self.ans = askyesno(title="Exit", message="Do you want to exit?")
        if self.ans:
            self.root.destroy()
            
            
            
    
    def clear_text(self, event):
        if event.widget == self.Login_passwordName_entry:
            if self.Login_passwordName_entry.get() == 'Password':
                self.Login_passwordName_entry.delete(0, "end") # delete all the text in the entry
                self.Login_passwordName_entry.insert(0, '') #Insert blank for user input
        elif event.widget == self.Login_emailName_entry:
            if self.Login_emailName_entry.get() == 'Username':
                self.Login_emailName_entry.delete(0, "end") # delete all the text in the entry
                self.Login_emailName_entry.insert(0, '') #Insert blank for user input