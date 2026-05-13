from abc import ABC,abstractmethod
class Animal(ABC):
     def sound(self):
        print("Gutur Gu...Gutur Gu from Animal")

class Bird(ABC):
    def sound():
        print("Koo....Koo... from Bird")

    @abstractmethod
    def fly():
        pass

class Pigeon(Animal,Bird):
   
    def fly(self):
        print("Flying....")

p = Pigeon()
p.sound()
p.fly()

