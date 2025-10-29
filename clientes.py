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
  