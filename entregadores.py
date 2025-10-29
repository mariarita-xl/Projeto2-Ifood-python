import json
import os
from usuario import Usuario
from clientes import Cliente

arquivo_entregadores = "__entregadores.json"

class Entregador(Usuario):
    def __init__(self, cpf, nome_completo, telefone, email, senha):
        super().__init__(cpf, nome_completo, telefone, email, senha)
        self.pedidos_entregues = []

    @staticmethod
    def carregar_entregadores():
        if not os.path.exists(arquivo_entregadores):
            return []
        try:
            with open(arquivo_entregadores, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return []

    @staticmethod
    def salvar_entregadores(entregadores):
        with open(arquivo_entregadores, "w", encoding="utf-8") as arquivo:
            json.dump(entregadores, arquivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cadastrar_entregador():
        entregadores = Entregador.carregar_entregadores()
        print("\n\033[1;34mCADASTRO DE ENTREGADOR\033[0m")
        print("\033[1;33m" + "="*30 + "\033[0m")
        cpf = input("CPF: ")
        nome = input("Nome completo: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        senha = input("Senha: ")

        for e in entregadores:
            if e["cpf"] == cpf or e["email"] == email:
                print("\033[1;31m⚠️  Entregador já cadastrado!\033[0m")
                return None

        novo_entregador = {
            "cpf": cpf,
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "senha": senha,
            "pedidos_entregues": []
        }
        entregadores.append(novo_entregador)
        Entregador.salvar_entregadores(entregadores)
        print(f"\033[1;32m✅ Entregador {nome} cadastrado com sucesso!\033[0m")
        return novo_entregador

    @staticmethod
    def login_entregador():
        entregadores = Entregador.carregar_entregadores()
        print("\n\033[1;34mLOGIN DO ENTREGADOR\033[0m")
        print("\033[1;33m" + "="*30 + "\033[0m")
        email = input("Email: ")
        senha = input("Senha: ")

        for e in entregadores:
            if e["email"] == email and e["senha"] == senha:
                print(f"\033[1;32m✅ Bem-vindo, {e['nome']}!\033[0m")
                return e
        print("\033[1;31m⚠️  Email e senha não encontrados\033[0m")
        return None


def pedidos_disponiveis():
    clientes = Cliente.carregar_clientes()
    lista = []
    indice = 1

    print("\n\033[1;36m" + "="*40 + "\033[0m")
    print("\033[1;33m📦 PEDIDOS DISPONÍVEIS 📦\033[0m")
    print("\033[1;36m" + "="*40 + "\033[0m")

    for c in clientes:
        for pedido in c.get("pedidos", []):
            print(f"{indice}. {pedido['descricao']} x{pedido['quantidade']} - R${pedido['total']} (Cliente: {c.get('nome')}, Endereço: {c.get('endereco')})")
            lista.append((c, pedido))
            indice += 1

    if not lista:
        print("\033[1;31m  Nenhum pedido disponível no momento.\033[0m")
    return lista


def atualizar_pedidos(entregador):
    lista = pedidos_disponiveis()
    if not lista:
        return

    try:
        escolha = int(input("Digite o número do pedido que você quer entregar: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    if escolha < 1 or escolha > len(lista):
        print("Número inválido!")
        return

    cliente_dict, pedido_dict = lista[escolha - 1]

    todos_clientes = Cliente.carregar_clientes()
    for c in todos_clientes:
        if c["cpf"] == cliente_dict["cpf"]:
            for i, p in enumerate(c.get("pedidos", [])):
                if p["descricao"] == pedido_dict["descricao"] and p["quantidade"] == pedido_dict["quantidade"] and p["total"] == pedido_dict["total"]:
                    c["pedidos"].pop(i)
                    break
            break
    Cliente.salvar_clientes(todos_clientes)

    entregadores = Entregador.carregar_entregadores()
    for e in entregadores:
        if e["cpf"] == entregador["cpf"]:
            registro = {
                "descricao": pedido_dict["descricao"],
                "quantidade": pedido_dict["quantidade"],
                "total": pedido_dict["total"],
                "cliente_nome": cliente_dict.get("nome"),
                "cliente_cpf": cliente_dict.get("cpf"),
                "endereco": cliente_dict.get("endereco")
            }
            e.setdefault("pedidos_entregues", []).append(registro)
            break
    Entregador.salvar_entregadores(entregadores)

    print(f"\033[1;32m✅ Pedido entregue: {pedido_dict['descricao']} para {cliente_dict.get('nome')}\033[0m")


def ver_historicos(entregador):
    entregadores = Entregador.carregar_entregadores()
    for e in entregadores:
        if e["cpf"] == entregador["cpf"]:
            historico = e.get("pedidos_entregues", [])
            break
    else:
        print("Entregador não encontrado no sistema.")
        return

    print("\n\033[1;36m" + "="*40 + "\033[0m")
    print("\033[1;33m📚 HISTÓRICO DE ENTREGAS 📚\033[0m")
    print("\033[1;36m" + "="*40 + "\033[0m")
    if not historico:
        print("\033[1;31m  Nenhuma entrega registrada ainda.\033[0m")
        return

    for i, reg in enumerate(historico):
        print(f"{i+1}. {reg['descricao']} x{reg['quantidade']} - R${reg['total']} (Cliente: {reg.get('cliente_nome')}, Endereço: {reg.get('endereco')})")
