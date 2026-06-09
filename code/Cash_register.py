class CashRegister:
    def __init__(self):
        self.money = 100

    def add_money(self,payment):
        self.money += payment

    def subtract_money(self,payment):
        self.money -= payment
