from Data.animal import Animal

class Cat(Animal):
    
    def __init__(self,ID,name,bornYear,disponibility,description,race,height,healthCondition):
        
        super().__init__(ID, name, bornYear, disponibility, description) #Inherits from Animal
        
        self._possibleRaces=["Siames", "Persa","Angora","Otro"] #Covered races
        
        if race not in self._possibleRaces: # this is for not covered races
            self._race = "Otro"
            
        else:
            self._race=race
        self._height = height
        self._healthCondition = healthCondition


    """ Getters and setters for Cat """

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        print("race es un atributo de solo lectura")


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


    @property
    def healthCondition(self):
        return self._healthCondition

    @healthCondition.setter
    def healthCondition(self, healthCondition):
        self._healthCondition = healthCondition
