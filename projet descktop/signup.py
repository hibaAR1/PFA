from tkinter import *
from tkinter import messagebox
from data_base.connectDB import gestionEmployee
from tkinter.messagebox import askyesno

gestEmpl = gestionEmployee()


class SignUp:
    def __init__(self):
        self.root = Tk()

        self.root.resizable(False, False)
        self.root.title("Ar_Vet")

        self.iconImage = PhotoImage(file="./images/logo.png")
        self.root.iconphoto(False, self.iconImage)

        self.height = 650
        self.width = 1120
        self.x = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        self.y = (self.root.winfo_screenheight() // 4) - (self.height // 4)
        self.root.geometry('{}x{}+{}+{}'.format(self.width,
                           self.height, self.x, self.y))

# ================cancel ====================
        self.root.protocol("WM_DELETE_WINDOW", self.confirm)
# ======================logo===================================
        self.logo_back = PhotoImage(file="./images/LoginLogo.png")
        self.logo = Label(
            self.root, image=self.logo_back
        )
        self.logo.place(x=516, y=27)
# ============================================================
# ================ CREATE ACCOUNT HEADER ====================
        self.createAccount_header = Label(

            text="Create new account",
            fg="black",
            font=("yu gothic ui Bold", 15),
            bg="#f0f0f0",

        )
        self.createAccount_header.place(x=470, y=150)
# ================ firstName Section ====================

        # Create a Frame with a blue background
        self.frame = Frame(self.root, bg="#5393cf")
        self.frame.place(x=250, y=250)

# Create the Entry with a gray background and Arial font of size 12
        self.firstName_entry = Entry(self.frame, bd=0,  font=(
            "Arial", 12), width=30, bg="#f0f0f0")

# Add padding to the top and bottom of the Entry widget within the Frame
        self.firstName_entry.pack(pady=[0, 2])
        # Insert placeholder text
        self.firstName_entry.insert(0, "FirstName")

        self.firstName_entry.bind("<FocusIn>", self.clear_text)

        self.firstName_email_icon = PhotoImage(file="./images/name_icon.png")

        self.firstName_icon_Label = Label(

            image=self.firstName_email_icon,
            bg="#f0f0f0")
        self.firstName_icon_Label.place(x=500, y=245)


# ================ Last Name Section ====================

        # Create a Frame with a blue background
        self.frame = Frame(self.root, bg="#5393cf")
        self.frame.place(x=650, y=250)

# Create the Entry with a gray background and Arial font of size 12
        self.lastName_entry = Entry(self.frame, bd=0,  font=(
            "Arial", 12), width=30, bg="#f0f0f0")

# Add padding to the top and bottom of the Entry widget within the Frame
        self.lastName_entry.pack(pady=[0, 2])
        # Insert placeholder text
        self.lastName_entry.insert(0, "LastName")

        self.lastName_entry.bind("<FocusIn>", self.clear_text)

        self.lastName_email_icon = PhotoImage(file="./images/name_icon.png")

        self.lastName_icon_Label = Label(

            image=self.lastName_email_icon,
            bg="#f0f0f0")
        self.lastName_icon_Label.place(x=900, y=245)


# ================ user Name Section ===================
 # Create a Frame with a blue background
        self.frame = Frame(self.root, bg="#5393cf")
        self.frame.place(x=250, y=300)

# Create the Entry with a gray background and Arial font of size 12
        self.emailName_entry = Entry(self.frame, bd=0,  font=(
            "Arial", 12), width=74, bg="#f0f0f0")

# Add padding to the top and bottom of the Entry widget within the Frame
        self.emailName_entry.pack(pady=[0, 2])
        # Insert placeholder text
        self.emailName_entry.insert(0, "UserName")

        self.emailName_entry.bind("<FocusIn>", self.clear_text)

        self.emailName_email_icon = PhotoImage(file="./images/email-icon.png")

        self.emailName_icon_Label = Label(

            image=self.emailName_email_icon,
            bg="#f0f0f0")
        self.emailName_icon_Label.place(x=905, y=300)

# ================ Password Name Section ====================

 # Create a Frame with a blue background
        self.frame = Frame(self.root, bg="#5393cf")
        self.frame.place(x=250, y=350)

# Create the Entry with a gray background and Arial font of size 12
        self.passwordName_entry = Entry(
            self.frame, bd=0,  font=("Arial", 12), width=30, bg="#f0f0f0")

# Add padding to the top and bottom of the Entry widget within the Frame
        self.passwordName_entry.pack(pady=[0, 2])
        # Insert placeholder text
        self.passwordName_entry.insert(0, "Password")

        self.passwordName_entry.bind("<FocusIn>", self.clear_text)

        self.passwordName_email_icon = PhotoImage(
            file="./images/pass-icon.png")

        self.passwordName_icon_Label = Label(

            image=self.passwordName_email_icon,
            bg="#f0f0f0")
        self.passwordName_icon_Label.place(x=500, y=345)
# ================ Confirm Password Name Section ====================

 # Create a Frame with a blue background
        self.frame = Frame(self.root, bg="#5393cf")
        self.frame.place(x=650, y=350)

# Create the Entry with a gray background and Arial font of size 12
        self.confirm_passwordName_entry = Entry(
            self.frame, bd=0,  font=("Arial", 12), width=30, bg="#f0f0f0")

# Add padding to the top and bottom of the Entry widget within the Frame
        self.confirm_passwordName_entry.pack(pady=[0, 2])
        # Insert placeholder text
        self.confirm_passwordName_entry.insert(0, "Confirm Password")

        self.confirm_passwordName_entry.bind("<FocusIn>", self.clear_text)

        self.confirm_passwordName_email_icon = PhotoImage(
            file="./images/pass-icon.png")

        self.confirm_passwordName_icon_Label = Label(

            image=self.confirm_passwordName_email_icon,
            bg="#f0f0f0")
        self.confirm_passwordName_icon_Label.place(x=900, y=345)

# ==========choice section=================================================

        self.options = ["Doctor", "Assistant"]
        self.selected_option = StringVar(value="Select an option")
        self.selected_label = OptionMenu(
            self.root, self.selected_option, *self.options)
        self.selected_label.config(bd=0, bg="#f0f0f0", borderwidth=1, highlightthickness=0, font=(
            "yu gothic ui Bold", 10), width=29)
        self.selected_label["menu"].config(
            bg="#f0f0f0", fg="black", font=("yu gothic ui Bold", 10))
        self.selected_label.place(x=459, y=410)

# =============== Submit Button ====================
        self.submit_buttonImage = PhotoImage(file="./images/image.png")
        self.submit_button = Button(

            image=self.submit_buttonImage,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            bg="#f0f0f0",
            cursor="hand2",
            command=self.insertEmployee
        )
        self.submit_button.place(x=466,  y=500, width=200, height=61)

# ================ ALREADY HAVE AN ACCOUNT TEXT ====================
        self.text = Label(
            # self.bg_image,
            text="Already a member?",
            fg="black",
            font=("yu gothic ui Regular", 10),
            bg="#f0f0f0"
        )
        self.text.place(x=480, y=569)
# ================ GO TO LOGIN ====================
        self.switchLogin = Button(

            text="Login",
            fg="black",
            font=("yu gothic ui Bold", 10),
            bg="#f0f0f0",
            bd=0,
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command=self.loginWindow
        )
        self.switchLogin.place(x=599, y=569, width=34, height=21)

        self.root.mainloop()

    def loginWindow(self):
        self.root.destroy()
        from login import Login
        Login()

    def update_selected(self, option):
        self.selected_label.config(text=option)

    def empty(self):
        self.firstName_entry.delete(0, END)
        self.lastName_entry.delete(0, END)
        self.emailName_entry.delete(0, END)
        self.passwordName_entry.delete(0, END)
        self.confirm_passwordName_entry.delete(0, END)
        self.update_selected('')

    def verify(self):
        return self.firstName_entry.get() != '' and self.lastName_entry.get() != '' and self.emailName_entry.get() != '' and self.passwordName_entry.get() != '' and self.confirm_passwordName_entry.get() != "" and self.selected_option.get() != ''

    def insertEmployee(self):
        if self.verify():
            if self.passwordName_entry.get() == self.confirm_passwordName_entry.get():
                tpl = (self.firstName_entry.get() + " " + self.lastName_entry.get(),
                       self.emailName_entry.get(), self.passwordName_entry.get(), self.selected_option.get())
                gestEmpl.insertTbl(tpl)
                self.empty()
            else:
                messagebox.showerror(
                    message='verify the confirmation password')
        else:
            messagebox.showerror(message='Can you fill all the elements')

    def confirm(self):
        self.ans = askyesno(title="Exit", message="Do you want to exit?")
        if self.ans:
            self.root.destroy()

    def clear_text(self, event):
        if event.widget == self.firstName_entry:
            if self.firstName_entry.get() == 'FirstName':
                # delete all the text in the entry
                self.firstName_entry.delete(0, "end")
                # Insert blank for user input
                self.firstName_entry.insert(0, '')
        elif event.widget == self.lastName_entry:
            if self.lastName_entry.get() == 'LastName':
                # delete all the text in the entry
                self.lastName_entry.delete(0, "end")
                # Insert blank for user input
                self.lastName_entry.insert(0, '')
        elif event.widget == self.emailName_entry:
            if self.emailName_entry.get() == 'UserName':
                # delete all the text in the entry
                self.emailName_entry.delete(0, "end")
                # Insert blank for user input
                self.emailName_entry.insert(0, '')
        elif event.widget == self.passwordName_entry:
            if self.passwordName_entry.get() == 'Password':
                # delete all the text in the entry
                self.passwordName_entry.delete(0, "end")
                # Insert blank for user input
                self.passwordName_entry.insert(0, '')
        elif event.widget == self.confirm_passwordName_entry:
            if self.confirm_passwordName_entry.get() == 'Confirm Password':
                self.confirm_passwordName_entry.delete(
                    0, "end")  # delete all the text in the entry
                self.confirm_passwordName_entry.insert(
                    0, '')  # Insert blank for user input
