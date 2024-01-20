class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit Complete.")
        self.get_balance()
        
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdrawl complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdrawl interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print("\n*****************\n\nBeginning Transfer...🚀")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete!\n\n***************")
        except BalanceException as error:
            print(f"\nTransfer interrupted: {error}")

class InterestRewards(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()
        
class SavingsAcct(InterestRewards):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")