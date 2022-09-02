import pytest
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento

@pytest.mark.pedido
def test_cria_objeto_e_devolve_detalhes():
    user = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
    prod = Produto('79', 'BoardMaster')
    carrinho = Carrinho()
    carrinho.adicionar_item(prod,7)
    pedido = Pedido(user,carrinho)

    assert pedido.detalhes() == "Nome: Alexandre Magno\nEndereços: []\nProdutos: {'79': 7}"