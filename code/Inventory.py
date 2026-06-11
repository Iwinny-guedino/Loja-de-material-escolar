
class Inventory:
    def __init__(self):

        self.products = {'Apontador': {'quantidade': 10, 'preco': 3.50},
                         'Borracha': {'quantidade': 25, 'preco': 2.00},
                         'Caderno': {'quantidade': 18, 'preco': 22.50},
                         'Corretivo': {'quantidade': 32, 'preco': 6.50},
                         'Lapis': {'quantidade': 52, 'preco': 1.50}
                         }

    def show_inventory(self):
        for k,v in self.products.items(): # Exiba o estoque
            print(f'{k}: {v['quantidade']}')
            print()



    def subtract_products(self, product, quantity): # Diminui o número de items após venda
        self.products[product]['quantidade'] -= quantity

    def add_products(self):#adicione items ao seu estoque
        try:
            product = input('\nQual produto deseja adicionar ao estoque? ')
            quantity = int(input('\nDigite a quantidade: '))
        except:
            print('Input inválido')
            return

        if product in self.products:
            self.products[product]['quantidade'] += quantity

        else:
            price = float(input('\nDigite o preco do produto: '))
            if price:
                self.products.update({ product:{'quantidade': quantity, 'preco': price} })
            else:
                print('\nValor inválido, Voltando ao inicio.')
                return


