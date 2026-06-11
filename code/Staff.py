import random

class Staff:
    def __init__(self):
        self.staff_members = {
            'Rodrigo': {'vendas': 0.0, 'bonus': 0},
            'Mariana': {'vendas': 0.0, 'bonus': 0},
            'Samara': {'vendas': 0.0, 'bonus': 0},
        }


    def staff_working(self):
        staff =  []
        for k in self.staff_members:
            staff.append(k)
        chosen_worker = random.choice(staff)
        return chosen_worker


    def staff_sales(self,chosen_worker,product_price):
        self.staff_members[chosen_worker]['vendas'] += product_price
        self.staff_members[chosen_worker]['bonus'] += (product_price * 0.10)
        print()

    def show_staff_sales(self,):
        for k, v in self.staff_members.items():
            print(f'{k}: Vendas = R${v['vendas']}, Bonus = R${v['bonus']} ')

