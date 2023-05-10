
from tkinter import *
# importe le module PIL (Python Imaging Library) qui permet de manipuler des images
from PIL import ImageTk, Image
import time
from login import Login


class LoadingPage:
    def __init__(self):
        #ne instance de la classe
        self.root = Tk()
        # Définit la largeur et la hauteur de la fenêtre
        self.width_of_window = 427
        self.height_of_window = 250
        # Définit la taille de la fenêtre
        self.root.geometry("%dx%d" % (self.width_of_window, self.height_of_window))
        # Calcule les coordonnées de la fenêtre sur l'écran
        x_pos = (self.root.winfo_screenwidth() - self.width_of_window) // 2
        y_pos = (self.root.winfo_screenheight() - self.height_of_window) // 2
        # Définit la position de la fenêtre sur l'écran
        self.root.geometry("+{}+{}".format(x_pos, y_pos))
        # utilisé pour indiquer que la fenêtre doit être sans bordure et sans barre de titre
        self.root.overrideredirect(1)
        
        Frame(self.root, width=427, height=250, bg='#272727').place(x=0, y=0)
        
        self.logo = PhotoImage(file="./images/footdog.png")
        self.background_label = Label(
            image=self.logo,
            bg='#272727'
        )
        self.background_label.place(x=188, y=40)
        
        self.label1 = Label(self.root, text='𝒫𝐸𝒯 𝒞𝒜𝑅𝐸 ',
                            fg='white', bg='#272727' ,font=("Calibri", 18, "bold") )

        self.label1.place(x=150, y=90)

        self.label2 = Label(self.root, text='Please wait...', fg='white',
                            bg='#272727' ,font=("Calibri", 11) )

        self.label2.place(x=10, y=215)

        self.image_a = ImageTk.PhotoImage(Image.open('./images/loadign.png'))
        self.image_b = ImageTk.PhotoImage(Image.open('./images/loadign2.png'))
        
        for i in range(5):  # boucle 5 fois 
            self.l1 = Label(self.root, image=self.image_a, border=0,
                            relief=SUNKEN).place(x=180, y=145)
            self.l2 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=200, y=145)
            self.l3 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=220, y=145)
            self.l4 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=240, y=145)
            # Met à jour la fenêtre :rafraîchir tous les éléments graphiques de la fenêtre,
            self.root.update_idletasks()
            #Attend 0.2 secondes
            time.sleep(0.2)
            self.l1 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=180, y=145)
            self.l2 = Label(self.root, image=self.image_a, border=0,
                            relief=SUNKEN).place(x=200, y=145)
            self.l3 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=220, y=145)
            self.l4 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.2)
            self.l1 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=180, y=145)
            self.l2 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=200, y=145)
            self.l3 = Label(self.root, image=self.image_a, border=0,
                            relief=SUNKEN).place(x=220, y=145)
            self.l4 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.2)
            self.l1 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=180, y=145)
            self.l2 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=200, y=145)
            self.l3 = Label(self.root, image=self.image_b, border=0,
                            relief=SUNKEN).place(x=220, y=145)
            self.l4 = Label(self.root, image=self.image_a, border=0,
                            relief=SUNKEN).place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)
        self.toLogin()

    def toLogin(self):
        self.root.destroy()
        from login import Login
        Login()

#Si le fichier est exécuté en tant que programme principal, la condition est vraie et le code sous la condition sera exécuté
if __name__ == '__main__':
    LoadingPage()
