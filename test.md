  # Widgets CustomTkinter
  
  1. CTk
     - CTk() : Crée une instance de la fenêtre principale.
     ```python
     import customtkinter as ctk
     app = ctk.CTk()
     app.mainloop()
     ```
  2. CTkButton
     - CTkButton(master, text, command, fg_color, hover_color, ...) : Crée un bouton avec diversesoptions de personnalisation.
     ```python
     button = ctk.CTkButton(master=app, text="Cliquez-moi", command=lambda: print("Bouton cliqué!"))
     button.pack(pady=10)
     ```
  3. CTkLabel
     - CTkLabel(master, text, ...) : Crée une étiquette.
     ```python
     label = ctk.CTkLabel(master=app, text="Hello, CustomTkinter!")
     label.pack(pady=10)
     ```
  4. CTkEntry
     - CTkEntry(master, ...) : Crée un champ de saisie.
     ```python
     entry = ctk.CTkEntry(master=app)
     entry.pack(pady=10)
     ```
  5. CTkTextbox
     - CTkTextbox(master, ...) : Crée une zone de texte.
     ```python
     textbox = ctk.CTkTextbox(master=app)
     textbox.pack(pady=10)
     ```
  6. CTkFrame
     - CTkFrame(master, ...) : Crée un cadre (container).
     ```python
     frame = ctk.CTkFrame(master=app)
     frame.pack(pady=10, fill="both", expand=True)
     ```
  7. CTkProgressBar
     - CTkProgressBar(master, ...) : Crée une barre de progression.
     ```python
     progress = ctk.CTkProgressBar(master=app)
     progress.pack(pady=10)
     progress.set(0.5)
     ```
  8. CTkSlider
     - CTkSlider(master, from_, to, ...) : Crée un curseur (slider).
     ```python
     slider = ctk.CTkSlider(master=app, from_=0, to=1)
     slider.pack(pady=10)
     ```
  9. CTkOptionMenu
     - CTkOptionMenu(master, values, ...) : Crée un menu déroulant.
     ```python
     option_menu = ctk.CTkOptionMenu(master=app, values=["Option 1", "Option 2", "Option 3"])
     option_menu.pack(pady=10)
     ```
  10. CTkCheckBox
      - CTkCheckBox(master, text, ...) : Crée une case à cocher.
      ```python
      checkbox = ctk.CTkCheckBox(master=app, text="Je suis d'accord")
      checkbox.pack(pady=10)
      ```
  11. CTkRadioButton
      - CTkRadioButton(master, text, value, ...) : Crée un bouton radio.
      ```python
      radio_button = ctk.CTkRadioButton(master=app, text="Option 1", value=1)
      radio_button.pack(pady=10)
      ```
  12. CTkSwitch
      - CTkSwitch(master, text, ...) : Crée un interrupteur (switch).
      ```python
      switch = ctk.CTkSwitch(master=app, text="Activer")
      switch.pack(pady=10)
      ```
  13. CTkCanvas
      - CTkCanvas(master, ...) : Crée un canvas pour le dessin.
      ```python
      canvas = ctk.CTkCanvas(master=app, width=200, height=200)
      canvas.pack(pady=10)
      canvas.create_line(0, 0, 200, 200)
      ```
  14. CTkScrollableFrame
      - CTkScrollableFrame(master, ...) : Crée un cadre défilable.
      ```python
      scrollable_frame = ctk.CTkScrollableFrame(master=app)
      scrollable_frame.pack(pady=10, fill="both", expand=True)
      ```
  ## Méthodes et Propriétés Communes
  - pack(), grid(), place() : Méthodes de gestion de géométrie pour placer les widgets dans la fenêtre.
    ```python
    label.pack(pady=10)
    label.grid(row=0, column=0)
    label.place(x=50, y=50)
    ```
  - configure(**options) : Modifie les options d'un widget après sa création.
    ```python
    button.configure(text="Nouveau texte")
    ```
  - bind(event, handler) : Associe un gestionnaire d'événement à un widget.
    ```python
    button.bind("<Button-1>", lambda e: print("Bouton cliqué!"))
    ```
  - cget(option) : Retourne la valeur d'une option du widget.
    ```python
    text = button.cget("text")
    print(text)
    ```
  - destroy() : Détruit le widget.
    ```python
    button.destroy()
    ```
  ## Options Communes pour les Widgets
  - master : Le parent du widget.
    ```python
    button = ctk.CTkButton(master=app)
    ```
  - text : Le texte affiché sur le widget.
    ```python
    button = ctk.CTkButton(master=app, text="Cliquez-moi")
    ```
  - command : La fonction à appeler lorsque l'événement spécifié se produit (par exemple, clic sur unbouton).
    ```python
    button = ctk.CTkButton(master=app, command=lambda: print("Bouton cliqué!"))
    ```
  - fg_color, bg_color : Couleurs de premier plan et de fond.
    ```python
    button = ctk.CTkButton(master=app, fg_color="blue", bg_color="yellow")
    ```
  - width, height : Dimensions du widget.
    ```python
    button = ctk.CTkButton(master=app, width=100, height=50)
    ```
  - font : Police de caractères utilisée pour le texte du widget.
    ```python
    button = ctk.CTkButton(master=app, font=("Helvetica", 16))
    ```
  - state : État du widget ("normal", "disabled", etc.).
    ```python
    button = ctk.CTkButton(master=app, state="disabled")
    ```
  """
