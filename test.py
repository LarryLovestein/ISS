from tkinter import *
from ControlerSef import *
ctrlSef=ControlerSef()
task="Horeanga Bogdan"
def sper(task):
    def sendTask(id, titlu, details,trTask):
        ctrlSef.trimiteTask(titlu.get(), details.get(), id)
        trTask.destroy()


    trTask = Tk()
    trTask.geometry('300x300')
    trTask.title('Task pentru: ' +task)
    NUME, PRENUME = task.split()
    angajat = ctrlSef.detAngajatId(NUME, PRENUME)
    titlu = StringVar()
    details = StringVar()
    titluLabel = Label(trTask, text="Titlu Task").grid(column=0,row=0)
    titluEntry = Entry(trTask, textvariable=titlu).grid(row=0, column=1)
    detailsLabel = Label(trTask, text="Details").grid(column=0, row=1)
    detailsEntry = Entry(trTask, textvariable=details).grid(row=1, column=1)
    btnTsk = Button(trTask, text="Trimite task",command=lambda titlu=titlu: sendTask(angajat.getId(),titlu,details,trTask),font=("Arial",16)).grid(row=4, column=1)

    trTask.mainloop()

sper(task)