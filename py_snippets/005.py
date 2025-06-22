
class O:
    def __init__(self, txt="O says hello"):
        print("O")
        self.txt = txt

class D(O):
    def __init__(self, txt="hello"):
        print("D")
        super().__init__(txt)
        print("D2")

        #self.txt = "D says bye"

class E(O):
    def __init__(self, txt="hello"):
        print("E")
        super().__init__(txt)
        print("E2")

        #self.txt = "E says bye"

class F(O):
    def __init__(self, txt="hello"):
        print("F")
        super().__init__(txt)
        print("F2")

        #self.txt = "F says bye"

class B(D, E):
    def __init__(self, txt="hello"):
        print("B")
        super().__init__(txt)
        print("B2")

        #self.txt = "B says bye"

class C(D, F):
    def __init__(self, txt="hello"):
        print("C")
        super().__init__(txt)
        print("C2")

        #self.txt = "C says bye"

class A(B, C):
    def __init__(self, txt="hello"):
        print("A")
        super().__init__(txt)
        print("A2")

        #self.txt = "A says bye"


obj = A()
print("")
for i in A.mro():
    print(i)
print(f"\n{obj.txt}")
