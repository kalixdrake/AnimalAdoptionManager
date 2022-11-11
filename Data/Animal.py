from datetime import date
class Animal:

    """ Getters and setters for the  general attributes and deleter for the disponibility attribute because
    it is the only one that can be modificated. """

    def __init__(self,ID,name,bornYear,disponibility,description) -> None:
        self._name = name
        self._bornYear = bornYear
        self._disponibility = disponibility
        self._description = description
        self._ID = ID

    # Inicio de getters y setters
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        print("Name es un atributo de solo lectura")

    
    @property
    def bornYear(self):
        if self._bornYear>=0 and self._bornYear<=20:
            year = date.today().year-self._bornYear
            return year
        else:
            return self._bornYear

    @bornYear.setter
    def bornYear(self, bornYear):
        print("BornYear es un atributo de solo lectura")

    @property
    def disponibility(self):
        return self._disponibility

    @disponibility.setter
    def disponibility(self, disponibility):
        self._disponibility = disponibility
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def ID(self):
        return self._ID
    
    @ID.setter
    def ID(self, ID):
        print("ID es un atributo de solo lectura")
    # Fin de getters y setters
    
    # Inicio de metodos
    @property
    def age(self):
        return date.today().year-self._bornYear
    
