from Animal import Animal

class Cat(Animal):
    """ Getters and setters for Cat """
    def __init__(self,ID,name,bornYear,disponibility,description,race,height,healthCondition) -> None:
        self._race = race
        self._height = height
        self._healthCondition = healthCondition
        Animal.__init__(self, ID, name, bornYear, disponibility, description)

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
    


Gato1 = Cat(1, "Paco", 1, True, "Gato1", "Persa", 15, True)
