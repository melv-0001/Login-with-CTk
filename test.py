import customtkinter as ctk

#instance de fenetre
app = ctk.CTk()
#modifs fenetre principal 

app.title("Hello, CustomTkinter!")
app.geometry("500x500")
app.resizable(False, False)
app.configure(bg="white")
app.iconbitmap("icone.png")

# couleur theme et option
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#création d'un cadre 
#frame = ctk.CTkFrame(master=app)
#frame.pack(pady=10, fill="both", expand=True)

#création d'un boutton
button = ctk.CTkButton(master=app
                       #"""pr apparaitre sur le frame : frame"""
                       , text="Cliquez-moi", command=lambda: print("Bouton cliqué!"))
button.pack(pady=10)
#modifs après création
#button.configure(text="Nouveau texte")
#

#creation d'un label
label = ctk.CTkLabel(master=app, text="Hello, CustomTkinter!")
label.pack(pady=10)
#label.grid(row=0, column=0)
#label.place(x=50, y=50)

#creation d'un champ de saisie
entry = ctk.CTkEntry(master=app)
entry.pack(pady=10)

#création d'une zone de texte
#textbox = ctk.CTkTextbox(master=app)
#textbox.pack(pady=10)

#création d'une barre de progression
#progress = ctk.CTkProgressBar(master=app)
#progress.pack(pady=10)
#progress.set(0.5)

#création d'un slider
slider = ctk.CTkSlider(master=app, from_=0, to=1)
slider.pack(pady=10)

#création d'un menu deroulant
option_menu = ctk.CTkOptionMenu(master=app, values=["Option 1", "Option 2", "Option 3"])
option_menu.pack(pady=10)

#création d'une case à cocher
checkbox = ctk.CTkCheckBox(master=app, text="Je suis d'accord")
checkbox.pack(pady=10)

#création d'un boutton radio(btn rond)
radio_button = ctk.CTkRadioButton(master=app, text="Option 1", value=1)
radio_button.pack(pady=10)

#création d'un interrupteur
switch = ctk.CTkSwitch(master=app, text="Activer")
switch.pack(pady=10)

#création d'un canva(zone où on dessine un elmt désiré)
canvas = ctk.CTkCanvas(master=app, width=200, height=200)
canvas.pack(pady=10)
canvas.create_line(0, 0, 200, 200)

#création d'un cadre défilant
scrollable_frame = ctk.CTkScrollableFrame(master=app)
scrollable_frame.pack(pady=10, fill="both", expand=True)

#gestion de la boucle d'affichage
app.mainloop()

