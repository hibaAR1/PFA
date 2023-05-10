from tkinter import Tk, Toplevel, Label, PhotoImage, Frame, Button
from PIL import Image, ImageTk

class animalInfo(Toplevel):
    def __init__(self,master,lst):
        super().__init__(master)
        self.title("Pet Card")
        self.overrideredirect(1)
        self.width_of_window = 284
        self.height_of_window = 442
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/2)
        self.geometry("%dx%d+%d+%d" % (self.width_of_window,
                                            self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.configure(bg="#272727")
        self.button = Button(self, text="X", command=self.close_window,bg="#272727",fg="white",border=0,font=("Helvetica", 16, "bold"))
        self.button.pack(anchor="ne",padx=10, pady=10)
        card_frame = Frame(self, bg="white", bd=2)
        card_frame.pack(pady=10)
        picture = Image.open(lst[7])
        self.picture_image = ImageTk.PhotoImage(picture)
        picture_label = Label(card_frame, image=self.picture_image)
        picture_label.pack()

        name_pet_label = Label(card_frame, text="Name: "+lst[2], font=("Helvetica", 12), bg="white")
        name_pet_label.pack()

        ref_pet_label = Label(card_frame, text="Ref: "+lst[3], font=("Helvetica", 12), bg="white")
        ref_pet_label.pack()

        sexe_pet_label = Label(card_frame, text="Sexe: "+lst[4], font=("Helvetica", 12), bg="white")
        sexe_pet_label.pack()

        date_naissance_pet_label = Label(card_frame, text="Date of Birth: "+lst[5], font=("Helvetica", 12), bg="white")
        date_naissance_pet_label.pack()

        type_pet_label = Label(card_frame, text="Type: "+lst[6], font=("Helvetica", 12), bg="white")
        type_pet_label.pack()
    def close_window(self):
        self.destroy()