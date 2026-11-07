class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"Рахунок {self.account_number} поповнено на {amount}. Новий баланс: {self.balance}")
        else:
            print("На карточку тре закинути к-сть грошей більше за 0")

    def withdraw(self, amount):

        if amount <= 0:
            print("З карточки тре знімати к-сть грошей більше за 0")
            return False

        if self.balance >= amount:
            self.balance -= amount
            print(f"З рахунку {self.account_number} знято {amount}. Залишок на рахунку: {self.balance}")
            return True
        else:
            print(
                f"Помилка: недостатньо коштів на рахунку {self.account_number}! Доступно: {self.balance}, а потрібно: {amount}")
            return False

















