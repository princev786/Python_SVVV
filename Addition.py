class A:
    def start(self):
        print("A started....")

class B(A):
    def start(self):
        super().start()
        print("B started....")

if __name__ == "__main__":
    b = B()
    b.start()
