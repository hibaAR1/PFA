from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from data_base.Api import getImage
from data_base.connectDB import gestanimaux, gestClients
# pip install tkcalendar (to install it)
from tkcalendar import DateEntry

gestionAnim = gestanimaux()
gestClient = gestClients()


class animaux:
    def __init__(self):
        self.Id = ''
        self.Id_Client = ''
        self.Nom = ''
        self.Ref = ''
        self.Sexe = ''
        self.Date_Naissance = ''
        self.Type = ''
        self.Image_Path = ''

    def setIdClient(self, Id_Client):
        self.Id_Client = Id_Client

    def initialize(self, Id, Id_Client, Nom, Ref, Sexe, Date_naissance, Type, Image_Path):
        self.Id = Id
        self.Id_Client = Id_Client
        self.Nom = Nom
        self.Ref = Ref
        self.Sexe = Sexe
        self.Date_Naissance = Date_naissance
        self.Type = Type
        self.Image_Path = Image_Path

    def getAllInfos(self):
        return self.Id, self.Id_Client, self.Nom, self.Ref, self.Sexe, self.Date_Naissance, self.Type, self.Image_Path


class Espace_animaux():
    tpl = ()

    def __init__(self):

        self.root = Tk()
        self.root.resizable(False, False)

        self.root.title("Ar_Vet")
        self.iconImage = PhotoImage(file="./images/logo.png")
        self.root.iconphoto(False, self.iconImage)
        self.root.configure(bg='#3d404b')
        self.height = 740
        self.width = 1200
        self.x = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        self.y = (self.root.winfo_screenheight() // 4) - (self.height // 4)
        self.root.geometry('{}x{}+{}+{}'.format(self.width,
                           self.height, self.x, self.y))

        # ===============================title of espace_client=============================================
        self.titre = Label(text="Espace_Animaux ",
                           font=("Arial", 20), fg="white", bg="#3d404b")
        self.titre.place(x=130, y=50, width=1200)

       # =============================sidebare========================================

        self.sidebar = Frame(self.root, bg='#151515')
        self.sidebar.place(x=0, y=0, width=300, height=750)

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
            "", 15, "bold"), bd=0, cursor='hand2', activeforeground="white", activebackground="#151515", command=self.Home)
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

        # =====================animal=======================================================
        self.animaux = animaux()

        # =======id_animal=====================================
        self.Id_Client_image = PhotoImage(file="./images/input_img.png")
        self.Id_Client_image_Label = Label(
            bg="#3d404b",
            image=self.Id_Client_image,

        )
        self.Id_Client_image_Label.place(x=330, y=135)

        self.Id_Client_text = Label(
            self.Id_Client_image_Label,
            # Cne
            text="Cne Client :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.Id_Client_text.place(x=15, y=0)

        self.Id_Client = Entry(
            self.Id_Client_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.Id_Client.place(x=8, y=22, width=150, height=25)

        # ==============Nom=========================================================

        self.Nom_image = PhotoImage(file="./images/input_img.png")
        self.Nom_image_Label = Label(
            bg="#3d404b",
            image=self.Nom_image,

        )
        self.Nom_image_Label.place(x=330, y=215)

        self.Nom_text = Label(
            self.Nom_image_Label,
            # nom
            text="Nom :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.Nom_text.place(x=15, y=0)

        self.Nom = Entry(
            self.Nom_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.Nom.place(x=8, y=22, width=150, height=25)

        # ======================Ref===================

        self.Ref_image1 = PhotoImage(file="./images/input_img.png")
        self.Ref_image1_Label = Label(
            bg="#3d404b",
            image=self.Ref_image1,

        )
        self.Ref_image1_Label.place(x=330, y=295)

        self.Ref_text = Label(
            self.Ref_image1_Label,
            # prenom
            text="Reference :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.Ref_text.place(x=15, y=0)

        self.Ref = Entry(
            self.Ref_image1_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.Ref.place(x=8, y=22, width=150, height=25)

        # ===============Sexe=========
        self.Sexe_image1 = PhotoImage(file="./images/input_img.png")
        self.Sexe_image_Label = Label(
            bg="#3d404b",
            image=self.Sexe_image1,
        )
        self.Sexe_image_Label.place(x=330, y=375)

        self.Sexe_text = Label(
            self.Sexe_image_Label,
            text="Sexe :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.Sexe_text.place(x=15, y=0)

        style = ttk.Style()
        style.layout('Custom.TCombobox', [])
        style.configure('Custom.TCombobox', background='white',
                        fieldbackground='white')

        self.Sexe = ttk.Combobox(
            self.Sexe_image_Label,
            values=["Male", "Female"],
            state="readonly",
            font=("yu gothic ui Bold", 10),
            style='Custom.TCombobox'
        )
        self.Sexe.place(x=8, y=22, width=150, height=25)
        # ===============Date_naissance=========
        self.Date_naissance_image1 = PhotoImage(file="./images/input_img.png")
        self.Date_naissance_image_Label = Label(
            bg="#3d404b",
            image=self.Date_naissance_image1,
        )
        self.Date_naissance_image_Label.place(x=330, y=455)

        self.Date_naissance_text = Label(
            self.Date_naissance_image_Label,
            text="Date_naissance :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.Date_naissance_text.place(x=15, y=0)
        self.Date_naissance = DateEntry(
            self.Date_naissance_image_Label,
            font=("yu gothic ui Bold", 10),
            foreground='white',
            date_pattern='MM/dd/yyyy'
        )
        self.Date_naissance.place(x=8, y=22, width=150, height=25)

        # ===============Type=========
        self.Type_image1 = PhotoImage(file="./images/input_img.png")
        self.Type_image_Label = Label(
            bg="#3d404b",
            image=self.Type_image1,

        )
        self.Type_image_Label.place(x=330, y=535)

        self.Type_text = Label(

            self.Type_image_Label,
            text="Type:",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"

        )
        self.Type_text.place(x=15, y=0)

        self.Type = Entry(
            self.Type_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.Type.place(x=8, y=22, width=150, height=25)
        # ===================treeView====================================

        self.treeView = ttk.Treeview(self.root)
        self.treeView['columns'] = ('Id',
                                    'Cne_Client', 'Nom', 'Ref', 'Sexe', 'Date_naissance', 'Type')

        self.treeView.column('#0', width=0, stretch=NO)

        self.treeView.heading('#0', text='', anchor=CENTER)
        self.lst1 = ['Id', 'Cne_Client', 'Nom', 'Ref',
                     'Sexe', 'Date_naissance', 'Type']
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
                               command=self.modifierAnimal, state=DISABLED)
        self.modifier.place(x=700, y=650, width=130, height=31)
        self.treeView.bind('<ButtonRelease-1>', self.activateGetButton)

        try:
            self.getAllValuesBdAnimal()
        except:
            pass
        # ====================searching======================
        self.searching = Entry(self.root, bg="#f0f0f0")
        self.searching.insert(0, "Saisir Ref : ")
        self.searching.bind(
            '<Button-1>', lambda event: self.searching.delete(0, END))
        self.searching.bind('<KeyRelease>', self.searchAnimal)
        self.searching.place(x=560, y=130, width=600)
        self.treeView.bind('<Double-Button-1>', self.showInfoAnimal)

        self.max = 0
        self.root.mainloop()

    def searchAnimal(self, event):
        if self.searching.get() != '':
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            lst = gestionAnim.selectRef(self.searching.get())
            for ele in sorted(lst, key=lambda k: k[0]):
                self.treeView.insert(
                    parent='', index=ele[0], iid=ele[0], text='h', values=ele)
        else:
            for item in self.treeView.get_children():
                self.treeView.delete(item)
            self.getAllValuesBdAnimal()

    def showInfoAnimal(self, event):
        item = self.treeView.selection()
        if item:
            lst = self.getSelectedAnimal()
            from animalInfo import animalInfo
            animal_info_window = animalInfo(self.root, lst)
        else:
            messagebox.showinfo("Warning", "Select a row !")

    def getAllValuesBdAnimal(self):
        lst = gestionAnim.selectALL()
        for ele in sorted(lst, key=lambda k: k[0]):
            lst = list(ele)
            lst[1] = gestClient.selectId(ele[1])[1]
            self.treeView.insert(
                parent='', index=ele[0], iid=ele[0], text='h', values=tuple(lst))

    def returnMaxid(self):
        lst = gestionAnim.selectALL()
        self.max = 0
        for ele in sorted(lst, key=lambda k: k[0]):
            self.max = max(int(self.max), int(ele[0]))

    def activateGetButton(self, event):
        item = self.treeView.selection()
        if item:
            self.modifier.configure(bg="#3838e2", fg="white", state=NORMAL)

    def getSelectedAnimal(self):
        item = self.treeView.selection()
        lst = []
        if item:
            lst = item
            lst = gestionAnim.selectId(item[0])
        return lst

    def modifierAnimal(self):
        item = self.treeView.selection()
        if item:
            try:
                title = self.modifier.configure()['text'][-1]
                selected_item = item[0]
                lst = self.treeView.item(selected_item)['values']
                if title == 'Get':
                    self.Id_Client.insert(0, lst[1])
                    self.Id_Client.configure(state=DISABLED)
                    self.Nom.insert(0, lst[2])
                    self.Ref.insert(0, lst[3])
                    self.Ref.configure(state=DISABLED)
                    self.Sexe.insert(0, lst[4])
                    self.Date_naissance.insert(0, lst[5])
                    self.Type.insert(0, lst[6])
                    self.Type.configure(state=DISABLED)

                    self.modifier.configure(text='Modifier')
                    self.ajouter.configure(
                        bg="#D3D3D3", fg="black", state=DISABLED)
                else:
                    if self.verif():
                        self.treeView.item(item, values=(lst[0], self.Id_Client.get(), self.Nom.get(
                        ), self.Ref.get(), self.Sexe.get(), self.Date_naissance.get(), self.Type.get()))
                        tpl = (self.Nom.get(),
                               self.Sexe.get(),
                               self.Date_naissance.get(),
                               lst[0])
                        gestionAnim.updateTbl(tpl)
                        self.Id_Client.configure(state=NORMAL)
                        self.Ref.configure(state=NORMAL)
                        self.Type.configure(state=NORMAL)
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
        self.Id_Client.delete(0, END)
        self.Nom.delete(0, END)
        self.Ref.delete(0, END)
        self.Sexe.set('')
        self.Date_naissance.delete(0, END)
        self.Type.delete(0, END)

    def inserting(self):
        if self.verif():
            self.returnMaxid()
            i = self.max + 1
            self.animaux.initialize(i, self.Id_Client.get(), self.Nom.get(), self.Ref.get(), self.Sexe.get(
            ), self.Date_naissance.get(), self.Type.get(), 'media/'+self.Type.get().replace(' ', '_')+str(i)+'.png')
            tpl = self.animaux.getAllInfos()
            self.treeView.insert(parent='', index=i,
                                 iid=i, text='h', values=tpl[:7])
            self.animaux.setIdClient(
                gestClient.selectCne(self.Id_Client.get())[0][0])
            tpl = self.animaux.getAllInfos()
            gestionAnim.insertTbl(tpl[1:])
            try:
                PetImg = self.Type.get()
                getImage(PetImg, i)
            except Exception as e:
                print("Exception  : ", e.with_traceback)
                pass
            self.emptying()

    def verif(self):
        if self.Id_Client.get() != '' and self.Nom.get() != '' and self.Ref.get() != '' and self.Sexe.get() != '' and self.Date_naissance.get() != '' and self.Type.get() != '':
            if gestClient.selectCne(self.Id_Client.get()):
                return True
            else:
                messagebox.showinfo(
                    "warning", "the client you picked does not exist !")
                return False
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
