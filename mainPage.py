import tkinter as tk
from tkinter import ttk
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
        menu.add_cascade(label="Catalogo", menu=filterMenu)

        filterMenu.add_command(
            label="Filtrar por disponibles",
 
        )
        filterMenu.add_command(
            label="Filtrar por especie y raza",
        )
        filterMenu.add_command(
            label="Filtrar por edad",
        )
        filterMenu.add_command(
            label="Reestablecer filtros",
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
        statusMenu.add_command(label="Cambiar estado de salud", 
        )

    """Methods for the creation of the filter Menu"""
    def _createFilterMenu(self):
        filterFrame = tk.Frame(master=self)
        filterFrame.pack(fill=tk.X)
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
        self.healthLabel.grid(row=0,column=3, 
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
        self.healthList.grid(row=1,column=3,
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
        self.speciesLabel.grid(row=2,column=0, 
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
        self.speciesList.grid(row=3,column=0,
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
        self.raceLabel.grid(row=2,column=3, 
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
        self.raceList.grid(row=3,column=3,
                           columnspan=2,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        self.raceList.config(state="disabled")

        

        """Races label and text selection"""
        self.minAge=tk.StringVar(value="")
        self.maxAge=tk.StringVar(value="")
        self.ageLabel = tk.Label(
            master=filterFrame,
            text="Filtro de edad",
            )
        self.ageLabel.grid(row=4,column=0, 
                              columnspan=2,
                              padx=20,
                              pady=10,
                              sticky="nsew"
                              )

        """Entry of min and max age"""
        self.minAgeEntry=tk.Entry(
            master=filterFrame,
            textvariable=self.minAge
            )
        self.minAgeEntry.grid(row=5,column=0,
                           columnspan=2,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                           )
        
        self.maxAgeEntry=tk.Entry(
            master=filterFrame,
            textvariable=self.maxAge
            )
        self.maxAgeEntry.grid(row=5,column=3,
                           columnspan=2,
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
        self.applyButton.grid(row=6,column=0,
                           padx=20,
                           pady=10,
                           sticky="nsew"
                            )


        self.cleanButton=tk.Button(
            master=filterFrame,
            text="Limpiar",
            command=self.cleanFilter
            )
        self.cleanButton.grid(row=6,column=2,
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
        """disable raceList"""
        self.raceList.config(state="disabled")
        self._manager._filter._filteredList=self._manager._animals
        self.Table.delete(*self.Table.get_children())
        for animal in self._manager._filter._filteredList:
            print(type(animal._disponibility))
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
        listFrame.pack(fill=tk.X)
        self.Table=ttk.Treeview(master=listFrame,
            columns=("Nombre","Especie","Raza","Edad")
        )
        self.Table.grid(row=4,column=0,
                   columnspan= 5,
                   sticky="nsew"
                   )

        self.Table.heading("#0", text="ID")
        self.Table.heading("#1", text="NOMBRE")
        self.Table.heading("#2", text="ESPECIE")
        self.Table.heading("#3", text="RAZA")
        self.Table.heading("#4", text="EDAD")

        for animal in self._manager._filter._filteredList:
            print(type(animal._disponibility))
            if isinstance(animal,Dog):
                sp="Perro"
            elif isinstance(animal,Cat):
                sp="Gato"
            self.Table.insert("",tk.END,text=str(animal._ID),
            values=(str(animal._name),sp,str(animal._race),str(animal.age()))
            )
        
    def filterAndRefresh(self):
        self.Table.delete(*self.Table.get_children())
        self._manager.applyFilter( self.disponibility.get(),self.health.get(),self.species.get(),self.race.get(),self.minAge.get(),self.maxAge.get())
        for animal in self._manager._filter._filteredList:
            print(type(animal._disponibility))
            if isinstance(animal,Dog):
                sp="Perro"
            elif isinstance(animal,Cat):
                sp="Gato"
            self.Table.insert("",tk.END,text=str(animal._ID),
            values=(str(animal._name),sp,str(animal._race),str(animal.age()))
            )