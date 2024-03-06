class Jogos:
    nome = '' 
    categoria = ''
    ativo = False

jogo_xadrez = Jogos()
jogo_xadrez.nome = 'Best Chess Set Ever'
jogo_xadrez.categoria = 'Estratégia Abstrata'
jogo_santorini = Jogos()

jogos = [jogo_xadrez, jogo_santorini]

print(jogo_xadrez.ativo)