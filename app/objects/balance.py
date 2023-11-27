class Balance:
    def __init__(self, balance):
        self.balance = balance
    
    def __str__(self):
        return f"{self.balance}"
    
    def getBlanace(self):
        return self.balance
    
    def increaseBalance(self, incrementValue):
        self.balance += incrementValue
    
    def decreaseBalance(self, decrementValue):
        self.balance -= decrementValue

    