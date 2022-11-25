from dog import Dog
from cat import Cat
class Filter:
    def __init__(self):
        self._filteredList=[]

    def filterByDisponibility(self,filt):
        filtered=[]
        if filt=="Disponibles":
            filtered=list(filter(lambda animal: animal._disponibility==True,self._filteredList))
            self._filteredList=filtered
        elif filt=="No Disponibles":
            filtered=list(filter(lambda animal: animal._disponibility==False,self._filteredList))
            self._filteredList=filtered

    
    def filterByHealth(self,filt):
        if filt=="Saludables":
            self._filteredList=list(filter(lambda animal: animal.healthCondition==True,self._filteredList))
        elif filt=="No saludables":
            self._filteredList=list(filter(lambda animal: animal.healthCondition==False,self._filteredList))

    def filterBySpecies(self,filt):
        if filt=="Perro":
            self._filteredList=list(filter(lambda animal: isinstance(animal,Dog),self._filteredList))
        elif filt=="Gato":
            self._filteredList=list(filter(lambda animal: isinstance(animal,Cat),self._filteredList))

    def filterByRace(self,species,filt):
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
        if int(min)>=0 and int(max)>=0:
            self._filteredList=list(filter(lambda animal: int(animal.age())>=int(min) and int(animal.age())<=int(max),self._filteredList))

    def checkDisponibility(self,ID):
        for animal in self.disponibleAnimals:
            if animal.ID==ID:
                return "El animal {animal.name} con ID {animal.ID} está disponible en este momento"
            else:
                continue

        return "El animal con esta ID no está disponible o no existe"
