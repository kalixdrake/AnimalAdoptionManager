from animal import Animal

class Dog(Animal):
    def __init__(self,ID,name,bornYear,disponibility,description,race,height,healthCondition):
        super().__init__(ID, name, bornYear, disponibility, description)
        self._race = race
        self._height = height
        self._healthCondition = healthCondition

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

        