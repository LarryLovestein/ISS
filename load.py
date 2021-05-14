import psycopg2
from Angajat import *
from Sef import *
from Task import *
from Prezenta import *
from datetime import *
def loadAngajati():
    #se stabileste conexiunea cu baza de date
    conn = psycopg2.connect(
       database="firma", user='bogdan', password='bogdan1234', host='localhost', port= '5432'
    )
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Retrieving data
    cursor.execute('''SELECT * from angajat''')
    #Fetching 1st row from the table
    result = cursor.fetchall();
    #Commit your changes in the database
    conn.commit()
    #Closing the connection
    conn.close()
    return result

def loadTaskuri():
    #se stabileste conexiunea cu baza de date
    conn = psycopg2.connect(
       database="firma", user='bogdan', password='bogdan1234', host='localhost', port= '5432'
    )
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Retrieving data
    cursor.execute('''SELECT * from task''')
    #Fetching 1st row from the table
    result = cursor.fetchall();
    #Commit your changes in the database
    conn.commit()
    #Closing the connection
    conn.close()
    return result
def loadPrezenta():
    #se stabileste conexiunea cu baza de date
    conn = psycopg2.connect(
       database="firma", user='bogdan', password='bogdan1234', host='localhost', port= '5432'
    )
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Retrieving data
    cursor.execute('''SELECT angajat_id,nume,prenume, p.Sosire as Sosire, p.Plecare as Plecare from angajat INNER JOIN prezente p on angajat.id = p.angajat_id''')
    #Fetching 1st row from the table
    result = cursor.fetchall();
    #Commit your changes in the database
    conn.commit()
    #Closing the connection
    conn.close()
    return result


def loadSef():
    #se stabileste conexiunea cu baza de date
    conn = psycopg2.connect(
       database="firma", user='bogdan', password='bogdan1234', host='localhost', port= '5432'
    )
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Retrieving data
    cursor.execute('''SELECT * from sef''')
    #Fetching 1st row from the table
    result = cursor.fetchall();
    #Commit your changes in the database
    conn.commit()
    #Closing the connection
    conn.close()
    return result


def declararePrezenta(id,prez):
    # se stabileste conexiunea cu baza de date
    conn = psycopg2.connect(
        database="firma", user='bogdan', password='bogdan1234', host='localhost', port='5432'
    )
    # Setting auto commit false
    conn.autocommit = True
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    sql = '''INSERT INTO prezente(angajat_id,sosire) VALUES (%s,%s)'''
    cursor.execute(sql, (id,prez))
    conn.commit()
    # Closing the connection
    conn.close()
    # loadTaskuri()

def declPlecare(id,plec):
    # se stabileste conexiunea cu baza de date
    conn = psycopg2.connect(
        database="firma", user='bogdan', password='bogdan1234', host='localhost', port='5432'
    )
    # Setting auto commit false
    conn.autocommit = True
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    sql = '''UPDATE prezente set plecare=%s where angajat_id= %s and plecare is NULL'''
    cursor.execute(sql, (plec,id))
    conn.commit()
    # Closing the connection
    conn.close()
    # loadTaskuri()


def detSef(results):
    listSef=list()
    for i in results:
        sef=Sef(i[0],i[1],i[2])
        listSef.append(sef)
    return listSef


def detPrezenta(results):
    listaPrezente=list()
    for i in results:
        prez = Prezenta(i[0],i[1],i[2],i[3],i[4])
        listaPrezente.append(prez)
    return listaPrezente

def detTaskuri(result):
    listaAngajati = list()
    for i in result:
        task = Task(i[0],i[1],i[2],i[3],i[4])
        listaAngajati.append(task)
    return listaAngajati


def detAngajati(result):
    listaAngajati=list()
    for i in result:
        ang=Angajat(i[0],i[1],i[2],i[3],i[4])
        listaAngajati.append(ang)
    return listaAngajati

