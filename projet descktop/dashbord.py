from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime, timedelta
import tkinter as tk
from data_base.connectDB import gestanimaux , gestrendezvous , gesttreatement
gestAnimaux = gestanimaux()
gestionRdv = gestrendezvous()
gestionTreat = gesttreatement()
class dashbord:
    def __init__(self):
        self.root = Tk()

        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        self.root.title("Ar_Vet")
        self.iconImage = PhotoImage(file="./images/logo.png")
        self.root.iconphoto(False, self.iconImage)

        self.height = 740
        self.width = 1200
        self.x = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        self.y = (self.root.winfo_screenheight() // 4) - (self.height // 4)
        self.root.geometry('{}x{}+{}+{}'.format(self.width,
                           self.height, self.x, self.y))

        # sidebare

        self.sidebar = Frame(self.root, bg='#151515')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # logo dashbord

        self.logoImage = Image.open('./images/cabinet_dog.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg='#151515')
        self.logo.image = photo
        self.logo.place(x=60, y=80)

        # le nom du logo
        self.logo = Label(
            text="Cabinet",
            fg="white",
            font=("yu gothic ui Bold", 16),
            bg="#151515",
        )
        self.logo.place(x=100, y=82)

        self.logo1 = Label(

            text="Vet",
            fg="#70AFFF",
            font=("yu gothic ui Bold", 16),
            bg="#151515",

        )
        self.logo1.place(x=186, y=82)

        # first : home
        self.homeImage = Image.open('./images/home.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=30, y=187)

        self.home_text = Button(self.sidebar, text='Home', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515", command=self.home)
        self.home_text.place(x=90, y=185)

        # second:client

        self.homeImage = Image.open('./images/client.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=30, y=245)

        self.home_text = Button(self.sidebar, text='Espace Client', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515",  command=self.Espace_client)
        self.home_text.place(x=90, y=240)

        # third:rendez-vous
        self.homeImage = Image.open('./images/calendrier.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=30, y=300)

        self.home_text = Button(self.sidebar, text='Rendez_vous', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515",  command=self.Rendez_vous)
        self.home_text.place(x=90, y=300)

        # animaux
        self.homeImage = Image.open('./images/calendrier_an.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=30, y=370)

        self.home_text = Button(self.sidebar, text='Espace Animaux', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515",  command=self.Espace_animaux)
        self.home_text.place(x=90, y=370)

        # traitement
        self.homeImage = Image.open('./images/traitment.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=30, y=430)

        self.home_text = Button(self.sidebar, text='Traitement', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515", command=self.traitement)
        self.home_text.place(x=90, y=430)

        # facture
        self.homeImage = Image.open('./images/facture.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=30, y=490)

        self.home_text = Button(self.sidebar, text='Facture', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515", command=self.Facture)
        self.home_text.place(x=90, y=490)

        # logout
        self.homeImage = Image.open('./images/logout.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=80, y=650)

        self.home_text = Button(self.sidebar, text='LogOut', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515",  command=self.logout)
        self.home_text.place(x=120, y=645)

        # photo dashbord
        self.dashImage = Image.open('./images/dash.png')
        photo = ImageTk.PhotoImage(self.dashImage)
        self.dash = Label(self.root, image=photo, bg='#f0f0f0')
        self.dash.image = photo
        self.dash.place(x=450, y=80)
        # date
        self.current_date = datetime.today()

        self.date_label = Label(
            self.root,  font=(
                "", 15, "bold"), text=self.current_date.strftime("%d-%m-%Y"), bg='#f0f0f0')

        self.date_label.place(x=1070, y=10)

        #
        # self.text = Label(self.root , text="Raport", bg="#f0f0f0" , font=("", 20 , "bold"))
        # self.text.place(x=310 , y= 410)
        # =======body Frame 1=======

        self.bodyframe1 = Frame(self.root, bg="#d7d7d7")
        self.bodyframe1.place(x=328, y=495, width=230, height=220)
        #changing text
        self.CountAnimal = Label(
            self.bodyframe1, text=len(gestAnimaux.selectALL()), font=(
                "", 20, "bold") , bg="#d7d7d7")
        self.CountAnimal.place(x=100, y=150)
        #image
        
        self.frame1Image = Image.open('./images/frame1.png')
        photo = ImageTk.PhotoImage(self.frame1Image)
        self.frame1_label = Label(self.bodyframe1, image=photo, bg='#d7d7d7' , bd=0)
        self.frame1_label.image = photo
        self.frame1_label.place(x=160, y=20)
        
        #text
        self.frame1_text = Label(self.bodyframe1 , text="Total Animaux", bg="#d7d7d7" , font=("", 12 , "bold"))
        self.frame1_text.place(x=57 , y= 80)
        # =======body Frame 2=======

        self.bodyframe2 = Frame(self.root, bg="#d7d7d7")
        self.bodyframe2.place(x=630, y=495, width=230, height=220)
        
        
        
        #changing text
        self.Countrendez_vous = Label(
            self.bodyframe2, text=len(gestionRdv.selectALL()), font=(
                "", 20, "bold") , bg="#d7d7d7")
        self.Countrendez_vous.place(x=109, y=150)
        #image
        
        self.frame2Image = Image.open('./images/frame2.png')
        photo = ImageTk.PhotoImage(self.frame2Image)
        self.frame2_label = Label(self.bodyframe2, image=photo, bg='#d7d7d7' , bd=0)
        self.frame2_label.image = photo
        self.frame2_label.place(x=160, y=20)
        
        #text
        self.frame2_text = Label(self.bodyframe2 , text="Total Rendez_vous", bg="#d7d7d7" , font=("", 12 , "bold"))
        self.frame2_text.place(x=40 , y= 80)
        # =======body Frame 3=======

        self.bodyframe3 = Frame(self.root, bg="#d7d7d7")
        self.bodyframe3.place(x=930, y=495, width=230, height=220)
        
        #changing text
        self.Count_traitement = Label(
            self.bodyframe3, text=len(gestionTreat.selectALL()), font=(
                "", 20, "bold") , bg="#d7d7d7")
        self.Count_traitement.place(x=109, y=150)
        
        #image
        self.frame3Image = Image.open('./images/frame3.png')
        photo = ImageTk.PhotoImage(self.frame3Image)
        self.frame3_label = Label(self.bodyframe3, image=photo, bg='#d7d7d7' , bd=0)
        self.frame3_label.image = photo
        self.frame3_label.place(x=165, y=20)
        
        #text
        self.frame3_text = Label(self.bodyframe3 , text="Total Traitement", bg="#d7d7d7" , font=("", 12 , "bold"))
        self.frame3_text.place(x=49 , y= 80)
        
        self.root.mainloop()

    def darkMode(self):
        if self.root.cget('bg') == 'white':
            self.root.configure(bg='#444654')
            self.ShowMode.configure(image=self.lightModeImage, bg='#444654')
            self.date_label.configure(bg='#444654', fg="white")
        else:
            self.root.configure(bg='white')
            self.ShowMode.configure(image=self.darkModeImage, bg='white')
            self.date_label.configure(bg='white', fg="black")

    # date

    def prev_day(self):
        self.current_date = self.current_date - timedelta(days=1)
        self.update_date_label()

    def next_day(self):
        self.current_date = self.current_date + timedelta(days=1)
        self.update_date_label()

    def update_date_label(self):
        self.date_label.configure(text=self.current_date.strftime("%d-%m-%Y"))


# liason entre les fils

    def Facture(self):
        self.root.destroy()
        from facture import Facture
        Facture()

    def traitement(self):
        self.root.destroy()
        from traitement import traitement
        traitement()

    def Espace_client(self):
        self.root.destroy()
        from Espace_client import Espace_client
        Espace_client()

    def Espace_animaux(self):
        self.root.destroy()
        from Espace_animaux import Espace_animaux
        Espace_animaux()

    def Rendez_vous(self):
        self.root.destroy()
        from Rendez_vous import Rendez_vous
        Rendez_vous()

    def logout(self):
        self.root.destroy()
        from login import Login
        Login()

    def home(self):

        from dashbord import dashbord
        dashbord()
