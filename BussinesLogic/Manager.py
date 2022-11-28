from Data.cat import Cat
from Data.dog import Dog

class Manager:
    """This is the most important class of the project, it contains the methods that allow the user to interact with the program,
    it also contains the list of animals and is able to filter the animals by implementing the filter class"""

    def __init__(self,animalData,filter):
        self._animalData = animalData
        self._animals=[]
        self._filter=filter
        self.createAnimals()
        self._filter._filteredList=self._animals


    def createAnimal(self, record):
        """Create an Animal object from an arrange"""
        record = list(map(lambda x: x.strip(), record))

        if record[1] == 'Cat':
            #format: [id,class,name,bornyear,disponibility,description,race,height,healthcondition]
            return Cat(int(record[0]), record[2], int(record[3]), record[4]=="True", record[5], record[6],int(record[7]),record[8]=="True")

        if record[1] == 'Dog':
            #format: [id,class,name,bornyear,disponibility,description,race,height,healthcondition]
            return Dog(int(record[0]), record[2], int(record[3]), record[4]=="True", record[5], record[6],int(record[7]),record[8]=="True")


    def createAnimals(self):
        """Read a data file and create Animal objects with the attributes of the file"""
        
        with open(self._animalData, 'r') as info:
            for line in info:
                self._animals.append(self.createAnimal(line.split(",")))


    def newAnimal(self,clase,name,bornyear,disponibility,description,race,height,healthcondition):
        """Receives the attributes and create an animal with the method createAnimal"""    
        
        animal=[str((self.maxID())+1),clase,name,bornyear,disponibility,description,race,height,healthcondition]
        self._animals.append(self.createAnimal(animal))


    def maxID(self):
        """Return the max ID"""
        
        listID = list(map(lambda x: x.ID, self._animals))
        return max(listID)


    def applyFilter(self,disp,health,species,race,minAge,maxAge):
        """This is the method that applies the filter to the list of animals given by the user in the GUI"""
        
        if disp!="No filtrar":
            self._filter.filterByDisponibility(disp)
        if health!="No filtrar":
            self._filter.filterByHealth(health)
        if species!="No filtrar":
            self._filter.filterBySpecies(species)
        if race!="No filtrar":
            self._filter.filterByRace(species,race)
        if minAge=="":
            minAge=0
        if maxAge=="":
            maxAge=10000
        self._filter.filterByAge(int(minAge),int(maxAge))


    def saveData(self):
        """This method is automatically called when the user closes the program, it saves the data in the file for preventing data loss"""

        with open("resources/base1.csv","w") as data:
                for animal in self._animals:
                    if isinstance(animal,Cat):
                        spec="Cat"
                    else:
                        spec="Dog"
                    data.write(str(animal._ID)+","+str(spec)+","+str(animal._name)+","+str(animal._bornYear)+","+str(animal._disponibility)+","+str(animal._description)+","+str(animal._race)+","+str(animal._height)+","+str(animal.healthCondition)+"\n")


    def checkDisponibility(self,ID):
        """This method is used to check if an animal is available for adoption"""

        disponibles=list(filter(lambda animal: animal._disponibility==True,self._animals))
        for animal in disponibles:
            if animal._ID==ID:
                return "El animal {animal.name} con ID {animal.ID} está disponible en este momento"
            else:
                continue


    def searchID(self,id):
        """This method is used to search an animal by ID, it returns the animal object so one can modify the attributes of the animal"""

        for animal in self._animals:
            if str(animal._ID)==str(id):
                return animal
        return None


    def change(self,ID,description,height,disponibility,health):
        """This method is used to modify the attributes of an animal that are not permanent
        such as the ID, name, bornyear and species of the animal"""
        animal=self.searchID(ID)
        animal._description=description
        animal._height=height
        animal._disponibility=disponibility
        animal._healthCondition=health
