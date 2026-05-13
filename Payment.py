from abc import ABC,abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay():
        pass

class UPI(Payment):
    def pay(self):
        print("Payment done by UPI")
class CC(Payment):
    def pay(self):
        print("Payment done by Credit Card")
class DC(Payment):
    def pay(self):
        print("Payment done by Debit Card")

if __name__ == "__main__":
    u = UPI()
    u.pay()