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

    def looking_for_product(self, product):
        if product in self.products:
            if self.products[product]['quantidade'] > 0:
                print(f'Há {self.products['quantidade']}, de {product} no estoque.')
                sell(product, product['preco'])


    def subtract_products(self, product, quantity): # Diminui o número de items após venda
        self.products[product]['quantidade'] -= quantity

    def add_products(self):#adicione items ao seu estoque
        try:
            product = input('Qual produto deseja adicionar ao estoque? ')
            quantity = int(input('Digite a quantidade: '))
        except:
            print('Input inválido')
            return

        if product in self.products:
            self.products[product]['quantidade'] += quantity

        else:
            price = float(input('Digite o preco do produto: '))
            if price:
                self.products.update({ product:{'quantidade': quantity, 'preco': price} })
            else:
                print('Valor inválido, Voltando ao inicio.')
                return


