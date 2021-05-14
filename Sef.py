class Sef:
    def __init__(self,id,username,password):
        self.__id=id
        self.__username=username
        self.__password=password
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getId(self):
        return self.__id
    def __str__(self):
        return f"Username:{self.__username}"

