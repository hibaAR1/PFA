from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

from data_base.connectDB import gestClients

gestClient = gestClients()


class client:
    def __init__(self):
        self.id = ''
        self.nom = ''
        self.prenom = ''
        self.Cne = ''
        self.tele = ''

    def initialize(self, id, cne, nom, prenom, tele):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.Cne = cne
        self.tele = tele

    def getAllInfos(self):
        return self.id, self.Cne, self.nom, self.prenom, self.tele


class Espace_client():
    tpl = ()

    def __init__(self):

        self.root = Tk()
        self.root.resizable(False, False)
        self.root.configure(bg='#3d404b')
        self.root.title("Ar_Vet")
        self.iconImage = PhotoImage(file="./images/logo.png")
        self.root.iconphoto(False, self.iconImage)

        self.height = 740
        self.width = 1200
        self.x = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        self.y = (self.root.winfo_screenheight() // 4) - (self.height // 4)
        self.root.geometry('{}x{}+{}+{}'.format(self.width,
                           self.height, self.x, self.y))
        # ===============================title of espace_client=============================================
        self.titre = Label(text="Espace_Client",
                           font=("Arial", 20), fg="white", bg="#3d404b")
        self.titre.place(x=130, y=50, width=1200)

       # ================================sidebare===========================================================

        self.sidebar = Frame(self.root, bg='#151515')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # ===============================dashbord=============================================
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

        # home
        self.homeImage = Image.open('./images/home.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=30, y=187)

        self.home_text = Button(self.sidebar, text='Home', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515", command=self.Home)
        self.home_text.place(x=90, y=185)

        # client

        self.homeImage = Image.open('./images/client.png')
        photo = ImageTk.PhotoImage(self.homeImage)
        self.home = Label(self.sidebar, image=photo, bg='#151515')
        self.home.image = photo
        self.home.place(x=30, y=245)

        self.home_text = Button(self.sidebar, text='Espace Client', fg='white', bg='#151515', font=(
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515",  command=self.Espace_client)
        self.home_text.place(x=90, y=240)

        # rendez-vous
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
        # ================================end of dashbord===================================

        # =====================client=======================================================
        # on fait appele a class client
        self.Client = client()

        # ==========================Nom=====================================
        self.nom_image = PhotoImage(file="./images/input_img.png")
        self.nom_image_Label = Label(
            bg="#3d404b",
            image=self.nom_image,

        )
        self.nom_image_Label.place(x=330, y=190)

        self.nom_text = Label(
            self.nom_image_Label,
            # Cne
            text="Cne :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.nom_text.place(x=15, y=0)

        self.nom = Entry(
            self.nom_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.nom.place(x=8, y=22, width=150, height=25)

        # ==============prenom=========================================================

        self.prenom_image = PhotoImage(file="./images/input_img.png")
        self.prenom_image_Label = Label(
            bg="#3d404b",
            image=self.prenom_image,

        )
        self.prenom_image_Label.place(x=330, y=290)

        self.prenom_text = Label(
            self.prenom_image_Label,
            # nom
            text="Nom :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.prenom_text.place(x=15, y=0)

        self.prenom = Entry(
            self.prenom_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.prenom.place(x=8, y=22, width=150, height=25)

        # ======================cne===================

        self.cne_image1 = PhotoImage(file="./images/input_img.png")
        self.cne_image1_Label = Label(
            bg="#3d404b",
            image=self.cne_image1,

        )
        self.cne_image1_Label.place(x=330, y=390)

        self.cne_text = Label(
            self.cne_image1_Label,
            # prenom
            text="Prenom :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.cne_text.place(x=15, y=0)

        self.Cne = Entry(
            self.cne_image1_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.Cne.place(x=8, y=22, width=150, height=25)

        # ===============telef=========
        self.tele_image1 = PhotoImage(file="./images/input_img.png")
        self.tele_image_Label = Label(
            bg="#3d404b",
            image=self.tele_image1,

        )
        self.tele_image_Label.place(x=330, y=490)

        self.tele_text = Label(

            self.tele_image_Label,
            text="Telephone :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"

        )
        self.tele_text.place(x=15, y=0)

        self.tele = Entry(
            self.tele_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.tele.place(x=8, y=22, width=150, height=25)

        # ===================treeView============================================

        self.treeView = ttk.Treeview(self.root)
        self.treeView['columns'] = (
            'id', 'Cne', 'Nom', 'prenom', 'Tele')

        self.treeView.column('#0', width=0, stretch=NO)

        self.treeView.heading('#0', text='', anchor=CENTER)
        self.lst1 = ['id', 'Cne', 'Nom', 'prenom', 'Tele']
        for el in self.lst1:
            self.treeView.column(el, anchor=CENTER, width=80)
            self.treeView.heading(el, text=el, anchor=CENTER)

        self.treeView.place(x=560, y=150, width=600, height=450)
        # ================================scrlbar========================================
        self.scrlbar = ttk.Scrollbar(
            self.treeView, orient="vertical",  command=self.treeView.yview)
        self.scrlbar.pack(side='right', fill='y', ipady=100)
        self.treeView.configure(xscrollcommand=self.scrlbar.set)
        # ===================ajouter====================================

        self.ajouter = Button(self.root, text="Ajouter", bd=0, bg="#151515", fg="white",  font=('Courier', 11, "bold"),
                              command=self.inserting)
        self.ajouter.place(x=410, y=650, width=130, height=31)

        # ============modifier=======================
        self.modifier = Button(self.root, text="Get", bd=0, bg="#151515",  fg="white", font=('Courier', 11, "bold"),
                               command=self.modifierClient, state=DISABLED)
        self.modifier.place(x=700, y=650, width=130, height=31)
        self.treeView.bind('<ButtonRelease-1>', self.activateGetButton)

        try:
            self.getAllValuesBdClient()
        except:
            pass
        # ====================searching======================
        self.searching = Entry(self.root, bg="#f0f0f0")
        self.searching.insert(0, "Saisir nom : ")
        self.searching.bind(
            '<Button-1>', lambda event: self.searching.delete(0, END))
        self.searching.bind('<KeyRelease>', self.searchClient)
        self.searching.place(x=560, y=130, width=600)

        self.max = 0
        self.root.mainloop()

    def searchClient(self, event):
        if self.searching.get() != '':
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            lst = gestClient.selectNom(self.searching.get())
            for ele in sorted(lst, key=lambda k: k[0]):
                self.treeView.insert(
                    parent='', index=ele[0], iid=ele[0], text='h', values=ele)
        else:
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            self.getAllValuesBdClient()

    def getAllValuesBdClient(self):
        lst = gestClient.selectALL()
        for ele in sorted(lst, key=lambda k: k[0]):
            self.treeView.insert(
                parent='', index=ele[0], iid=ele[0], text='h', values=ele)

    def returnMaxid(self):
        lst = gestClient.selectALL()
        self.max = 0
        for ele in sorted(lst, key=lambda k: k[0]):
            self.max = max(int(self.max), int(ele[0]))

    def activateGetButton(self, event):
        item = self.treeView.selection()
        if item:
            self.modifier.configure(bg="black", fg="white", state=NORMAL)

    def getSelectedClient(self):
        item = self.treeView.selection()
        lst = []
        if item:
            lst = item
            selected_item = item[0]
        return lst

    def modifierClient(self):
        item = self.treeView.selection()
        if item:
            try:
                title = self.modifier.configure()['text'][-1]
                selected_item = item[0]
                lst = self.treeView.item(selected_item)['values']
                if title == 'Get':
                    self.nom.insert(0, lst[1])
                    self.prenom.insert(0, lst[2])
                    self.Cne.insert(0, lst[3])
                    self.tele.insert(0, lst[4])
                    self.modifier.configure(text='Modifier')

                    self.ajouter.configure(
                        bg="#D3D3D3", fg="black", state=DISABLED)
                else:

                    if self.verif():

                        self.treeView.item(item, values=(
                            lst[0], self.nom.get(), self.prenom.get(
                            ), self.Cne.get(), self.tele.get()))

                        tpl = (self.nom.get(),
                               self.prenom.get(),
                               self.Cne.get(),
                               self.tele.get(), lst[0])
                        gestClient.updateTbl(tpl)
                        self.modifier.configure(
                            text='Get',
                            bg="#D3D3D3",
                            fg="black",
                            state=DISABLED)

                        self.ajouter.configure(
                            bg="#3838e2",
                            fg="white",
                            state=NORMAL)

                        self.emptying()
            except:
                pass

    def emptying(self):
        self.nom.delete(0, END)
        self.prenom.delete(0, END)
        self.Cne.delete(0, END)

        self.tele.delete(0, END)

    def inserting(self):
        if self.verif():
            self.returnMaxid()
            i = self.max + 1
            self.Client.initialize(i, self.nom.get(), self.prenom.get(), self.Cne.get(),
                                   self.tele.get())
            tpl = self.Client.getAllInfos()
            gestClient.insertTbl(tpl)
            self.treeView.insert(parent='', index=i,
                                 iid=i, text='h', values=tpl)
            self.emptying()

    def verif(self):
        if self.nom.get() != '' and self.prenom.get() != '' and self.Cne.get() != '' and self.tele.get() != '':
            return True
        messagebox.showinfo("warning", "can you fill all the inputs !!")
        return False

    def Espace_client(self):
        self.root.destroy()
        from Espace_client import Espace_client
        Espace_client()

    def logout(self):
        self.root.destroy()
        from login import Login
        Login()

    def Espace_animaux(self):
        self.root.destroy()
        from Espace_animaux import Espace_animaux
        Espace_animaux()

    def Rendez_vous(self):
        self.root.destroy()
        from Rendez_vous import Rendez_vous
        Rendez_vous()

    def Facture(self):
        self.root.destroy()
        from facture import Facture
        Facture()

    def traitement(self):
        self.root.destroy()
        from traitement import traitement
        traitement()

    def Home(self):
        self.root.destroy()
        from dashbord import dashbord
        dashbord()
