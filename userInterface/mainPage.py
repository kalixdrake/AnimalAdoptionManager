import tkinter as tk
from functools import partial
from tkinter import ttk,messagebox
from Data.dog import Dog
from Data.cat import Cat
from Data.animal import Animal
from userInterface.Table import MyTreeview


class MainPage(tk.Tk):
    def __init__(self, manager):
        super().__init__()
        self.title("Adoption Manager")
        self._manager = manager
        self.protocol("WM_DELETE_WINDOW", self.saveAndClose)
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

        """Create a cascade menu for status of the animals"""
        statusMenu = tk.Menu(master=self)
        menu.add_cascade(label="Gestionar", menu=statusMenu)
        statusMenu.add_command(
            label="Modificar informacion",
            command=self.modifyWindow
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
        _columns=("Nombre","Especie","Raza","Edad")
        self.Table=MyTreeview(master=listFrame,
            columns=_columns,
            height=20,
            selectmode="browse",
            show= "headings"
        )
        
        sortType = ["name", "name", "name", "num"]
        
        for i in range(len(_columns)):
            strHdr = _columns[i]
            self.Table.heading(strHdr, text=strHdr, sort_by=sortType[i])
            self.Table.column(_columns[i], stretch=True)
        
        self.Table.pack()
        
        self.Table.grid(row=0,column=0,
                   columnspan= 5,
                   sticky="nsew"
                   )


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
            command=self.newAnimalWindow.destroy
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

    def modifyWindow(self):
        """Create the window"""
        self.modWindow=tk.Toplevel()
        self.modWindow.title("Nuevo Animal")
        self.modWindow.config(width=200,height=200)
        """Create the entrys for the values"""
        """ID search"""
        self.IDtext=tk.StringVar(value="")
        self.IDLabel=tk.Label(
            master=self.modWindow,
            text="ID:",
            )
        self.IDLabel.grid(row=0,column=0, 
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )

        self.IDEntry=tk.Entry(
            master=self.modWindow,
            textvariable=self.IDtext,
            )
        self.IDEntry.grid(row=0,column=1,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        self.searchButton=tk.Button(
            master=self.modWindow,
            text="Buscar",
            command=self.searchAndDisplay
            )
        self.searchButton.grid(row=0,column=3,
                            columnspan=2,
                            padx=20,
                            pady=10,
                            sticky="nsew"
                            )
    
    def searchAndDisplay(self):
        """Search the ID and display info, some info is enabled to be changed"""
        ID=self.IDtext.get()
        an=self._manager.searchID(ID)
        if isinstance(an,Animal):
            if isinstance(an,Cat):
                specie="Gato"
            else:
                specie="Perro"
            """Species label, it cannot be changed"""
            self.specLabel=tk.Label(
                master=self.modWindow,
                text=str("Especie:"+specie),
                )
            self.specLabel.grid(row=1,column=0, 
                                padx=20,
                                pady=10,
                                sticky="nsew",
                                )
            
            """Race label, it cannot be changed"""
            self.raceLabel=tk.Label(
                master=self.modWindow,
                text="Raza:"+str(an._race),
                )
            self.raceLabel.grid(row=1,column=1, 
                                padx=20,
                                pady=10,
                                sticky="nsew"
                                )

            """Name label, it cannot be changed"""
            self.nameLabel=tk.Label(
                master=self.modWindow,
                text="Nombre:"+str(an._name),
                )
            self.nameLabel.grid(row=2,column=0, 
                                padx=20,
                                pady=10,
                                sticky="nsew"
                                )
            
            """BornYear label, it cannot be changed"""
            self.bornLabel=tk.Label(
                master=self.modWindow,
                text="Nacimiento:"+str(an._bornYear),
                )
            self.bornLabel.grid(row=2,column=1, 
                                padx=20,
                                pady=10,
                                sticky="nsew"
                                )
            
            """Description label, it can be changed"""
            self.Desc=tk.StringVar(value=str(an._description))
            self.descLabel=tk.Label(
                master=self.modWindow,
                text="Descripcion:",
                )
            self.descLabel.grid(row=3,column=0, 
                                padx=20,
                                pady=10,
                                sticky="nsew"
                                )
            self.descEntry=tk.Entry(
            master=self.modWindow,
            textvariable=self.Desc,
            )
            self.descEntry.grid(row=3,column=1,
                            columnspan=5,
                            padx=10,
                            pady=10,
                            sticky="nsew"
                            )
            
            """Height label, it can be changed"""
            self.Height=tk.StringVar(value=str(an._height))
            self.HeLabel=tk.Label(
                master=self.modWindow,
                text="Tamaño:",
                )
            self.HeLabel.grid(row=4,column=0, 
                                padx=20,
                                pady=10,
                                sticky="nsew"
                                )
            self.HeEntry=tk.Entry(
            master=self.modWindow,
            textvariable=self.Height,
            )
            self.HeEntry.grid(row=4,column=1,
                            columnspan=5,
                            padx=10,
                            pady=10,
                            sticky="nsew"
                            )

            """Disponibility checkbox, it can be changed"""
            self.disp = tk.BooleanVar(value=an._disponibility)
            self.dispCheckbox = ttk.Checkbutton(
            master=self.modWindow,
            text="Disponible", 
            variable=self.disp
            )

            self.dispCheckbox.grid(row=5,column=0,
                            padx=20,
                            pady=10,
                            sticky="nsew",
                            )
            """Health condition checkbox, it can be changed"""
            self.hs = tk.BooleanVar(value=an._healthCondition)
            self.hsCheckbox = ttk.Checkbutton(
            master=self.modWindow,
            text="Saludable", 
            variable=self.hs
            )

            self.hsCheckbox.grid(row=5,column=1,
                            padx=20,
                            pady=10,
                            sticky="nsew",
                            )
            
            self.cancButton=tk.Button(
            master=self.modWindow,
            text="Cancelar",
            command=self.modWindow.destroy
            )
            self.cancButton.grid(row=6,column=0,
                            padx=20,
                            pady=10,
                            sticky="nsew"
                                )


            self.saveButton=tk.Button(
                master=self.modWindow,
                text="Guardar",
                command=self.changeInfo
                )
            self.saveButton.grid(row=6,column=1,
                            padx=20,
                            pady=10,
                            sticky="nsew"
                                )
        else:
            messagebox.showwarning(message="La ID buscada no fue encontrada", title="No encontrado")
            self.modWindow.destroy()
    
    def createAnimal(self):
        if self.newSpecies.get()=="Perro":
            self._manager.newAnimal("Dog",self.newName.get(),str(self.newBornYear.get()),"True",self.newDescription.get(),self.newRace.get(),str(self.newHeight.get()),str(self.newHealth.get()))
        elif self.newSpecies.get()=="Gato":
            self._manager.newAnimal("Cat",self.newName.get(),str(self.newBornYear.get()),"True",self.newDescription.get(),self.newRace.get(),str(self.newHeight.get()),str(self.newHealth.get()))    
        self.newAnimalWindow.destroy()
    
    def saveAndClose(self):
        self.close=messagebox.askokcancel(message="¿Desea continuar?\nSe guardaran los cambios realizados a la base de datos", title="Terminar Sesión")
        if self.close:
            self._manager.saveData()
            self.destroy()
    
    def changeInfo(self):
        self._manager.change(self.IDtext.get(),self.Desc.get(),self.Height.get(),self.disp.get(),self.hs.get())
        self.modWindow.destroy()