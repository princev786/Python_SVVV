class Bank:
    accno = 0
    name = ""

    def __init__(self,accno,name):
        self.accno = accno
        self.name = name
        

    def show(self):
        print("AccNo",self.accno)
        print("Name ",self.name)

b = Bank(599800,"Prince Soni")
b2 = Bank(500800,"Aditya Soni")
print(b.name)
b.show()
b2.show()
