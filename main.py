from code.Inventory import Inventory
app = True

i = Inventory()

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
        i.looking_for_product(item)

    elif interface == 2:
        pass

    elif interface == 3:
        print('Fechando...')