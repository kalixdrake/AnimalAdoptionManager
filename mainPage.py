import tkinter as tk
from tkinter import ttk,messagebox
from dog import Dog
from cat import Cat

class MainPage(tk.Tk):
    def __init__(self, manager):
        super().__init__()
        self.title("Adoption Manager")
        self._manager=manager
        self._createMenu()
        self._createFilterMenu()
        self._createList()

    

    def _createMenu(self):
        """Create the menu"""
        menu = tk.Menu(master=self)
        self.config(menu=menu)
        """Create a cascade menu for filters"""
        filterMenu = tk.Menu(master=menu)
        menu.add_cascade(label="Inicio", menu=filterMenu)

        filterMenu.add_command(
            label="Base de datos",
 
        )
        filterMenu.add_command(
            label="Filtrar por ID",
        )

        """Create a cascade menu for status of the animals"""
        statusMenu = tk.Menu(master=self)
        menu.add_cascade(label="Gestionar", menu=statusMenu)
        statusMenu.add_command(
            label="Modificar informacion",
        )
        statusMenu.add_command(
            label="Cambiar estado de adopcion",
        )
        statusMenu.add_command(
            label="Cambiar estado de salud", 
        )
        statusMenu.add_command(
            label="Ingresar Nuevo",
            command=self.creationWindow
        )

    """Methods for the creation of the filter Menu"""
    def _createFilterMenu(self):
        filterFrame = tk.Frame(master=self)
        filterFrame.grid(row=0,column=0,)
        """Disponibility label and text selection"""
        self.disponibility=tk.StringVar(value="No filtrar")
        self.dispLabel = tk.Label(
            master=filterFrame,
            text="Disponibilidad",
            )
        self.dispLabel.grid(row=0,column=0, 
                            columnspan=2,
                            padx=20,
                            pady=10,
                            sticky="nsew"
                            )

        self.dispList=ttk.Combobox(
            master=filterFrame,
            state="readonly",
            values=["No filtrar", "Disponibles", "No disponibles"],
            textvariable=self.disponibility
            )
        self.dispList.grid(row=1,column=0,
                           columnspan=2,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )

        """Health status label and text selection"""
        self.health=tk.StringVar(value="No filtrar")
        self.healthLabel = tk.Label(
            master=filterFrame,
            text="Condicion de salud",
            )
        self.healthLabel.grid(row=3,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )


        self.healthList=ttk.Combobox(
            master=filterFrame,
            state="readonly",
            values=["No filtrar", "Saludables", "No saludables"],
            textvariable=self.health
            )
        self.healthList.grid(row=4,column=0,
                           columnspan=2,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        """Species label and text selection"""
        self.species=tk.StringVar(value="No filtrar")
        self.speciesLabel = tk.Label(
            master=filterFrame,
            text="Especie",
            )
        self.speciesLabel.grid(row=5,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )

        self.speciesList=ttk.Combobox(
            master=filterFrame,
            state="readonly",
            values=["No filtrar", "Perro", "Gato"],
            textvariable=self.species
            )
        self.speciesList.grid(row=6,column=0,
                           columnspan=2,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        self.speciesList.bind("<<ComboboxSelected>>", self.enableRaceList)
        

        """Races label and text selection"""
        self.race=tk.StringVar(value="No filtrar")
        self.raceLabel = tk.Label(
            master=filterFrame,
            text="Raza",
            )
        self.raceLabel.grid(row=7,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )

        self.raceList=ttk.Combobox(
            master=filterFrame,
            state="readonly",
            textvariable=self.race
            )
        self.raceList.grid(row=8,column=0,
                           columnspan=2,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        self.raceList.config(state="disabled")

        

        """Ages label and text selection"""
        self.minAge=tk.StringVar(value="")
        self.maxAge=tk.StringVar(value="")
        self.ageLabel = tk.Label(
            master=filterFrame,
            text="Filtro de edad",
            )
        self.ageLabel.grid(row=9,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.minAgeLabel = tk.Label(
            master=filterFrame,
            text="Minima",
            anchor="w"
            )
        self.minAgeLabel.grid(row=10,column=0, 
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.maxAgeLabel = tk.Label(
            master=filterFrame,
            text="Maxima",
            anchor="w"
            )
        self.maxAgeLabel.grid(row=10,column=1, 
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )

        """Entry of min and max age"""
        self.minAgeEntry=tk.Entry(
            master=filterFrame,
            textvariable=self.minAge
            )
        self.minAgeEntry.grid(row=11,column=0,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        self.maxAgeEntry=tk.Entry(
            master=filterFrame,
            textvariable=self.maxAge
            )
        self.maxAgeEntry.grid(row=11,column=1,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        """Buttons for clear filter and apply filter"""
        self.applyButton=tk.Button(
            master=filterFrame,
            text="Aplicar",
            command=self.filterAndRefresh
            )
        self.applyButton.grid(row=12,column=0,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                            )


        self.cleanButton=tk.Button(
            master=filterFrame,
            text="Limpiar",
            command=self.cleanFilter
            )
        self.cleanButton.grid(row=12,column=1,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                            )
        

    def enableRaceList(self,event):
        """Enable raceList when species filter is given ans set values for each species"""
        species=event.widget.get()
        if species=="Perro":
            self.raceList.config(values=["No filtrar", "Labrador", "BullDog","Golden","Otro"])
            self.raceList.config(state="readonly") 
        elif species=="Gato":
            self.raceList.config(values=["No filtrar", "Siames", "Persa","Angora","Otro"])
            self.raceList.config(state="readonly") 
        elif species=="No filtrar":
            self.raceList.config(state="disabled")  

    def cleanFilter(self):
        """Setup vars to default"""
        self.disponibility.set("No filtrar")
        self.health.set("No filtrar")
        self.species.set("No filtrar")
        self.race.set("No filtrar")
        self.minAge.set("")
        self.maxAge.set("")
        """disable raceList and enable applyButton"""
        self.applyButton.config(state="normal")
        self.raceList.config(state="disabled")
        """Restart the list"""
        self._manager._filter._filteredList=self._manager._animals
        self.Table.delete(*self.Table.get_children())
        for animal in self._manager._filter._filteredList:
            if isinstance(animal,Dog):
                sp="Perro"
            elif isinstance(animal,Cat):
                sp="Gato"
            self.Table.insert("",tk.END,text=str(animal._ID),
            values=(str(animal._name),sp,str(animal._race),str(animal.age()))
            )
    """Methods for the creation of the list"""

    def _createList(self):
        listFrame=tk.Frame(master=self)
        listFrame.grid(row=0,column=1)
        self.Table=ttk.Treeview(master=listFrame,
            columns=("Nombre","Especie","Raza","Edad"),
            height=20,
            selectmode="browse"
        )
        self.Table.grid(row=0,column=0,
                   columnspan= 5,
                   sticky="nsew"
                   )

        self.Table.heading("#0", text="ID")
        self.Table.heading("#1", text="NOMBRE")
        self.Table.heading("#2", text="ESPECIE")
        self.Table.heading("#3", text="RAZA")
        self.Table.heading("#4", text="EDAD")

        for animal in self._manager._filter._filteredList:
            if isinstance(animal,Dog):
                sp="Perro"
            elif isinstance(animal,Cat):
                sp="Gato"
            self.Table.insert("",tk.END,text=str(animal._ID),
            values=(str(animal._name),sp,str(animal._race),str(animal.age())),
            tags=("mytag",)
            )
        
        self.Table.tag_bind("mytag", "<<TreeviewSelect>>",self.showInfo)
        
    def filterAndRefresh(self):
        self.Table.delete(*self.Table.get_children())
        self._manager.applyFilter( self.disponibility.get(),self.health.get(),self.species.get(),self.race.get(),self.minAge.get(),self.maxAge.get())
        for animal in self._manager._filter._filteredList:
            if isinstance(animal,Dog):
                sp="Perro"
            elif isinstance(animal,Cat):
                sp="Gato"
            self.Table.insert("",tk.END,text=str(animal._ID),
            values=(str(animal._name),sp,str(animal._race),str(animal.age())),
            tags=("mytag",)
            )
        self.applyButton.config(state="disabled")
        self.Table.tag_bind("mytag", "<<TreeviewSelect>>",self.showInfo)

    def showInfo(self,event):
        """Identify Selection"""
        item = event.widget.selection()[0]
        text = self.Table.item(item, option="text")
        for animal in self._manager._animals:
            if int(animal._ID)==int(text):
                selectedAnimal=animal
                break
        """Create the secundary window to display info""" 
        self.infoWindow=tk.Toplevel()
        self.infoWindow.title("Nuevo Animal")
        self.infoWindow.config(width=200,height=200)

        self.IDLabel=tk.Label(
            master=self.infoWindow,
            text="ID:"+str(selectedAnimal._ID),
            )
        self.IDLabel.grid(row=0,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.NameLab=tk.Label(
            master=self.infoWindow,
            text="Name:"+str(selectedAnimal._name),
            )
        self.NameLab.grid(row=1,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.ageLab=tk.Label(
            master=self.infoWindow,
            text="Edad:"+str(selectedAnimal.age()),
            )
        self.ageLab.grid(row=2,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        if isinstance(selectedAnimal,Cat):
            especie="Gato"
        else:
            especie="Perro"

        self.speciesLab=tk.Label(
            master=self.infoWindow,
            text="Especie:"+str(especie),
            )
        self.speciesLab.grid(row=3,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.raceLab=tk.Label(
            master=self.infoWindow,
            text="Raza:"+str(selectedAnimal._race),
            )
        self.raceLab.grid(row=4,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.heightLab=tk.Label(
            master=self.infoWindow,
            text="tamaño:"+str(selectedAnimal._height),
            )
        self.heightLab.grid(row=5,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.descriptionLab=tk.Label(
            master=self.infoWindow,
            text="Descripcion:\n"+str(selectedAnimal._description),
            )
        self.descriptionLab.grid(row=4,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        if selectedAnimal._disponibility:
            disponibilidad="Disponible"
        else:
            disponibilidad="No Disponible"
        self.disponibilityLab=tk.Label(
            master=self.infoWindow,
            text="Disponibilidad:\n"+str(disponibilidad),
            )
        self.disponibilityLab.grid(row=0,column=3, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        if selectedAnimal._healthCondition:
            disponibilidad="Saludable"
        else:
            disponibilidad="No Saludable"
        self.disponibilityLab=tk.Label(
            master=self.infoWindow,
            text="Estado de salud:\n"+str(disponibilidad),
            )
        self.disponibilityLab.grid(row=1,column=3, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
    """Create the secundary window to create a new animal"""
    def creationWindow(self):
        """Create the window"""
        self.newAnimalWindow=tk.Toplevel()
        self.newAnimalWindow.title("Nuevo Animal")
        self.newAnimalWindow.config(width=200,height=200)
        """Create the entrys for the values"""
        """newSpecies label and text selection"""
        self.newSpecies=tk.StringVar(value="")
        self.newSpeciesLabel=tk.Label(
            master=self.newAnimalWindow,
            text="Especie",
            )
        self.newSpeciesLabel.grid(row=0,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )

        self.newSpeciesList=ttk.Combobox(
            master=self.newAnimalWindow,
            state="readonly",
            values=["Perro", "Gato"],
            textvariable=self.newSpecies
            )
        self.newSpeciesList.grid(row=1,column=0,
                           columnspan=2,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        self.newSpeciesList.bind("<<ComboboxSelected>>", self.enableNewRaceList)
        
        """newRace label and text selection"""
        self.newRace=tk.StringVar(value="")
        self.newRaceLabel=tk.Label(
            master=self.newAnimalWindow,
            text="Raza",
            )
        self.newRaceLabel.grid(row=2,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )

        self.newRaceList=ttk.Combobox(
            master=self.newAnimalWindow,
            state="readonly",
            textvariable=self.newRace
            )
        self.newRaceList.grid(row=3,column=0,
                           columnspan=2,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )

        self.newRaceList.config(state="disabled")

        """newName label and text entry"""
        self.newName=tk.StringVar(value="")
        self.newNameLabel=tk.Label(
            master=self.newAnimalWindow,
            text="Nombre",
            )
        self.newNameLabel.grid(row=4,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.newNameEntry=tk.Entry(
            master=self.newAnimalWindow,
            textvariable=self.newName
            )
        self.newNameEntry.grid(row=5,column=0,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        """newBornYear label and text entry"""
        self.newBornYear=tk.StringVar(value="")
        self.newBornYearLabel=tk.Label(
            master=self.newAnimalWindow,
            text="Año de nacimiento",
            )
        self.newBornYearLabel.grid(row=6,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.newBornYearEntry=tk.Entry(
            master=self.newAnimalWindow,
            textvariable=self.newBornYear
            )
        self.newBornYearEntry.grid(row=7,column=0,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        """newHeight label and text entry"""
        self.newHeight=tk.StringVar(value="")
        self.newHeightLabel=tk.Label(
            master=self.newAnimalWindow,
            text="Tamaño",
            )
        self.newHeightLabel.grid(row=8,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.newHeightEntry=tk.Entry(
            master=self.newAnimalWindow,
            textvariable=self.newHeight
            )
        self.newHeightEntry.grid(row=9,column=0,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        """newDescription label and text entry"""
        self.newDescription=tk.StringVar(value="")
        self.newDescriptionLabel=tk.Label(
            master=self.newAnimalWindow,
            text="Descripcion",
            )
        self.newDescriptionLabel.grid(row=10,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )
        
        self.newDescriptionEntry=tk.Entry(
            master=self.newAnimalWindow,
            textvariable=self.newDescription
            )
        self.newDescriptionEntry.grid(row=11,column=0,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )

        """newHealth label ant text selection"""
        self.newHealth = tk.BooleanVar(self)
        self.newHealthCheckbox = ttk.Checkbutton(
            master=self.newAnimalWindow,
            text="Saludable", 
            variable=self.newHealth
            )

        self.newHealthCheckbox.grid(row=12,column=0,
                            padx=20,
                            pady=10,
                            sticky="nsew",
                            )
        
        """Cancel and create button"""
        self.cancelButton=tk.Button(
            master=self.newAnimalWindow,
            text="Cancelar",
            command=self.closeWindow
            )
        self.cancelButton.grid(row=13,column=0,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                            )


        self.createButton=tk.Button(
            master=self.newAnimalWindow,
            text="Crear",
            command=self.createAnimal
            )
        self.createButton.grid(row=13,column=1,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                            )

    def enableNewRaceList(self,event):
        """Enable raceList when species filter is given ans set values for each species"""
        species=event.widget.get()
        if species=="Perro":
            self.newRaceList.config(values=["Labrador", "BullDog","Golden","Otro"])
            self.newRaceList.config(state="readonly") 
        elif species=="Gato":
            self.newRaceList.config(values=["Siames", "Persa","Angora","Otro"])
            self.newRaceList.config(state="readonly")   
        
    def closeWindow(self):
        self.newAnimalWindow.destroy()
    
    def createAnimal(self):
        if self.newSpecies.get()=="Perro":
            self._manager.newAnimal("Dog",self.newName.get(),str(self.newBornYear.get()),"True",self.newDescription.get(),self.newRace.get(),str(self.newHeight.get()),str(self.newHealth.get()))
        elif self.newSpecies.get()=="Gato":
            self._manager.newAnimal("Cat",self.newName.get(),str(self.newBornYear.get()),"True",self.newDescription.get(),self.newRace.get(),str(self.newHeight.get()),str(self.newHealth.get()))    
        self.closeWindow()