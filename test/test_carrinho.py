import pytest
from classes.Produto import Produto
from classes.Carrinho import Carrinho

@pytest.mark.carrinho
def test_cria_objeto_e_add_item():
    prod = Produto('79', 'BoardMaster')
    carrinho = Carrinho()
    carrinho.adicionar_item(prod, 7)
    assert carrinho.itens() == {'79': 7}

@pytest.mark.carrinho
def test_remove_item():
    prod = Produto('79', 'BoardMaster')
    carrinho = Carrinho()
    carrinho.adicionar_item(prod, 7)
    assert carrinho.remover_item(prod) == {}

