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
            return Cat(int(record[0]), record[2], int(record[3]), record[4]=="True", record[5], record[6],int(record[7]),record[8]=="True")
        if record[1] == 'Dog':
            """formato[id,class,name,bornyear,disponibility,description,race,height,healthcondition]"""
            return Dog(int(record[0]), record[2], int(record[3]), record[4]=="True", record[5], record[6],int(record[7]),record[8]=="True")
       
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
    base1.append("")
    ID,bornYear,height = i,i,i
    
    race = "Raza"+str(i)
    description = "Es un gato muy lindo "+str(i)
    if i%2==0:
        name = "Gato"+str(i)
        disponibility = True
        healthCondition = False
        base1[i-1]=[str(ID),"Cat",name,str(bornYear),str(disponibility),description,race,str(height),str(healthCondition)]

    else:
        name = "Perro"+str(i)
        disponibility = False
        healthCondition = True
        base1[i-1]=[str(ID),"Cat",name,str(bornYear),str(disponibility),description,race,str(height),str(healthCondition)]

with open("base1.csv","w") as file:
    for e in base1:
        file.write(str(e[0])+","+str(e[1])+","+str(e[2])+","+str(e[3])+","+str(e[4])+","+str(e[5])+","+str(e[6])+","+str(e[7])+","+str(e[8])+"\n") 





intentobase1 = Manager("base1.csv")
intentobase1.createLists()
for animal in intentobase1._disponibleAnimals:
    print(animal.name)
