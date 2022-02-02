from unittest import TestCase

from leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('gui')
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular ')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionamos_em_ordem_crescente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe_lance(lance_do_yuri)
        self.leilao.propoe_lance(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionamos_em_ordem_decrescente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe_lance(self.lance_do_gui)
        self.leilao.propoe_lance(lance_do_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_apenas_um_lance(self):
        self.leilao.propoe_lance(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances_usuarios_diferentes(self):
        vini = Usuario('vini')
        yuri = Usuario('yuri')

        lance_do_vini = Lance(vini, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe_lance(self.lance_do_gui)
        self.leilao.propoe_lance(lance_do_yuri)
        self.leilao.propoe_lance(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_leilao_nao_tenha_lances(self):
        self.leilao.propoe_lance(self.lance_do_gui)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    # Se o ultimo usuario for diferente, deve permitir propor um lance
    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('yuri')
        lance_yuri = Lance(yuri, 200.0)

        self.leilao.propoe_lance(self.lance_do_gui)
        self.leilao.propoe_lance(lance_yuri)

        quantidade_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_lances_recebido)

    # Se o ultimo usuario for o mesmo(atual), não deve permitir propor o lance
    def test_nao_deve_permitir_propro_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)
        self.leilao.propoe_lance(self.lance_do_gui)

        try:
            self.leilao.propoe_lance(lance_do_gui200)
            self.fail('Não lançou exceção')
        except ValueError:
            quantidade_lances_recebidos = len(self.leilao.lances)
            self.assertEqual(1, quantidade_lances_recebidos)
