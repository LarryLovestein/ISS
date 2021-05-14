
class Prezenta:
    def __init__(self,id,nume,prenume,sosire,plecare):
        self.__id=id
        self.__nume=nume
        self.__prenume=prenume
        self.__sosire=sosire
        self.__plecare=plecare

    def __str__(self):

        return f"{self.__nume},{self.__prenume}, SOSIRE: {self.__sosire} PLECARE: {self.__plecare}"

    def getId(self):
        return self.__id
    def getAngajat(self):
        return self.__angajat
    def getSosire(self):
        return self.__sosire
    def getPlecare(self):
        return self.__plecare
    def getNume(self):
        return self.__nume
    def getPrenume(self):
        return self.__prenume
    def setId(self,id):
        self.__id=id

    def setAngajat(self,angajat):
        self.__angajat=angajat

    def setSosire(self,sosire):
        self.__sosire=sosire

    def setPlecare(self,plecare):
        self.__plecare=plecare
