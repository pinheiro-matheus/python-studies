#school catalogue

class School:
    def __init__(self, name, level, numberOfStudents):
        self.__name = name
        self.__level = level 
        self.__numberOfStudents = numberOfStudents 

    def __repr__(self):
        return "This is {name} {level} School ans it`s has {numberOfStudents}".format(name = self.__name, level = self.__level, numberOfStudents = self.__numberOfStudents)

    def getName(self):
        return self.__name
    
    def getLevel(self):
        return self.__level
    def getNumberOfStudents(self):
        return self.__numberOfStudents
    
    def setName(self, name):
        self.__name = name
    def setLevel(self, level):
        self.__level = level
    def setNumberOfStudents(self, numberOfStudents):
        self.__numberOfStudents = numberOfStudents


class Primary(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy 

    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + " - pick up at 3 pm"
    
    def getpickupPolicy(self):
        return self.pickupPolicy
    
    def setpickupPolicy(self, pickupPolicy):
        self.pickupPolicy = pickupPolicy


class Middle(School):
    pass


class High(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "High", numberOfStudents)
        self.sportsTeam = sportsTeams
    def getSportsTeams(self):
        return self.sportsTeam
    def __repr__(self):
        parent_repr = super().__repr__()
        return parent_repr + self.sportsTeam

deels = School("del", "primary", 420 )
a = School("Codecademy", "high", 100)
b = Primary("dels", 420, " on")
c = High("dells", 420, str([" basket", "tennis"]))
print(c.getSportsTeams())
# print(a.getName())
# print(a.getLevel())
# a.setNumberOfStudents(200)
# print(a.getNumberOfStudents())
# print(b)

