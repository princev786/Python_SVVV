class TravelAgencies:
    __regno =0
    __agencyname=""
    __packagetype=""
    __price=0
    __flightfacility=False

    def __init__(self,regno,agencyname,packagetype,price,flightfacility):
        self.__regno = regno
        self.__agencyname = agencyname
        self.__packagetype = packagetype
        self.__price = price
        self.__flightfacility = flightfacility
        

    def getregno(self):
        return self.__regno
    def setregno(self,regno):
        self.__regno = regno
    def getagencyname(self):
        return self.__agencyname
    def setagencyname(self,agencyname):
        self.__agencyname = agencyname
    def getpackagetype(self):
        return self.__packagetype
    def setpackagetype(self,packagetype):
        self.__packagetype = packagetype
    def getprice(self):
        return self.__price
    def setprice(self,price):
        self.__price = price
    def getflightfacility(self):
        return self.__flightfacility
    def setflightfacility(self,flightfacility):
        self.__flightfacility = flightfacility

class Solution:
    @staticmethod
    def findAgencyWithHighestPackagePrice(lst):
        max = 0
        for agency in lst:
            if agency.getprice()>max:
                max = agency.getprice()
        
        return max
    
    @staticmethod
    def agencyDetailsForGivenldAndType(lst,regno,packagetype):
        for agency in lst:
            if agency.getflightfacility() and agency.getregno() == regno and agency.getpackagetype() == packagetype:
                return agency
        return None
    

if __name__ == "__main__":
    n = int(input())
    lst=[]
    for i in range(n):
        regno= int(input())
        agencyname= input()
        packagetype= input()
        price= int(input())
        flightfacility= bool(input())

        agency = TravelAgencies(regno,agencyname,packagetype,price,flightfacility)
        lst.append(agency)

    regno = int(input())
    packagetype = input()

    print("-------------------------------\nOutput\n-------------------------------")
    max = Solution.findAgencyWithHighestPackagePrice(lst)
    agency = Solution.agencyDetailsForGivenldAndType(lst,regno,packagetype)

    print(max)
    print(agency.getagencyname(),":",agency.getprice())


    