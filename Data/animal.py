from datetime import date

class Animal:

    """ This is the superclass of Cat and Dog, it contains the common attributes of both classes, as well as it's getters and setters """

    def __init__(self,ID,name,bornYear,disponibility,description):
        self._name = name
        self._bornYear = bornYear
        self._disponibility = disponibility
        self._description = description
        self._ID = ID


    """ Getters and setters for Animal """

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

# Class method to see the age instead of the bornyear of determinated animal
    def age(self):
        return date.today().year-self._bornYear
    
