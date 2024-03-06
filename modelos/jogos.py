class Jogos:
    jogos = [] # tudo criado no init ja coloca na lista.

    def __init__(self, nome, categoria):
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False
        Jogos.jogos.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_jogos():
        for jogo in Jogos.jogos: # Para cada restaurante na minha lista in restaurantes. posso por a classe para ficar mais claro. 
            print(f'{jogo.nome} | {jogo.categoria} | {jogo.ativo}') # Está pegando direto da lista que já armazenou esse objeto

jogo_xadrez = Jogos('Best Chess Set Ever', 'Estratégia Abstrata')
jogo_santorini = Jogos('Santorini', 'Educativo')

Jogos.listar_jogos()


# Informações teóricas:
# __init__ : vai construir um método construtor. Sempre que criar a instância de um objeto, esse método é chamado. Usado sempre que quer garantir que quando tiver a instância daquela classe, sempre que tiver objeto, quero ter aqueles valores definidos. 
# self: cada jogo tem suas próprias informações. Referência da instância atua lque estamos usando no momento. 
# Médoto especial: __str__: mostrar método em formato de texto. Sempre que criar um métodoqual objeto que quero referenciar? 
# Método especial tem esses dois __ nome do metodo __
# Podemos criar nossos próprios métodos como o listar_jogos