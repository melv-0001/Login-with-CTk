import customtkinter as ctk
import __main__ as main

#color_11 = "#B3B3B3"
#color_12 = "#D8D8D8"

class fenetre():
    def __init__(self):
        #création d'une instance de fenetre
        self.fenetre = ctk.CTk()
        #titre de la fenetre
        self.titre = self.fenetre.title("Login")
        #taille de la fenetre
        self.geometry = self.fenetre.geometry("900x600")
        #logo de la fenetre
        self.icon = self.fenetre.iconbitmap("")
        self.requirement()
        self.execute()
        

    def requirement(self):
        #création d'un cadre 
        self.frame = ctk.CTkFrame(master=self.fenetre, width=300, height=550)
        self.frame.pack(pady=10, expand=True)
        #ecrito d'introduction et d'inscription
        label = ctk.CTkLabel(master=self.frame, text="Formulaire d'inscription",text_color = "blue")
        label.pack(pady=10)

        #creation d'un champ de saisie
        for i in ["Nom","Prenom","Email","Mot de passe"]:

            self.entry = ctk.CTkEntry(master=self.frame,placeholder_text=i)
            self.entry.pack(pady=10)

        #création d'un boutton
        button = ctk.CTkButton(master= self.frame, text="Inscription", command=lambda: print("Bouton cliqué!"))
        button.pack(pady=10)
        
        
    
    def execute(self):
        self.fenetre.mainloop()
#instanciation de la fenetre
#if __name__ == "main" :
fenetre()




        