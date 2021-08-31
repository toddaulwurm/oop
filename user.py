class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -= amount
    def display_balance(self):
        print(self.balance)
    def transfer(self, amount):
        self.balance -= amount
        paul.balance += amount


todd = User("Todd", "toddaulwurm@yahoo.com")
nich = User("Nich", "nichaulwurm@yahoo.com")
paul = User("Paul", "paulaulwurm@yahoo.com")
print(todd.name)
print(todd.email)
todd.make_deposit(100)
todd.make_deposit(200)
todd.make_deposit(300)
todd.make_withdrawal(50)
todd.display_balance()

print(nich.name)
print(nich.email)
nich.make_deposit(20)
nich.make_deposit(200)
nich.make_withdrawal(3)
nich.make_withdrawal(100)
nich.display_balance()

print(paul.name)
print(paul.email)
paul.make_deposit(1000)
paul.make_withdrawal(400)
paul.make_withdrawal(400)
paul.make_withdrawal(400)
paul.display_balance()

nich.transfer(200)
print(nich.name)
nich.display_balance()
print(paul.name)
paul.display_balance()

