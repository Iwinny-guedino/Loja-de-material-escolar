from code.Inventory import Inventory
from code.Cash_register import CashRegister
from code.Transaction import Transaction

app = True

i = Inventory()
cr = CashRegister()
t = Transaction(cr,i)

while app:
    print(' """""Loja de materiais escolares""""" \n'
          '1 - Vender\n'
          '2 - Estoque\n'
          '3 - Mostrar caixa\n'
          '4 - Fechar caixa\n'

          )

    interface = int(input('Escolha uma das opções: '))
    print()

    if interface == 1:
        item = input("Digite o nome do item: ")
        t.looking_for_product(item)

    elif interface == 2:
        i.show_inventory()

    elif interface == 3:
        cr.show_money()


    elif interface == 4:
        print('Fechando...')
        app = False