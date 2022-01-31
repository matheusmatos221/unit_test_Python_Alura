from unittest import TestCase

from leilao.dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

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


    def test_deve_retornar_o_menor_e_maior_valor_quando_leilao_tiver_tres_lances_mesmo_usuario(self):
        gui = Usuario('gui')

        lance_do_gui_1 = Lance(gui, 100.0)
        lance_do_gui_2 = Lance(gui, 120.0)
        lance_do_gui_3 = Lance(gui, 150.0)

        self.leilao.propoe_lance(lance_do_gui_1)
        self.leilao.propoe_lance(lance_do_gui_2)
        self.leilao.propoe_lance(lance_do_gui_3)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
