class BankAccount:
    interest_rate = float(2.5)
    accounts = []

    def __init__(self):
        self.balance = 0
    
    def deposit(self, number_to_add):
        self.balance += number_to_add

    def withdraw(self, number_to_subtract):
        self.balance -= number_to_subtract
    
    @classmethod
    def create(cls):
        new_account = BankAccount()
        cls.accounts.append(new_account)
        return new_account

    @classmethod
    def total_funds(cls):
        balances = 0
        for account in cls.accounts:
            balances += account.balance
        return balances

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += (account.balance * cls.interest_rate)

my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance)
print(BankAccount.total_funds())
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) 
print(your_account.balance) 
print(BankAccount.total_funds()) 
BankAccount.interest_time()
print(my_account.balance)
print(your_account.balance) 
print(BankAccount.total_funds()) 
my_account.withdraw(50)
print(my_account.balance)
print(BankAccount.total_funds())  