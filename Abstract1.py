class Meal:
    def __cookRajma(self):
        print("Rajma Prepared")
    def __cookRumaliRoti(self):
        print("Roomali Roti Prepared")
    def __prepraesalad(self):
        print("Salaad prepared")
    def __cookrice(self):
        print("Rice Prepared...")
    def __sweet(self):
        print("Sweet prepared..")

    def cookmeal(self):
        self.__cookRajma()
        self.__cookRumaliRoti()
        self.__prepraesalad()
        self.__cookrice()
        self.__sweet()

if __name__ == "__main__":
    m = Meal()
    m.cookmeal()    