import random

class Staff:
    def __init__(self):
        self.staff_members = {
            'Rodrigo': {'senha': 123, 'vendas': 0, 'bonus': 0},
            'Mariana': {'senha': 456, 'vendas': 0, 'bonus': 0},
            'Samara': {'senha': 789, 'vendas': 0, 'bonus': 0},
        }

    @staticmethod
    def staff_workin(staff_members):
        chosen_member = random.choice(staff_members)

    def staff_sales(self,chosen_member,product_price):
        chosen_member['vendas'] += product_price
        chosen_member['bonus'] += (product_price * 0.10)

