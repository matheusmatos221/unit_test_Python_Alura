import pytest as pytest
from src.leilao.dominio import Usuario, Leilao


@pytest.fixture()
def user_vini():
    return Usuario('vini', 100.0)

@pytest.fixture()
def leilao_celular():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(user_vini, leilao_celular):
    user_vini.propoe_lance(leilao_celular, 50.0)

    assert user_vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(user_vini, leilao_celular):
    user_vini.propoe_lance(leilao_celular, 1.0)

    assert user_vini.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(user_vini, leilao_celular):
    user_vini.propoe_lance(leilao_celular, 100.0)

    assert user_vini.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(user_vini, leilao_celular):
    with pytest.raises(ValueError):
        user_vini.propoe_lance(leilao_celular, 150.0)
