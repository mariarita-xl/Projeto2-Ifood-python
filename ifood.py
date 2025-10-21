# Meu projeto iFood

from ifood import Usuario, Entregador, Cliente

def menuIfood():
    while True:
        print()
        print("\033[1;37m" + "#"*45 + "\033[0m") 
        texto = "🤳🚴🏠 MENU PRINCIPAL - IFOOD 🍟🥤🍕 "
        largura = 40
        print("\033[1;31m" + texto.center(largura) + "\033[0m")
        print("\033[1;37m" + "#"*45 + "\033[0m") 
        print("1️⃣  Entrar como entregador  2️⃣  Entrar como cliente  3️⃣  Sair")

        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            print("Entrando como entregador🛵")  
        elif opcao == "2":
           print("Entrando como cliente...🧑‍💻👩‍💻")  
        elif opcao == "3":
            print("Saindo do Ifood... 🍕")
            break

        else:
            print("\033[1;36m⚠️  Opção inválida! Digite 1, 2 ou 3.\033[0m")

      
if __name__ == "__main__":
    menuIfood()
