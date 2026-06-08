class Inventory:
    def __init__(self):
        self.items = {
            'Apontador': {'quantidade': 10, 'preco':3.50},
            'Borracha': {'quantidade': 25, 'preco': 2.00},
            'Caderno': {'quantidade': 18, 'preco': 22.50},
            'Corretivo': {'quantidade': 32, 'preco': 6.50},
            'Lapis': {'quantidade': 52, 'preco': 1.50},
        }


    def show_quantity(self,):
        for k,v in self.items.items():
           print(f'{k}: quantidade = {v['quantidade']}')

        print()

    def show_items(self):
        for k in self.items:
            print(k)

        print()
