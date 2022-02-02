from src.leilao.dominio import Usuario, Lance, Leilao


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    user_vini = Usuario('vini', 100.0)
    leilao_celular = Leilao('Celular')

    user_vini.propoe_lance(leilao_celular, 50.0)

    assert user_vini.carteira == 50.0
