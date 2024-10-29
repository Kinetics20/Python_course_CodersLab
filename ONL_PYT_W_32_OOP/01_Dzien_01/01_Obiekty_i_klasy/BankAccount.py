class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def print_info(self):
        print(f'Numer konta: {self.number}, stan: {self.cash} PLN')

    def deposit_cash(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            return
        self.cash += amount

    def withdraw_cash(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            return
        if amount > self.cash:
            amount = self.cash
        self.cash -= amount
        return amount


account = BankAccount('145856231545623')
account.print_info()
account.deposit_cash(100)
account.print_info()
account.deposit_cash(1000)
account.print_info()
print('Próbuję wypłacić 700zł, wypłacam:', account.withdraw_cash(700))
account.print_info()
print('Próbuję wypłacić 600zł, wypłacam:', account.withdraw_cash(600))
account.print_info()