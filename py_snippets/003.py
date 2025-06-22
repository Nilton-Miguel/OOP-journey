
class O:
    def __init__(self):
        print("O")

class D(O):
    def __init__(self):
        print("D")
        super().__init__()
        print("D2")

class E(O):
    def __init__(self):
        print("E")
        super().__init__()
        print("E2")

class F(O):
    def __init__(self):
        print("F")
        super().__init__()
        print("F2")

class B(D, E):
    def __init__(self):
        print("B")
        super().__init__()
        print("B2")

class C(D, F):
    def __init__(self):
        print("C")
        super().__init__()
        print("C2")

class A(B, C):
    def __init__(self):
        print("A")
        super().__init__()
        print("A2")

obj = A()
print("")
for i in A.mro():
    print(i)
