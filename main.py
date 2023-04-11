from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maquina = CoffeeMaker()
maquinha_dinheiro = MoneyMachine()

maquina_ligada = True
while maquina_ligada:
    pedido = input(f"Qual o seu pedido? {menu.get_items()}")
    if pedido == 'desligar':
        maquina_ligada = False
    elif pedido == 'status':
        print(maquina.report())

    elif pedido == 'latte' or pedido == 'espresso' or pedido == 'cappuccino':
        bebida = menu.find_drink(pedido)
        if maquina.is_resource_sufficient(bebida):
            maquinha_dinheiro.make_payment(bebida.cost)
            maquina.make_coffee(bebida)
    else:
        print('Digite algo do cardapio')
