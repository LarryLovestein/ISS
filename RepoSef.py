from RepoAngajat import *
class RepoSef(RepoAngajati):
    def __init__(self):
        super(RepoSef, self).__init__()
        results= loadPrezenta()
        self.__prezenta= detPrezenta(results)

    def getPrezenta(self):
        return self.__prezenta

