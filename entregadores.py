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
