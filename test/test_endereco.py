import pytest
import numpy as np
import requests
from classes.Endereco import Endereco

@pytest.mark.endereco
def test_criacao_de_objetos():
    end = Endereco('08320330',300)
    assert end.rua == 'Rua Clemente Falcão'
    assert end.cidade == 'São Paulo'

@pytest.mark.endereco
def test_cep_como_int():
    end = Endereco.consultar_cep(15417000)
    assert end == {'cep': '15417-000', 'logradouro': '', 'complemento': '', 'bairro': 'Monte Verde Paulista', 'localidade': 'Cajobi', 'uf': 'SP', 'ibge': '3509304', 'gia': '2422', 'ddd': '17', 'siafi': '6287'}

@pytest.mark.endereco
def test_cep_como_string():
    end = Endereco.consultar_cep('15417000')
    assert end == {'cep': '15417-000', 'logradouro': '', 'complemento': '', 'bairro': 'Monte Verde Paulista', 'localidade': 'Cajobi', 'uf': 'SP', 'ibge': '3509304', 'gia': '2422', 'ddd': '17', 'siafi': '6287'} 

@pytest.mark.endereco
def test_cep_invalido_poucos_digitos():
    end = Endereco.consultar_cep(5417000)
    assert end == False

@pytest.mark.endereco
def test_cep_invalido_muitos_digitos():
    end = Endereco.consultar_cep(5417000771)
    assert end == False

@pytest.mark.endereco
def test_cep_nao_existente():
    end = Endereco.consultar_cep(11111111)
    assert end == False

@pytest.mark.endereco
def test_internet_nao_conectada():
    with requests.exceptions.ConnectionError as connection:
        Endereco.consultar_cep()
        assert '' in str(connection.value)