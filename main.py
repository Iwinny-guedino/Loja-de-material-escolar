from code.vendedores import Staff
from code.estoque import Inventory
from code.venda import Transaction


app = True

s = Staff()
i = Inventory()
t = Transaction()

staff_worker = s.chosen_staff_member()

while app:
    print(' """""Loja de materiais escolares""""" \n'
          '1 - Vender\n'
          '2 - Estoque\n'
          '3 - Fechar caixa\n'

          )

    interface = int(input('Escolha uma das opções: '))
    print()

    if interface == 1:
        item = input("Digite o nome do item: ")
        t.find_item(item)
    elif interface == 2:
        i.show_quantity()
    elif interface == 3:
        print('Fechando...')