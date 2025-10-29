import json
import os
from usuario import Usuario

arquivo_clientes = "__clientes.json"

cardapio = [
        {"codigo": "1", "descricao": "Pão de queijo", "preco": 2.00},
        {"codigo": "2", "descricao": "Tapioca", "preco": 7.99},
        {"codigo": "3", "descricao": "Bolo de chocolate (bandeja)", "preco": 20.99},
        {"codigo": "4", "descricao": "Sonho (doce de leite)", "preco": 2.50},
        {"codigo": "5", "descricao": "Pão caseiro", "preco": 0.89},
        {"codigo": "6", "descricao": "Pão pizza", "preco": 0.89},
        {"codigo": "7", "descricao": "Pão pizza (grande)", "preco": 5.50},
        {"codigo": "8", "descricao": "Pastel de queijo", "preco": 6.00},
        {"codigo": "9", "descricao": "Pastel de carne", "preco": 5.50},
        {"codigo": "10", "descricao": "Torta de frango (pedaço)", "preco": 4.00},
        {"codigo": "11", "descricao": "Cachorro quente", "preco": 5.00},
        {"codigo": "12", "descricao": "Broa de milho", "preco": 1.00},
        {"codigo": "13", "descricao": "Coxinha de frango", "preco": 5.50},
    ]

class Cliente(Usuario):
    def __init__(self, cpf, nome_completo, telefone, email, senha, endereco):
        super().__init__(cpf, nome_completo, telefone, email, senha)
        self.endereco = endereco
        self.pedidos = []

    @staticmethod
    def carregar_clientes():
        """
        Método estático que carrega a lista de clientes do JSON.
        Retorna lista vazia se não existir ou JSON inválido.
        """
        if not os.path.exists(arquivo_clientes):
            return []  
        try:
            with open(arquivo_clientes, "r",  encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return []  

    @staticmethod
    def salvar_clientes(clientes):
       """
       Método estático que salva a lista de clientes no JSON, sobrescrevendo o arquivo existente.
       """
       with open(arquivo_clientes, "w",  encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
  
    @staticmethod
    def cadastrar_cliente():
        """
        Cadastra um novo cliente e salva no JSON.
        """
        dados = Cliente.carregar_clientes()
        print("\n\033[1;34mCADASTRO DE CLIENTE\033[0m")
        print("\033[1;33m" + "="*30 + "\033[0m")
        cpf = input("CPF: ")
        nome = input("Nome completo: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        senha = input("Senha: ")
        endereco = input("Endereço: ")

        for cliente in dados:
            if cliente["cpf"] == cpf or cliente["email"] == email:
                print("\033[1;31m⚠️  Cliente já cadastrado!\033[0m")
                return None

        novo_cliente = {
            "cpf": cpf,
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "senha": senha,
            "endereco": endereco,
            "pedidos": []
        }
        dados.append(novo_cliente)
        Cliente.salvar_clientes(dados)
        print(f"\033[1;32m✅ Cliente {nome} cadastrado com sucesso!\033[0m")
        return novo_cliente

    @staticmethod
    def login_cliente():
        """
        Login do cliente a partir do JSON.
        """
        dados = Cliente.carregar_clientes()
        print("\n\033[1;34mLOGIN DO CLIENTE\033[0m")
        print("\033[1;33m" + "="*30 + "\033[0m")
        email = input("Email: ")
        senha = input("Senha: ")

        for cliente in dados:
            if cliente["email"] == email and cliente["senha"] == senha:
                print(f"\033[1;32mBem-vindo, {cliente['nome']}!\033[0m")
                return cliente
        print("\033[1;31m ⚠️  Email e senha não encontrados!\033[0m")
        return None
    
def ver_cardapio():
    print("\033[1;33m" + "="*40 + "\033[0m")  
    print("\033[1;36m   CARDÁPIO - PADARIA POR DO SOL   \033[0m")
    print("\033[1;33m" + "="*40 + "\033[0m")

    for item in cardapio:
        print(f"{item['codigo']}. {item['descricao']} - R${item['preco']}")

def fazer_pedido(cliente):
    ver_cardapio()
    print("\n\033[1;36m" + "="*40 + "\033[0m")        
    print("\033[1;33m🛒 FAZENDO PEDIDO... 🛒\033[0m") 
    print("\033[1;36m" + "="*40 + "\033[0m")
    codigo = input("Digite o código do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    
    produto = None
    for item in cardapio:
        if item['codigo'] == codigo:
            produto = item
            break

    if produto:
        cliente["pedidos"].append({
            "descricao": produto['descricao'],
            "quantidade": quantidade,
            "total": produto['preco'] * quantidade
        })
        print(f"\033[1;32m✅ Pedido adicionado: {quantidade}x {produto['descricao']}\033[0m")
        
        todos_clientes = Cliente.carregar_clientes()
        for c in todos_clientes:
            if c["cpf"] == cliente["cpf"]:
                c["pedidos"] = cliente["pedidos"]  
                break
        Cliente.salvar_clientes(todos_clientes)
    else:
        print("❌ Produto não encontrado!")


def ver_pedido(cliente):
    if cliente["pedidos"] == []:
        print("\033[1;31m📭 Seu carrinho está vazio!\033[0m")
        return
    
    print("\n\033[1;36m" + "="*40 + "\033[0m")
    print("\033[1;33m🧾 VENDO PEDIDO... 🧾\033[0m")
    print("\033[1;36m" + "="*40 + "\033[0m") 
    for pedido in cliente["pedidos"]:
        print(f"{pedido['descricao']} x{pedido['quantidade']} - R${pedido['total']}")

def cancelar_pedido(cliente):
    if cliente["pedidos"] == []:
        print("❌ Não há pedidos para cancelar!")
        return

    print("\nSEUS PEDIDOS:")
    for i in range(len(cliente["pedidos"])):
        pedido = cliente["pedidos"][i]
        print(f"{i+1}. {pedido['descricao']} x{pedido['quantidade']} - R${pedido['total']}")

    indice = int(input("Digite o número do pedido que deseja cancelar: "))
    if 1 <= indice <= len(cliente["pedidos"]):
        pedido_cancelado = cliente["pedidos"].pop(indice - 1)
        print(f"✅ Pedido cancelado: {pedido_cancelado['quantidade']}x {pedido_cancelado['descricao']}")

        todos_clientes = Cliente.carregar_clientes()
        for c in todos_clientes:
            if c["cpf"] == cliente["cpf"]:
                c["pedidos"] = cliente["pedidos"]
                break
        Cliente.salvar_clientes(todos_clientes)
    else:
        print("❌ Número inválido!")
    