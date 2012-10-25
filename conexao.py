class Conexao(object):

    conexoes = []

    def __init__(self, nome, data, hora_inicio):
        self.nome = nome
        self.data = data
        self.hora_inicio = hora_inicio
        self.arquivos_enviados = {}

    @staticmethod
    def adicionar_conexao(conexao):
        Conexao.conexoes.append(conexao)
