from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkinter import ttk
from data_base.connectDB import gestanimaux, gesttreatement

gestionAnim = gestanimaux()
gestionTreat = gesttreatement()


class Treatement:
    def __init__(self):
        self.Id = ''
        self.Id_animal = ''
        self.Nom = ''
        self.DateDebut = ''
        self.DateFin = ''
        self.DoesPerDay = ''
        self.Prix = ''

    def setIdAnimal(self, Id_animal):
        self.Id_animal = Id_animal

    def initialize(self, Id, Id_animal, Nom, DateDebut, DateFin, DoesPerDay, Prix):
        self.Id = Id
        self.Id_animal = Id_animal
        self.Nom = Nom
        self.DateDebut = DateDebut
        self.DateFin = DateFin
        self.DoesPerDay = DoesPerDay
        self.Prix = Prix

    def getAllInfos(self):
        return self.Id, self.Id_animal, self.Nom, self.DateDebut, self.DateFin, self.DoesPerDay, self.Prix


class traitement:
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

        # ===============================title of espace treatement=============================================
        self.titre = Label(text="Espace Treatments ",
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
        self.treat = Treatement()

        # =======id_animal=====================================
        self.Id_animal_image = PhotoImage(file="./images/input_img.png")
        self.Id_animal_image_Label = Label(
            bg="#3d404b",
            image=self.Id_animal_image,

        )
        self.Id_animal_image_Label.place(x=330, y=160)

        self.Id_animal_text = Label(
            self.Id_animal_image_Label,
            text="Ref Animal:",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.Id_animal_text.place(x=15, y=0)

        self.Id_animal = Entry(
            self.Id_animal_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.Id_animal.place(x=8, y=22, width=150, height=25)

        # ==============Nom=========================================================

        self.Nom_image = PhotoImage(file="./images/input_img.png")
        self.Nom_image_Label = Label(
            bg="#3d404b",
            image=self.Nom_image,

        )
        self.Nom_image_Label.place(x=330, y=235)

        self.Nom_text = Label(
            self.Nom_image_Label,
            # nom
            text="Nom Treatement:",
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

        # ======================DateDebut===================
        self.DateDebut_image1 = PhotoImage(file="./images/input_img.png")
        self.DateDebut_image1_Label = Label(
            bg="#3d404b",
            image=self.DateDebut_image1,

        )
        self.DateDebut_image1_Label.place(x=330, y=310)

        self.DateDebut_text = Label(
            self.DateDebut_image1_Label,
            # prenom
            text="Date Debut :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.DateDebut_text.place(x=15, y=0)

        self.DateDebut = DateEntry(
            self.DateDebut_image1_Label,
            font=("yu gothic ui Bold", 10),
            foreground='white',
            date_pattern='MM/dd/yyyy'
        )
        self.DateDebut.place(x=8, y=22, width=150, height=25)

        # ===============DateFin=========
        self.DateFin_image1 = PhotoImage(file="./images/input_img.png")
        self.DateFin_image_Label = Label(
            bg="#3d404b",
            image=self.DateFin_image1,
        )
        self.DateFin_image_Label.place(x=330, y=385)

        self.DateFin_text = Label(
            self.DateFin_image_Label,
            text="Date Fin :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.DateFin_text.place(x=15, y=0)

        self.DateFin = DateEntry(
            self.DateFin_image_Label,
            font=("yu gothic ui Bold", 10),
            foreground='white',
            date_pattern='MM/dd/yyyy'
        )
        self.DateFin.place(x=8, y=22, width=150, height=25)
        # ===============DoesPerDay=========
        self.DoesPerDay_image1 = PhotoImage(file="./images/input_img.png")
        self.DoesPerDay_image_Label = Label(
            bg="#3d404b",
            image=self.DoesPerDay_image1,
        )
        self.DoesPerDay_image_Label.place(x=330, y=460)

        self.DoesPerDay_text = Label(
            self.DoesPerDay_image_Label,
            text="DoesPerDay :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"
        )
        self.DoesPerDay_text.place(x=15, y=0)
        self.DoesPerDay = Entry(
            self.DoesPerDay_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.DoesPerDay.place(x=8, y=22, width=150, height=25)

        # ===============Prix=========
        self.Prix_image1 = PhotoImage(file="./images/input_img.png")
        self.Prix_image_Label = Label(
            bg="#3d404b",
            image=self.Prix_image1,

        )
        self.Prix_image_Label.place(x=330, y=535)

        self.Prix_text = Label(

            self.Prix_image_Label,
            text="Price :",
            fg="black",
            font=("yu gothic ui  Bold", 10),
            bg="white"

        )
        self.Prix_text.place(x=15, y=0)

        self.Prix = Entry(
            self.Prix_image_Label,
            bd=0,
            bg="white",
            highlightthickness=0,
            font=("yu gothic ui Bold", 10),
        )
        self.Prix.place(x=8, y=22, width=150, height=25)
        # ===================treeView====================================
        self.treeView = ttk.Treeview(self.root)
        self.treeView['columns'] = ('Id',
                                    'Ref Animal', 'Nom Treatement', 'Date Debut', 'Date Fin', 'Doses Per Day', 'Prix')

        self.treeView.column('#0', width=0, stretch=NO)

        self.treeView.heading('#0', text='', anchor=CENTER)
        self.lst1 = ['Id', 'Ref Animal', 'Nom Treatement',
                     'Date Debut', 'Date Fin', 'Doses Per Day', 'Prix']
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
            self.getAllValuesBdTreatement()
        except:
            pass

        self.max = 0
        self.root.mainloop()

    def getAllValuesBdTreatement(self):
        lst = gestionTreat.selectALL()
        for ele in sorted(lst, key=lambda k: k[0]):
            lst = list(ele)
            lst[1] = gestionAnim.selectId(ele[1])[3]
            self.treeView.insert(
                parent='', index=ele[0], iid=ele[0], text='h', values=tuple(lst))

    def returnMaxid(self):
        lst = gestionTreat.selectALL()
        self.max = 0
        for ele in sorted(lst, key=lambda k: k[0]):
            self.max = max(int(self.max), int(ele[0]))

    def activateGetButton(self, event):
        item = self.treeView.selection()
        if item:
            self.modifier.configure(bg="#3838e2", fg="white", state=NORMAL)

    def modifierAnimal(self):
        item = self.treeView.selection()
        if item:
            try:
                title = self.modifier.configure()['text'][-1]
                selected_item = item[0]
                lst = self.treeView.item(selected_item)['values']
                if title == 'Get':
                    self.Id_animal.insert(0, lst[1])
                    self.Id_animal.configure(state=DISABLED)
                    self.Nom.insert(0, lst[2])
                    self.DoesPerDay.insert(0, lst[5])
                    self.Prix.insert(0, lst[6])

                    self.modifier.configure(text='Modifier')
                    self.ajouter.configure(
                        bg="#D3D3D3", fg="black", state=DISABLED)
                else:
                    if self.verif():
                        self.treeView.item(item, values=(lst[0], self.Id_animal.get(), self.Nom.get(
                        ), self.DateDebut.get(), self.DateFin.get(), self.DoesPerDay.get(), self.Prix.get()))
                        tpl = (self.Nom.get(), self.DateDebut.get(), self.DateFin.get(
                        ), self.DoesPerDay.get(), self.Prix.get(), lst[0])
                        gestionTreat.updateTbl(tpl)
                        self.Id_animal.configure(state=NORMAL)
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
        self.Id_animal.delete(0, END)
        self.Nom.delete(0, END)
        self.DateDebut.delete(0, END)
        self.DateFin.delete(0, END)
        self.DoesPerDay.delete(0, END)
        self.Prix.delete(0, END)

    def inserting(self):
        if self.verif():
            self.returnMaxid()
            i = self.max + 1
            self.treat.initialize(i, self.Id_animal.get(), self.Nom.get(), self.DateDebut.get(
            ), self.DateFin.get(), self.DoesPerDay.get(), self.Prix.get())
            tpl = self.treat.getAllInfos()
            self.treeView.insert(parent='', index=i,
                                 iid=i, text='h', values=tpl)
            self.treat.setIdAnimal(
                gestionAnim.selectRef(self.Id_animal.get())[0][0])
            tpl = self.treat.getAllInfos()
            gestionTreat.insertTbl(tpl[1:])
            self.emptying()

    def verif(self):
        if self.Id_animal.get() != '' and self.Nom.get() != '' and self.DateDebut.get() != '' and self.DateFin.get() != '' and self.DoesPerDay.get() != '' and self.Prix.get() != '':
            if gestionAnim.selectRef(self.Id_animal.get()):
                return True
            else:
                messagebox.showinfo(
                    "warning", "the client you picked does not exist !")
        else:
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
