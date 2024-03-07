class Jogos:
    jogos = [] # tudo criado no init ja coloca na lista.

    def __init__(self, nome, categoria):
        self._nome = nome.title() 
        self._categoria = categoria.upper()
        self._ativo = False # com o _, as pessoas vão usar a propriedade
        Jogos.jogos.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_jogos(cls):
        print(f'{'Nome do Jogo'.ljust(25)} | {'Categoria do Jogo'.ljust(25)} | {'Status do Jogo'}')
        for jogo in cls.jogos: # Para cada restaurante na minha lista in restaurantes. posso por a classe para ficar mais claro. 
            print(f'{jogo._nome.ljust(25)} | {jogo._categoria.ljust(25)} | {jogo.ativo}') # Está pegando direto da lista que já armazenou esse objeto

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_status(self): #método para os objetos
        self._ativo = not self._ativo


jogo_xadrez = Jogos('best Chess Set Ever', 'Estratégia Abstrata')
jogo_xadrez.alternar_status()
jogo_santorini = Jogos('santorini', 'Educativo')

Jogos.listar_jogos()


# Informações teóricas:
# __init__ : vai construir um método construtor. Sempre que criar a instância de um objeto, esse método é chamado. Usado sempre que quer garantir que quando tiver a instância daquela classe, sempre que tiver objeto, quero ter aqueles valores definidos. 
# self: cada jogo tem suas próprias informações. Referência da instância atua lque estamos usando no momento. 
# Médoto especial: __str__: mostrar método em formato de texto. Sempre que criar um métodoqual objeto que quero referenciar? 
# Método especial tem esses dois __ nome do metodo __
# Podemos criar nossos próprios métodos como o listar_jogos
# @property: pegar um atributo, e modificar como ele será lido. 
# método da classe: cls convenção - indicar o tipo do metodo