from code.estoque import Inventory

i = Inventory()

class Transaction:
    def __init__(self):
        self.cash_register = 90

    def find_item(self,item):
        if item in i.items:
            print(f'{item}: R${i.items[item]['preco']:.2f}')
            print()
            self.confirm_sale(item)

    def confirm_sale(self,item):
        buy = input('Proseguir com a compra? (S/N)').lower()
        if buy == 's':
            quantidade = int(input(f"Qual a quantidade de {item} deseja comprar? "))
            total = i.items[item]['preco'] * quantidade
            print(f'O preço de {quantidade} {item} é : R${total:.2f}')
            self.payment(total)
        else:
            return print('Compra cancelada')


    def payment(self,total):

        deposito = int(input(f'Deposite {total} ou mais: '))
        if deposito > total:
            devolucao = deposito - total

            self.cash_register -= devolucao
            return print(f'O seu troco é de R${devolucao:.2f}')

        elif deposito == total:
            return print('Obrigado pela compra!')

        elif deposito < total:
            return print('Saldo insuficiente!')

        else:
            return print('Input inválido, não aceitamos este metodo de poagamento.')



