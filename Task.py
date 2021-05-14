from Angajat import *

class Task:
    def __init__(self,id,titlu,detalii,angajat,completat):
        self.__id=id
        self.__titlu = titlu
        self.__detalii = detalii
        self.__angajat = angajat
        self.__completat = completat

    def getTitlu(self):
        return self.__titlu
    def getDetalii(self):
        return self.__detalii
    def getAngajat(self):
        return self.__angajat
    def getCompletat(self):
        return self.__completat
    def getId(self):
        return self.__id

    def setTitlu(self,titlu):
        self.__titlu=titlu
    def setDetalii(self,detalii):
        self.__detalii=detalii
    def setAngajat(self,angajat):
        self.__angajat=angajat
    def setCompletat(self,completat):
        self.__completat=completat

    def __str__(self):
        return f"Titlu task:{self.__titlu}, descriere:{self.__detalii}, angajat:{self.__angajat}, completat:{self.__completat}"
