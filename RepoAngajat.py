from load import *

class RepoAngajati:
    def __init__(self):
        result = loadAngajati()
        result2 = loadTaskuri()
        self.__angajati=detAngajati(result)
        self.__taskuri=detTaskuri(result2)
        results = loadPrezenta()
        self.__prezenta = detPrezenta(results)

    def reloadAngajati(self):
        result=loadAngajati()
        self.__angajati = detAngajati(result)

    def reloadTaskuri(self):
        result2 = loadTaskuri()
        self.__taskuri = detTaskuri(result2)

    def reloadPrezenta(self):
        results = loadPrezenta()
        self.__prezenta = detPrezenta(results)

    def getPrezenta(self):
        return self.__prezenta

    def getAngajati(self):
        return self.__angajati
    def getTaskuri(self):
        return self.__taskuri

    def completareTask(self,idTask):
        # se stabileste conexiunea cu baza de date
        conn = psycopg2.connect(
            database="firma", user='bogdan', password='bogdan1234', host='localhost', port='5432'
        )
        # Setting auto commit false
        conn.autocommit = True
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        sql="""UPDATE TASK SET completat=true where id=%s"""
        cursor.execute(sql,(idTask,))
        # Commit your changes in the database
        conn.commit()
        # Closing the connection
        conn.close()


