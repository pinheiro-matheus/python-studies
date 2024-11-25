class BankAccount:
  

    def __init__(self, name):
        self.name = name
        self.balance = 0
    def __repr__(self):
        return "Welcome to your account {}, your balance is $ {}: ".format(self.name, self.balance)
    def show_balance(self):
        print ("Your balacne is: "f"{self.balance: .2f}")
    def deposit(self, amount):
        self.amount = amount
        if amount <= 0:
            print("Negative amount not allowed")
            return self.balance
        else:
            print("you deposit $: {}".format(f"{amount: .2f}"))
            self.balance += amount
            self.show_balance()
            return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            print("The amount can`t be bigger than the balacne")
            return 
        else:
            print("You withdraw $: {}".format(f"{amount: .2f}"))
            self.balance -= amount
            self.show_balance()
            return self.balance
my_account = BankAccount("del")

print(my_account)
print(my_account.deposit(10000))
print(my_account.withdraw(1000))