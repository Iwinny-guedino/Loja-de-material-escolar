from code.Inventory import Inventory
from code.Cash_register import CashRegister
from code.Transaction import Transaction
from code.Staff import Staff

app = True

s = Staff()
i = Inventory()
cr = CashRegister()
t = Transaction(cr,i,s)

while app:
    print(' """""Loja de materiais escolares""""" \n'
          '1 - Vender\n'
          '2 - Estoque\n'
          '3 - Mostrar Caixa\n'
          '4 - Quadro de Funcionários\n'
          '5- Sair'

          )

    interface = int(input('Escolha uma das opções: '))
    print()

    if interface == 1:
        item = input("Digite o nome do item: \n")

        t.looking_for_product(item)

    elif interface == 2:
        i.show_inventory()

    elif interface == 3:
        cr.show_money()

    elif interface == 4:
        s.show_staff_sales()

    elif interface == 5:
        print('\nFechando...')
        app = False