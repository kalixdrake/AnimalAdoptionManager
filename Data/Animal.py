class Animal:
    """ Getters and setters for the  general attributes and deleter for the disponibility attribute because
    it is the only one that can be modificated. """
    def __init__(self) -> None:
        self._name = ""
        self._age = 0
        self._species = 0
        self._disponibility = True
        self._description = ""
        pass

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age


    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, species):
        self._species = species


    @property
    def disponibility(self):
        return self._disponibility

    @disponibility.setter
    def disponibility(self, disponibility):
        self._disponibility = disponibility
    
    @disponibility.deleter
    def disponibility(self):
        del self._disponibility

    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description


class Cat:
    """ Getters and setters for Cat """
    def __init_subclass__(Animal) -> None:
        Animal._race = 0
        Animal._height = 0
        Animal._healthCondition = True
        pass

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        self._race = race
    

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


class Dog:
    def __init_subclass__(Animal) -> None:
        Animal._race = 0
        Animal._Height = 0
        Animal._healthCondition = True
        pass

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        self._race = race
    

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