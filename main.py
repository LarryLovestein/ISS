from tkinter import *
from functools import partial
from datetime import datetime
from ControlerAngajat import *

from ControlerSef import *
from ControlerAngajat import *

ctrlSef=ControlerSef()


def validateLogin(username, password):
    sefi=ctrlSef.getSefi()
    angajati=ctrlSef.getRepo().getAngajati()

    for i in angajati:
        if username.get()==i.getUsername() and password.get()==i.getPassword():
            print("username entered :", username.get())
            print("password entered :", password.get())
            print(i.getId())
            prezenta(i.getId())
    for i in sefi:
        if i.getUsername() == username.get() and password.get()==i.getPassword():
            vizualAngajati()
            break

from tkinter import ttk

def istoricAng(nume):
    istoric = Tk()
    istoric.resizable(width = 1, height = 1)
    istoric.title('Vizualizare Istoric Angajati')
    treev = ttk.Treeview(istoric, selectmode='browse')
    treev.pack(side='right')
    verscrlbar = ttk.Scrollbar(istoric,
                               orient="vertical",
                               command=treev.yview)
    verscrlbar.pack(side ='right', fill ='x')
    treev.configure(xscrollcommand=verscrlbar.set)
    treev["columns"] = ("1", "2", "3","4","5")
    treev['show'] = 'headings'
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=90, anchor='c')
    treev.column("2", width=90, anchor='se')
    treev.column("3", width=90, anchor='se')
    treev.column("4", width=90, anchor='se')
    treev.column("5", width=90, anchor='se')
    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="Nume")
    treev.heading("2", text="Prenume")
    treev.heading("3", text="Data")
    treev.heading("4", text="Ora Sosirii")
    treev.heading("5", text="Ora Plecarii")
    NUME,PRENUME=nume.split()
    angajat=ctrlSef.detAngajatId(NUME,PRENUME)
    for i in ctrlSef.getIstoricAngajat(angajat.getId()):
        if i.getPlecare()!=None:
            treev.insert("", 'end', text="L1",
                         values=(i.getNume(), i.getPrenume(), i.getSosire().date(),i.getSosire().strftime("%H:%M"),i.getPlecare().strftime("%H:%M")))





def istoricAngajati():
    istoric = Tk()
    istoric.resizable(width = 1, height = 1)
    istoric.title('Vizualizare Istoric Angajati')
    treev = ttk.Treeview(istoric, selectmode='browse')
    treev.pack(side='right')
    verscrlbar = ttk.Scrollbar(istoric,
                               orient="vertical",
                               command=treev.yview)
    verscrlbar.pack(side ='right', fill ='x')
    treev.configure(xscrollcommand=verscrlbar.set)
    treev["columns"] = ("1", "2", "3","4","5")
    treev['show'] = 'headings'
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=90, anchor='c')
    treev.column("2", width=90, anchor='se')
    treev.column("3", width=90, anchor='se')
    treev.column("4", width=90, anchor='se')
    treev.column("5", width=90, anchor='se')
    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="Nume")
    treev.heading("2", text="Prenume")
    treev.heading("3", text="Data")
    treev.heading("4", text="Ora Sosirii")
    treev.heading("5", text="Ora Plecarii")

    for i in ctrlSef.getRepo().getPrezenta():
        if i.getPlecare() != None:
            treev.insert("", 'end', text="L1",
                         values=(i.getNume(), i.getPrenume(), i.getSosire().date(),i.getSosire().strftime("%H:%M:%S"),i.getPlecare().strftime("%H:%M:%S")))


'''
    treev.insert("", 'end', text="L1",
                 values=("Alyosha", "Karamazov", "23.03.2021","08:00","16:00"))
    treev.insert("", 'end', text="L1",
                 values=("Alyosha", "Karamazov", "23.03.2021","08:00","16:00"))'''

def vizualAngajati():
    #tkWindow.destroy()
    visualTask = Tk()
    visualTask.geometry('600x700')
    visualTask.title('Vizualizare Angajati')
    lbl = Label(visualTask, text="Lista angajati prezenti")
    listbox = Listbox(visualTask)
    listbox.config(width=20, height=20)
    ctrlSef.getRepo().reloadAngajati()
    for i in ctrlSef.getAngajatiPrezenti():
        listbox.insert(i.getId(),str(i.getNume())+" "+str(i.getPrenume()))
    btnTsk = Button(visualTask, text="Trimite task",command=lambda listbox=listbox: trimiteTask(listbox.get(ANCHOR)))
    btnIst = Button(visualTask, text="Istoric Angajat", command=lambda listbox=listbox: istoricAng(listbox.get(ANCHOR)))
    btnIstAng = Button(visualTask, text="Istoric Angajati", command=lambda listbox=listbox: istoricAngajati())
    lbl.pack()
    listbox.pack()
    btnTsk.pack()
    btnIst.pack()
    btnIstAng.pack()


''' listbox.insert(1, "Ionica Amariei")
    listbox.insert(2, "Bogdan Horeanga")
    listbox.insert(3, "Raskolnikov")
    listbox.insert(4, "Alyosha")'''



def trimiteTask(task):
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
    

def sendTask(id, titlu, details,trTask):
    ctrlSef.trimiteTask(titlu.get(), details.get(), id)
    trTask.destroy()




def prezenta(idAngajat):
    # Toplevel object which will
    # be treated as a new window
    prezenta1 = Toplevel(tkWindow)

    # sets the title of the
    # Toplevel widget
    prezenta1.title("prezenta")

    # sets the geometry of toplevel
    prezenta1.geometry("350x120")

    # A Label widget to show in toplevel
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    dataLabel=Label(prezenta1,text="Ora si data:", font=("arial",16)).grid(row=0,column=0)
    dataLabel=Label(prezenta1,text=dt_string,font=("arial",16)).grid(row=0,column=1)
    confButton = Button(prezenta1, text="Confirmare", command=lambda: vizualTask(dt_string,idAngajat,prezenta1), font=("Arial", 16)).grid(row=4, column=1)
def plecare(idAngajat,visualTask):
    # Toplevel object which will
    # be treated as a new window
    plecare1 = Toplevel(tkWindow)

    # sets the title of the
    # Toplevel widget
    plecare1.title("plecare")

    # sets the geometry of toplevel
    plecare1.geometry("350x120")

    # A Label widget to show in toplevel
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    dataLabel = Label(plecare1 , text="Ora si data:", font=("arial", 16)).grid(row=0, column=0)
    dataLabel = Label(plecare1, text=dt_string, font=("arial", 16)).grid(row=0, column=1)
    confButton = Button(plecare1, text="Confirmare", command= lambda: destroyAll(idAngajat,plecare1,visualTask) ,
                        font=("Arial", 16)).grid(row=4, column=1)



def destroyAll(idAngajat,plecare1,visualTask):
    ctrlAng = ControlerAngajat(idAngajat)
    ctrlAng.setPlecare()
    plecare1.destroy()
    visualTask.destroy()

def vizualTask(dt_string,idAngajat,prezenta1):

    prezenta1.destroy()

    ctrlAngajat=ControlerAngajat(idAngajat)
    ctrlAngajat.setSosire(dt_string)

    visualTask = Tk()

    visualTask.geometry('600x700')
    visualTask.title('Vizualizare Task-uri')
    lbl = Label(visualTask, text="Lista task-uri")
    listbox = Listbox(visualTask)
    listbox.config(width=20, height=20)
    for i in ctrlAngajat.getTaskuriAngajat():
        listbox.insert(i.getId(),i.getTitlu())

    btn = Button(visualTask, text="Completare",font=("Arial", 16),command = lambda listbox=listbox: completareTask(listbox.get(ANCHOR),idAngajat,listbox))
    btnViz= Button(visualTask, text="Detalii",command=lambda listbox=listbox: taskDetaliat(listbox.get(ANCHOR),idAngajat))
    btnPlecare = Button(visualTask, text="Plecare", command=lambda: plecare(idAngajat,visualTask) )
    lbl.pack()
    listbox.pack()
    btn.pack()
    btnViz.pack()
    btnPlecare.pack()


def completareTask(task,idAngajat,listbox):
    ctrlAng=ControlerAngajat(idAngajat)
    sarcina=ctrlAng.getTaskTitlu(task)
    ctrlAng.setTaskCompletatat(sarcina.getId())
    listbox.delete(ANCHOR)



def taskDetaliat(task,idAngajat):
    taskDetal = Tk()
    print(task)
    taskDetal.geometry('300x300')
    ctrlAngajat=ControlerAngajat(idAngajat)

    taskDetal.title('Task detaliat:' +task)
    sarcina=ctrlAngajat.getTaskTitlu(task)
    detaliu=sarcina.getDetalii()
    T = Text(taskDetal, height=5, width=52)
    T.pack()
    T.insert(END, detaliu)

#window
tkWindow = Tk()
tkWindow.geometry('350x120')
tkWindow.title('Login Form')


#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name:",font=("Arial",16)).grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",font=("Arial",16)).grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin,font=("Arial",16)).grid(row=4, column=1)

tkWindow.mainloop()

