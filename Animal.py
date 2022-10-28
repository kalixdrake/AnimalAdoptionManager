class Animal:
    def __init__(self) -> None:

        pass


class Cat:
    def __init_subclass__(Animal) -> None:

        pass


class Dog:
    def __init_subclass__(Animal) -> None:
        
        pass