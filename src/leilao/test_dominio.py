from unittest import TestCase

from leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def setUp(self):
        self.gui = Usuario('gui')
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular ')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionamos_em_ordem_crescente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionamos_em_ordem_decrescente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.lances.append(self.lance_do_gui)
        self.leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_apenas_um_lance(self):
        self.leilao.lances.append(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances_usuarios_diferentes(self):
        vini = Usuario('vini')
        yuri = Usuario('yuri')

        lance_do_vini = Lance(vini, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.lances.append(self.lance_do_gui)
        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(lance_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


    def test_deve_retornar_o_menor_e_maior_valor_quando_leilao_tiver_tres_lances_mesmo_usuario(self):
        gui = Usuario('gui')

        lance_do_gui_1 = Lance(gui, 100.0)
        lance_do_gui_2 = Lance(gui, 120.0)
        lance_do_gui_3 = Lance(gui, 150.0)

        leilao = Leilao('Novo Leilao')
        leilao.lances.append(lance_do_gui_1)
        leilao.lances.append(lance_do_gui_2)
        leilao.lances.append(lance_do_gui_3)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
