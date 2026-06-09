from code.Cash_register import CashRegister

cr = CashRegister

class Transaction:

    def sell(self, product, price):
        quantity = int(input(f'Quantos {product} para esta venda: '))
        total = product * price
        self.proceed(total)

    def proceed(self, total):
        while True:
            foward = input('Dejesa continuar? (S/N').lower()
            if foward == 's':
                self.transaction(total)
            elif foward == 'n':
                print('Venda cancelada.')
                return
            else:
                print('Por favor, digite uma das opções acima.')
                pass

    def transaction(self,total):

        while True:
            payment = float(input('Valor depositado: '))
            if payment > total:
                change = payment - total
                cr.add_money(total)
                return print(f'Seu troco é de R$ {change}')

            elif payment == total:
                cr.add_money(total)
                return print(f'Seu troco é R$ 0')

            elif payment < total:
                print('Deposito insuficiente.')
                self.proceed(total)
                continue

            else:
                print('Input inválido!')
                self.proceed(total)









