class Bank:
    __accno =0 #private variable
    __name=""
    __balance=0

    def __init__(self,accno,name,bal):
        self.__accno = accno     
        self.__name = name     
        self.__balance = bal     

    def getaccno(self):
        return self.__accno
    def setaccno(self,accno):
        self.__accno = accno
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name
    def getbalance(self):
        return self.__balance
    def setbalance(self,balance):
        self.__balance = balance


    
b = Bank(123,"Prince",1000)
print(b._Bank__accno)

