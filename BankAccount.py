class BankAccount:
    def __init__(self, name, email, balance, int_rate):
        self.name = name
        self.email = email
        self.balance = 0
        self.int_rate = 0.01
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else: 
            print("Insufficient Funds: Charging a $5 Fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if BankAccount.is_pos(self.balance):
            self.balance= (self.balance*self.int_rate)+self.balance
        else:
            print("Not interested")
        return self
    def identity(self):
        print(self.name)
        print(self.email)
        return self
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    @staticmethod
    def is_pos(balance):
        if balance < 0:
            return False
        else:
            return True
    # @classmethod
    # def account_record(balance):
    #     print(balance)

todd = BankAccount("Todd", "toddaulwurm@yahoo.com", 500, 0.01)
nich = BankAccount("Nich", "nichaulwurm@yahoo.com", 500, 0.01)

todd.identity().deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()

nich.identity().deposit(20).deposit(200).withdraw(3).withdraw(100).withdraw(20).withdraw(5).yield_interest().display_account_info()


