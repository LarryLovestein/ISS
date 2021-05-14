from RepoAngajat import *

class ControlerAngajat:
    def __init__(self,id):
        self.__repo=RepoAngajati()
        self.__id=id
    def getRepo(self):
        return self.__repo
    def getId(self):
        return self.__id

    def getAngajat(self):
        ang=self.__repo.getAngajati()
        for i in ang:
            if i.getId()==self.__id:
                return i
    def getTaskuriAngajat(self):
        taskuri=self.__repo.getTaskuri()
        tasks=list()
        for i in taskuri:
            if i.getAngajat()==self.__id and i.getCompletat()==False:
                tasks.append(i)
        return tasks
    def getTaskTitlu(self,titlu):
        taskuri = self.getTaskuriAngajat()
        for i in taskuri:
            if i.getTitlu()==titlu and i.getCompletat()==False:
                return i


    def getTaskuriCompleteAngajat(self):
        taskuri=self.__repo.getTaskuri()
        tasks=list()
        for i in taskuri:
            if i.getAngajat()==self.__id and i.getCompletat()==True:
                tasks.append(i)
        return tasks
    def setTaskCompletatat(self,idTask):
        self.__repo.completareTask(idTask)
    def setSosire(self,data):
        #now = datetime.now()
        #dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        declararePrezenta(self.__id,data)

    def setPlecare(self):
        now = datetime.now()
        dat=date.today()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        for i in self.__repo.getPrezenta():
            if i.getSosire().date() == dat and i.getPlecare()==None:
                idPrez=i.getId()
                break
        declPlecare(idPrez,dt_string)




