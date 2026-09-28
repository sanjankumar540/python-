"""from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sample(self):
        pass
    
class dog(Animal):
    def sound(self):
        print("dog barks")
obj = dog()
obj.sample() """


from abc import ABC , abstractmethod
class RBI(ABC):
    @abstractmethod
    def loan(self):
        pass
    @abstractmethod
    def ATM(self):
        pass
    @abstractmethod
    def passbook(self):
        pass
    @abstractmethod
    def ac_no(self):
        pass
    @abstractmethod
    def ATM_card(self):
        pass
    def coffie(self):
        pass
    def snacks(self):
        pass   

class SBI(RBI):
    def loan(self):
        print("we provide loan with 5% interest")
    def ATM(self):
        print("only 500 and 200 notes are available")
    def passbook(self):
        print("passbook is neccessary while coming to bank")
    def ac_no(self):
        print("passbook is neccessary while coming to bank")
    def ATM_card(self):
        print("for the account holders above 18 years we provide debit card")

class Indian(RBI):
    def loan(self):
        print("we provide loan with 5% interest")
    def ATM(self):
        print("only 500 and 200 notes are available")
    def passbook(self):
        print("passbook is neccessary while coming to bank")
    def ac_no(self):
        print("passbook is neccessary while coming to bank")
    def ATM_card(self):
        print("for the account holders above 18 years we provide debit card")

class HDFC(RBI):
    def loan(self):
        print("we provide loan with 5% interest")
    def ATM(self):
        print("only 500 and 200 notes are available")
    def passbook(self):
        print("passbook is neccessary while coming to bank")
    def ac_no(self):
        print("passbook is neccessary while coming to bank")
    def ATM_card(self):
        print("for the account holders above 18 years we provide debit card")

obj1 = SBI()
obj1.ATM()
obj1.coffie()
obj1.ac_no()

obj2 = Indian()
obj2.ATM_card()
obj2.snacks()

obj3 = HDFC()
obj3.passbook() 



        
        
        
        
