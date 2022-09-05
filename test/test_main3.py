import pytest 
import copy
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento

#Testes únicos para o main3
@pytest.mark.main3
def test_add_endereco_de_fatura_e_entrega():
    carrinho = Carrinho()
    pessoa1 = PessoaFisica('Carlos Magno', 'magno@email.com', '524.222.452-6')
    end1 = Endereco('08320330', 430)
    end2 = Endereco('04546042', 300)

    pedido = Pedido(pessoa1,carrinho)
    pedido.endereco_entrega = copy.deepcopy(end1) 
    pedido.endereco_faturamento = copy.deepcopy(end2)

    assert pedido.endereco_entrega.rua == 'Rua Clemente Falcão'
    assert pedido.endereco_faturamento.rua == 'Rua Quatá'