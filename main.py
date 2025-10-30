from clientes import *
from entregadores import*
def menu_cliente(cliente):
    while True:
        print("\n\033[1;34mMENU CLIENTE \033[0m")
        print("\033[1;33m" + "="*30 + "\033[0m")
        print("1️⃣  Mostrar cardápio 2️⃣  Fazer pedido 3️⃣  Ver pedido 4️⃣  Cancelar pedido 5️⃣  Sair")
        opcao = input("Escolha uma opção: ")
        print()
        if opcao == "1":
            ver_cardapio()
        elif opcao == "2":
            fazer_pedido(cliente)
        elif opcao == "3":
            ver_pedido(cliente)
        elif opcao == "4":
            cancelar_pedido(cliente)
        elif opcao == "5":
            print("Saindo do menu cliente...")
            break
        else:
            print("\033[1;36m⚠️  Opção inválida! Digite 1, 2, 3, 4 ou 5.\033[0m")
            
def menu_entregador(entregador):
    while True:
        print("\n\033[1;34mMENU ENTREGADOR \033[0m")
        print("\033[1;33m" + "="*30 + "\033[0m")
        print("1️⃣  Ver pedidos disponíveis 2️⃣  Atualizar status de entrega 3️⃣  Ver histórico de entregas 4️⃣  Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            pedidos_disponiveis()
        elif opcao == "2":
            atualizar_pedidos(entregador)
        elif opcao == "3":
            ver_historicos(entregador)
        elif opcao == "4":
            print("Saindo do menu entregador...")
            break
        else:
            print("\033[1;36m⚠️  Opção inválida! Digite 1, 2, 3 ou 4.\033[0m")
   
def menuIfood():
    while True:
        print()
        print("\033[1;37m" + "="*45 + "\033[0m")
        texto = "🤳🚴🏠 MENU PRINCIPAL - IFOOD 🍟🥤🍕 "
        largura = 40
        print("\033[1;31m" + texto.center(largura) + "\033[0m")
        print("\033[1;37m" + "="*45 + "\033[0m")
        print("1️⃣  Entrar como Cliente")
        print("2️⃣  Entrar como Entregador")
        print("3️⃣  Cadastrar como Cliente")
        print("4️⃣  Cadastrar como Entregador")
        print("5️⃣  Sair")
        
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            cliente = Cliente.login_cliente()
            if cliente:
                menu_cliente(cliente)
        elif opcao == "2":
            entregador = Entregador.login_entregador()
            if entregador:
                menu_entregador(entregador)
        elif opcao == "3":
            cliente = Cliente.cadastrar_cliente()
            if cliente:  
                menu_cliente(cliente)
        elif opcao == "4":
            entregador = Entregador.cadastrar_entregador()
            if entregador:
                menu_entregador(entregador)
        elif opcao == "5":
            print("Saindo do Ifood... 🍕")
            break
        else:
            print("\033[1;36m⚠️  Opção inválida! Digite 1, 2, 3, 4 ou 5.\033[0m")

if __name__ == "__main__":
    menuIfood()
