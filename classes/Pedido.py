from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re

class Pedido:
    EM_ABERTO = 1
    PAGO = 2

    def __init__(self,pessoa,carrinho):
        self.endereco_entrega = ''
        self.endereco_faturamento = ''
        self.pessoa = pessoa
        self.carrinho = carrinho
    
    def detalhes(self):
        return f'Nome: {self.pessoa.nome}\nEndereços: {list(self.pessoa.listar_enderecos().keys())}\nProdutos: {self.carrinho.itens()}'
    