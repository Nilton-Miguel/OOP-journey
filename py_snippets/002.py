
class Base:
    def __init__(self):
        print("Base")

class ChildA(Base):
    def __init__(self):
        print("ChildA")
        super().__init__()
        print("ChildA2")

class ChildB(Base):
    def __init__(self):

        print("ChildB")
        super().__init__()
        print("ChildB2")

class User(ChildA, ChildB):
    def __init__(self):
        print("User")
        super().__init__()
        print("User2")

obj = User()

print("")
for i in User.mro():
    print(i)
