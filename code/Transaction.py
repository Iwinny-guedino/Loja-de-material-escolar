

class Transaction:
    def __init__(self,cash_register,inventory):
        self.cr = cash_register
        self.i = inventory


    def looking_for_product(self, product):
        if product in self.i.products:
            if self.i.products[product]['quantidade'] > 0:
                print(f'Há {self.i.products[product]['quantidade']}, de {product} no estoque.')
                self.sell(product, self.i.products[product]['preco'])

    def sell(self, product, price):
        quantity = float(input(f'Quantos {product} para esta venda: '))
        total = quantity * price
        self.proceed(total)

    def proceed(self, total):
            foward = input('Dejesa continuar? (S/N): ').lower()
            if foward == 's':
                self.transaction(total)
            elif foward == 'n':
                print('Venda cancelada.')
                return
            else:
                print('Por favor, digite uma das opções acima.')
                pass

    def transaction(self,total):
        payment = float(input('Valor depositado: '))
        if payment > total:
            change = payment - total
            self.cr.add_money(total)
            print(f'Seu troco é de R$ {change}')

        elif payment == total:
            self.cr.add_money(total)
            print(f'Seu troco é R$ 0')

        elif payment < total:
            print('Deposito insuficiente.')

        else:
            print('Input inválido!')
