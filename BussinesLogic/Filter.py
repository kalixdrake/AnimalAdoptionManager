from Manager import Manager

class Filter:
    def __init__(self,disponibleAnimals):
        self._disponibleAnimals=disponibleAnimals

    @property
    def disponibleAnimals(self,disponibleAnimals):
        return self._disponibleAnimals

    def checkDisponibility(self,ID):
        for animal in self.disponibleAnimals:
            if animal.ID==ID:
                return "El animal {animal.name} con ID {animal.ID} está disponible en este momento"
            else:
                continue

        return "El animal con esta ID no está disponible o no existe"
