class Tata:
    def __init__(self):
        print("Tata groups has multiple sub companies")
class Tcs(Tata):
    def __init__(self):
        super().__init__()
        print("TCS belongs to tata groups")
class Zudio(Tata):
    def __init__(self):
        super().__init__()
        print("Zudio belongs to tata groups")
class indego(Tata):
    def __init__(self):
        super().__init__()
        print("Indego belongd to tata groups")

obj1 = Tcs()
obj2 = Zudio()
obj3 = indego()
