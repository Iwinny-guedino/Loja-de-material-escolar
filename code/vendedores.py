from random import choice
class Staff:
    def __init__(self):
        self.staff_one = {'Rodrigo': 0}
        self.staff_two = {'Clara': 0}
        self.staff_three = {'Mariana': 0}

    def chosen_staff_member(self):
        staff_list = [self.staff_one, self.staff_two, self.staff_three]
        chosen_worker = choice(staff_list)
        return chosen_worker

