class Phone:
    __phoneid = 0
    __os=""
    __brand =""
    __price = 0

    def __init__(self,phoneid,os,brand,price):
        self.__phoneid = phoneid
        self.__os = os
        self.__brand = brand
        self.__price = price

    def getphoneid(self):
        return self.__phoneid
    def setphoneid(self,phoneid):
        self.__phoneid = phoneid
    def getos(self):
        return self.__os
    def setos(self,os):
        self.__os = os
    def getbrand(self):
        return self.__brand
    def setbrand(self,brand):
        self.__brand =brand
    def getprice(self):
        return self.__price
    def setprice(self,price):
        self.__price =price

class Solution:
    @staticmethod
    def findPriceForGivenBrand(lst,brand):
        sum = 0
        for phone in lst:
            if phone.getbrand() == brand :
                sum += brand.getprice()
        return sum
    @staticmethod
    def getPhoneIdBasedOnOs(lst,os):
        for phone in lst:
            if phone.getos()==os and phone.getprice()>=50000:
                return phone
        return None
    
if __name__ == "__main__":
    n = int(input())
    lst=[]
    for i in range(n):
        phoneid = int(input())
        os = input()
        brand=input()
        price = int(input())

        p = Phone(phoneid,os,brand,price)
        lst.append(p)
    brand = input()
    os = input()

    sum = Solution.findPriceForGivenBrand(lst,brand)
    phone = Solution.getPhoneIdBasedOnOs(lst,os)

    if sum>0:
        print(sum)
    else:
        print("The Given Brand is not Available")
    if phone!=None:
        print(phone.getphoneid())
    else:
        print("No phones are available with specified os and price range")