
from Data.dog import Dog
from Data.cat import Cat

class Filter:
    """
    This class is the one who filters the animals the way we want,
    it is possible to aplly various filters at once and the result will be the intersection of all the filters
    because one filter is not dependant of another
    """
    
    def __init__(self):
        """
        This is the constructor of the class, it initializes the list of animals to filter
        """
        self._filteredList=[]


    def filterByDisponibility(self,filt):
        
        """This method filters the animals by their disponibility
        filt (string): This is the filter to apply, and it is predisposed by the options in te GUI
        """
        
        if filt=="Disponibles":
            self._filteredList=list(filter(lambda animal: animal._disponibility==True,self._filteredList))
        elif filt=="No Disponibles":
            self._filteredList=list(filter(lambda animal: animal._disponibility==False,self._filteredList))


    def filterByHealth(self,filt):
        
        """This method filters the animals by their health condition
        filt (string): This is the filter to apply, and it is predisposed by the options in te GUI
        """
        
        if filt=="Saludables":
            self._filteredList=list(filter(lambda animal: animal._healthCondition==True,self._filteredList))
        elif filt=="No saludables":
            self._filteredList=list(filter(lambda animal: animal._healthCondition==False,self._filteredList))


    def filterBySpecies(self,filt):
        
        """This method filters the animals by their species
        filt (string): This is the filter to apply, and it is predisposed by the options in te GUI
        """
        
        if filt=="Perro":
            self._filteredList=list(filter(lambda animal: isinstance(animal,Dog),self._filteredList))
        elif filt=="Gato":
            self._filteredList=list(filter(lambda animal: isinstance(animal,Cat),self._filteredList))


    def filterByRace(self,species,filt):
        
        """This method filters the animals by their race
        filt (string): This is the filter to apply, and it is predisposed by the options in te GUI
        """
        
        if species=="Perro":
            if filt=="Labrador":
                self._filteredList=list(filter(lambda animal: animal.race=="Labrador",self._filteredList))
            elif filt=="BullDog":
                self._filteredList=list(filter(lambda animal: animal.race=="BullDog",self._filteredList))
            elif filt=="Golden":
                self._filteredList=list(filter(lambda animal: animal.race=="Golden",self._filteredList))
            elif filt=="Otro":
                self._filteredList=list(filter(lambda animal: animal.race=="Otro",self._filteredList))
            
        elif species=="Gato":
            if filt=="Siames":
                self._filteredList=list(filter(lambda animal: animal.race=="Siames",self._filteredList))
            elif filt=="Persa":
                self._filteredList=list(filter(lambda animal: animal.race=="Persa",self._filteredList))
            elif filt=="Angora":
                self._filteredList=list(filter(lambda animal: animal.race=="Angora",self._filteredList))
            elif filt=="Otro":
                self._filteredList=list(filter(lambda animal: animal.race=="Otro",self._filteredList))


    def filterByAge(self,min,max):
        
        """This method filters the animals by their disponibility
        filt (string): This is the filter to apply, and it is predisposed by the options in te GUI
        """
        
        if int(min)>=0 and int(max)>=0:
            self._filteredList=list(filter(lambda animal: int(animal.age())>=int(min) and int(animal.age())<=int(max),self._filteredList))

    

        return "El animal con esta ID no está disponible o no existe"
