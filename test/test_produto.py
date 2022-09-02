import pytest
import numpy as np
from classes.Produto import Produto

@pytest.mark.produto
def test_cria_objeto():
    prod = Produto('79', 'BoardMaster')
    assert prod.id == '79'
    assert prod.nome == 'BoardMaster'

@pytest.mark.produto
def test_busca_nome():
    prod = Produto('79', 'BoardMaster')
    resultado = Produto.busca_nome('Master')
    assert 'BoardMaster' == resultado[0].nome

@pytest.mark.produto
def test_busca_nome_maiusculo_e_minusculo():
    prod = Produto('79', 'BoardMaster')
    resultado = Produto.busca_nome('board')
    assert 'BoardMaster' == resultado[0].nome

@pytest.mark.produto
def test_pegar_id():
    prod = Produto('79', 'BoardMaster')
    _id = prod.get_id()
    assert _id == '79' 