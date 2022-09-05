import pytest
import numpy as np
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco

@pytest.mark.pessoa
def test_cria_objeto():
    user = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
    assert user.nome == 'Alexandre Magno'
    assert user.email == 'ale@gmail.com'
    assert user.cpf == '000.000.000-00'

@pytest.mark.pessoa
@pytest.mark.main3
def test_busca_nome():
    user1 = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
    resultado = PessoaFisica.busca_nome('Ale')
    assert resultado[0].nome == user1.nome

@pytest.mark.pessoa
def test_busca_nome_letras_maiusculas_e_minusculas():
    user2 = PessoaFisica('Carlos Magno', 'tiago@email.com', '524.222.452-6')
    resultado = PessoaFisica.busca_nome('carlos')
    assert resultado[0].nome == user2.nome

@pytest.mark.pessoa
def test_get_endereco():
    user = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
    end = Endereco('04546042', 300)
    user.adicionar_endereco('inspi', end)
    assert user.get_endereco('inspi')== 'Rua Quatá'

@pytest.mark.pessoa
def test_add_endereco_e_listar_endereco():
    user1 = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
    end = Endereco('04546042', 300)

    user1.adicionar_endereco('inspi', end)
    ends = user1.listar_enderecos()
    assert f'{ends.keys()}' == "dict_keys(['inspi'])"
