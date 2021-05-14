class Angajat:
    def __init__(self,id,username,password,nume,prenume):
        self.__id=id
        self.__username=username
        self.__password=password
        self.__nume=nume
        self.__prenume=prenume
    def getUsername(self):
        return self.__username
    def getNume(self):
        return self.__nume
    def getPrenume(self):
        return self.__prenume
    def getPassword(self):
        return self.__password
    def getId(self):
        return self.__id
    def __str__(self):
        return f"Nume: {self.__nume},Prenume: {self.__prenume},username: {self.__username}"

