
class Transaction:
    def __init__(self,cash_register,inventory,staff):
        self.cr = cash_register
        self.i = inventory
        self.s = staff
        self.s.seller = self.s.staff_working()


    def looking_for_product(self, product): # Procurando produto no estoque
        if product in self.i.products:
            if self.i.products[product]['quantidade'] > 0:
                print(f'Há {self.i.products[product]['quantidade']}, {product}(es/os) no estoque.\n')
                self.sell(product, self.i.products[product]['preco'])

    def sell(self, product, price):
        quantity = float(input(f'Quantos {product}(es/os) deseja vender: '))
        total = quantity * price
        print(f'O valor total é de: {total}')
        self.proceed(total, product, quantity)

    def proceed(self, total, product, quantity): #Consirmação de compra
            foward = input('Dejesa continuar com a venda? (S/N): ').lower()
            if foward == 's':
                self.transaction(total, product, quantity)
            elif foward == 'n':
                print('Venda cancelada.')
                return
            else:
                print('Por favor, digite uma das opções acima.')
                pass

    def transaction(self,total, product, quantity):
        payment = float(input('\nValor depositado: '))
        if payment > total:
            change = payment - total
            self.i.subtract_products(product, quantity)
            self.cr.add_money(total)
            self.s.staff_sales(self.s.seller, total)
            print(f'\nSeu troco é de R$ {change}')

        elif payment == total:
            self.cr.add_money(total)
            self.i.subtract_products(product, quantity)
            self.s.staff_sales(self.s.seller, total)
            print(f'\nSeu troco é R$ 0')

        elif payment < total:
            print('\nDeposito insuficiente.')

        else:
            print('\nInput inválido!')
