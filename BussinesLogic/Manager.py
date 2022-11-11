from Data.Cat import Cat
from Data.Dog import Dog

class Manager:
    def __init__(self,animalData) -> None:
        self._animalData = animalData
        self._animals=[]
        self._disponibleAnimals=[]
        self._nonDisponibleAnimals=[]

    def createLists(self):
        self.CreateAnimals()
        for animal in self._animals:
            if animal.disponibility==True:
                self._disponibleAnimals.append(animal)
            else:
                self._nonDisponibleAnimals.append(animal)
        
    def createAnimal(self, record):
        record = list(map(lambda x: x.strip(), record))
        if record[1] == 'Cat':
            """formato[id,class,name,bornyear,disponibility,description,race,height,healthcondition]"""
            return Cat(record[0], float(record[2]), float(record[3]), record[4], record[5], record[6],record[7],record[8])
        if record[1] == 'Dog':
            """formato[id,class,name,bornyear,disponibility,description,race,height,healthcondition]"""
            return Dog(record[0], float(record[2]), float(record[3]), record[4], record[5], record[6],record[7],record[8])
       
    def CreateAnimals(self):
        with open(self._animalData, 'r') as info:
            for line in info:
                self._animals.append(self.createAnimal(line.split(",")))
    
    def maxID(self):
        listID = list(map(lambda x: x.ID, self._animals))
        return max(listID)

    def newAnimal(self,clase,name,bornyear,disponibility,description,race,height,healthcondition):      
        animal=[(self.maxID())+1,clase,name,bornyear,disponibility,description,race,height,healthcondition]
        self._animals.append(self.createAnimal(animal))
        
base1 = []
for i in range(1,100):
    ID,bornYear,height = i,i,i
    name = "Gato"+str(i)
    if i%2==0:
        disponibility = True
    else:
        disponibility = False
    description = "Es un gato muy lindo "+str(i)
    race = "Raza"+str(i)
    if i%2==0:
        healthCondition = False
    else:
        disponibility = True
    if i%2==0:
        base1.append(Dog(ID,name,bornYear,disponibility,description,race,height,healthCondition))
    else:
        base1.append(Cat(ID,name,bornYear,disponibility,description,race,height,healthCondition))


with open("base1.csv","w") as file:
        file.write(base1)

intentobase1 = Manager("base1.csv")
intentobase1.CreateAnimals()
intentobase1.createLists()

print(intentobase1._disponibleAnimals)