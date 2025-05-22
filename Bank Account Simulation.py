class Bank_Account:
    def __init__(self,owner,balance=0.0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f'Deposited {amount}')
        else:
            print('Deposit amount must be positive')

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawn {amount}')
        else:
            print('Insufficient balance or the amount is invalid')

    def balance_inquiry(self):
        print(f'{self.owner} has Current Balance : {self.balance}')

account = Bank_Account('Eve',1000.0)

account.balance_inquiry()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.balance_inquiry()
            
