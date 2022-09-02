import pytest
import numpy as np
from classes.PessoaFisica import PessoaFisica

@pytest.mark.pessoa
def test_cria_objeto():
    user = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
    assert user.nome == 'Alexandre Magno'
    assert user.email == 'ale@gmail.com'
    assert user.cpf == '000.000.000-00'

@pytest.mark.pessoa
def test_busca_nome():
    user1 = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
    resultado = PessoaFisica.busca_nome('Ale')
    assert resultado[0].nome == user1.nome

@pytest.mark.pessoa
def test_busca_nome_letras_maiusculas_e_minusculas():
    user2 = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    resultado = PessoaFisica.busca_nome('carlos')
    assert resultado[0].nome == user2.nome

@pytest.mark.pessoa
def test_get_endereco():
    user1 = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
    #criar end e add
    end = user1.get_endereco('inspi')
    assert end == 'Rua Quatá'

#teste de integração
# @pytest.mark.pessoa
# def test_add_e_lista_endereco():
#     user1 = PessoaFisica('Alexandre Magno', 'ale@gmail.com', '000.000.000-00')
#     end = Endereco('04546042', 300)

#     lista = user1.adicionar_endereco('inspi', end)


