class atm():
    def __init__(self, name, accountnumber):
        self.name = name
        self.accountnumber = accountnumber
        self.balance = 5000
    def display (self):
        print("name-", self.name)
        print("accountnumber-", self.accountnumber)
        print("balance-", str(self.balance))
    def withdraw(self, amount):
        self.balance = self.balance-amount 
tanish = atm("tanish", "xx1234")
tanish.display()
tanish.withdraw(3000)
tanish.display()