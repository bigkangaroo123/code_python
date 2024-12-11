class Bankaccount:
    def __init__(self, acc_holder):
        self.__accholder = acc_holder
        self.__balance = 0
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def accholder(self):
        return self.__accholder
    
    def add_amount(self, value):
        self.__balance += value
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Can't withdraw more money than the bank balance")
        else:
            self.__balance -= amount
    
    def __repr__(self):
        return f"Account Holder: {self.accholder}, Balance: {self.balance}"
        
    @balance.setter
    def balance(self, random_val):
        self.__balance = random_val
    
b1 = Bankaccount("John Doe")
b1.add_amount(1500)
print(repr(b1))
b1.add_amount(2000)
print(repr(b1))
b1.withdraw(2000)
print(repr(b1))
b1.balance = 6900
print(repr(b1))
