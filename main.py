global a
global b


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,a=0):
        a=int(input("Скіки на карточку закинути?"))
        self.balance += a
    def withdraw(self,b=0):
        b=int(input('Скіки зняти з карточки?'))
        if b<=a:
            balance=b-a
            print('Тепер в тебе на карточці ', balance, 'грн')
        else:
            print('Недостатньо коштів')

anton=BankAccount('123123', 0)

anton.deposit(200)
anton.withdraw(100)
anton.withdraw(200)














