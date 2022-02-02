from src.leilao.dominio import Leilao, Usuario, Lance

gui = Usuario('gui')
yuri = Usuario('yuri')
matheus = Usuario('matheus')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular ')
leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')
