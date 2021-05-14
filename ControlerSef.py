from RepoAngajat import *

class ControlerSef:
    def __init__(self):
        self.__repo=RepoAngajati()
        results=loadSef()
        self.__sefi=detSef(results)

    def getRepo(self):
        return self.__repo

    def getId(self):
        return self.__id
    def getSefi(self):
        return self.__sefi
    def getAngajatiPrezenti(self):
        data=date.today()

        prezenti=list()
        prezenta=self.__repo.getPrezenta()
        for i in prezenta:
            if i.getPlecare() == None and i.getSosire().date()==data:
                prezenti.append(i)
        return prezenti
    def getIstoricAngajat(self,idAngajat):
        prezenti=list()
        prezenta=self.__repo.getPrezenta()
        for i in prezenta:
            if i.getId()==idAngajat:
                prezenti.append(i)
        return prezenti

    def trimiteTask(self,titlu,detalii,idAngajat):
        # se stabileste conexiunea cu baza de date
        conn = psycopg2.connect(
            database="firma", user='bogdan', password='bogdan1234', host='localhost', port='5432'
        )
        # Setting auto commit false
        conn.autocommit = True
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        sql='''INSERT INTO TASK(titlu,detalii,angajat_id,completat) VALUES (%s,%s,%s,FALSE )'''
        cursor.execute(sql,(titlu,detalii,idAngajat))
        # Commit your changes in the database
        conn.commit()
        # Closing the connection
        conn.close()
        #loadTaskuri()

    def detAngajatId(self,nume,prenume):
        for i in self.__repo.getAngajati():
            if i.getNume()==nume and i.getPrenume()==prenume:
                return i
ctrl=ControlerSef()

