from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from data_base.connectDB import gestClients,gesttreatement,gestrendezvous
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from datetime import datetime

gestClient = gestClients()
gestTreat = gesttreatement()
gestRdv = gestrendezvous()

def generate_facture(data,client):
    pdf = SimpleDocTemplate("facture_pdf/{}.pdf".format(client[1]+"_"+datetime.today().strftime('%d_%m_%Y')), pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    header = Paragraph("<para align=center><b>Facture</b></para>", styles["Heading1"])
    elements.append(header)

    company_details = Paragraph("<para align=right><b>Cabinet Vet</b><br/>Facture Date: {}</para>".format(datetime.today().strftime('%d/%m/%Y')), styles["Normal"])
    elements.append(company_details)

    client_details = Paragraph("<para align=left><b>Client Information:</b><br/>First Name: {}<br/>Last Name: {}<br/>CNE: {}<br/>Phone Number: {}</para>".format(client[3],client[2],client[1],client[4]), styles["Normal"])
    elements.append(client_details)

    elements.append(Spacer(1, 0.25 * inch))

    table = Table(data, colWidths=[pdf.width / 3.0] * 3)
    table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 14),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.black),
        ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
    ]))

    elements.append(table)
    pdf.build(elements)
    messagebox.showinfo("pdf","Generated Successfully")
    
class Facture:
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
        self.titre = Label(text="Facture",
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
        
        
        #-------------------------- Entry Cne Client -----------------------------------------------
        self.cne_image1 = PhotoImage(file="./images/facture_cne.png")
        self.cne_image1_Label = Label(
            bg="#3d404b",
            image=self.cne_image1,

        )
        self.cne_image1_Label.place(x=397, y=336)

        self.cne_text = Label(
            self.cne_image1_Label,
            # prenom
            text="Enter Cne : ",
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
        self.Cne.place(x=8, y=22, width=650, height=25)
        #=========================================================================
        #------------------Button to generate the facture ------------------------
        self.ajouter = Button(self.root, text="Generate", bd=0, bg="#151515", fg="white",  font=('Courier', 11, "bold"),command=self.generateFacture)
        self.ajouter.place(x=635, y=421, width=230, height=49)
        #-------------------------------------------------------------------------        
        self.root.mainloop()
    def generateFacture(self):
        if self.Cne.get() != '':
            if gestClient.selectCne(self.Cne.get()):
                if gestClient.selectTreat(self.Cne.get()) or gestClient.selectRdv(self.Cne.get()):
                    data = [["Element", "Deplacement", "Prix"]]
                    total=0
                    for rdv in gestClient.selectRdv(self.Cne.get()):
                        data.append(["Consultation : "+rdv[2],rdv[4],str(self.getPrice(rdv[4]))+" DH"])
                        total +=self.getPrice(rdv[4])
                        gestRdv.paid(rdv[0])
                    for treat in gestClient.selectTreat(self.Cne.get()):
                        data.append(["Treatement : "+treat[2],"---",str(treat[6])+" DH"])
                        total += treat[6]
                        gestTreat.paid(treat[0])
                    data.append(["Total",'',str(total)+" DH"])
                    generate_facture(data,gestClient.selectCne(self.Cne.get())[0])
                else:
                    messagebox.showwarning("warning", "This Client paid everything")
            else:
                messagebox.showerror("Error", "This Client doesn\'t exist !!")
        else:
            messagebox.showerror("Error", "Fill the field please !!")
            
    def getPrice(self,dep):
        if dep == "Marrakech":
            return 300.0
        elif dep == "Casablanca":
            return 700.0
        else:
            return 1000.0
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
