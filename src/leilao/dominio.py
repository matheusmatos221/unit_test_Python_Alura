class Usuario:

    def __init__(self, nome, carteira=0.0):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_e_valido(valor):
            raise ValueError("Não pode propor um lance com valor maior que o da carteira")

        lance = Lance(self, valor)
        leilao.propoe_lance(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_e_valido(self, valor):
        return valor <= self.carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe_lance(self, lance: Lance):
        if not self._lance_e_valido(lance):
            raise ValueError("Erro ao propor lance!")

        else:
            if not self._tem_lances():
                if not self.__lances:
                    self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _valor_e_maior_que_o_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_e_valido(self, lance):
        return not self._tem_lances() or \
               (self._usuarios_diferentes(lance) and self._valor_e_maior_que_o_anterior(lance))
