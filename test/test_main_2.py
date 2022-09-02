import pytest 
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento

@pytest.mark.main2
@pytest.mark.main3
def test_cria_pessoa():
    pessoa1 = PessoaFisica('Carlos Magno', 'magno@email.com', '524.222.452-6')
    assert pessoa1 in PessoaFisica.lista_pessoas

@pytest.mark.main2
@pytest.mark.main3
def test_add_endereco():
    pessoa1 = PessoaFisica('Carlos Magno', 'magno@email.com', '524.222.452-6')
    end1 = Endereco('08320330', 430)

    pessoa1.adicionar_endereco('casa', end1)
    assert f'{pessoa1.listar_enderecos().keys()}' == "dict_keys(['casa'])"

@pytest.mark.main2
@pytest.mark.main3
def test_cria_produto():
    sabonete = Produto("0010342967", "Sabonete")
    assert sabonete in Produto.lista

@pytest.mark.main2
@pytest.mark.main3
def test_cria_carrinho_e_add_produto():
    sabonete = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete,5)
    assert carrinho.itens() == {'0010342967': 5}

@pytest.mark.main2
@pytest.mark.main3
def test_cria_pedido():
    pessoa1 = PessoaFisica('Carlos Magno', 'magno@email.com', '524.222.452-6')
    sabonete = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete,5)
    pedido = Pedido(pessoa1,carrinho)

    assert pedido.detalhes() == "Nome: Carlos Magno\nEndereços: []\nProdutos: {'0010342967': 5}"

@pytest.mark.main2
@pytest.mark.main3
def test_pagamento():
    pessoa1 = PessoaFisica('Carlos Magno', 'magno@email.com', '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido()
    pag = Pagamento(pedido)
    assert pag.processa_pagamento() == True


