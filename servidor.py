from microcomputador import Microcomputador

class Servidor(Microcomputador):

    servidores = []
    
    def __init__(self, codigo_implementacao, descricao, capacidade_do_hd, quantidade_de_ram, estacao, quantidade_maxima_de_buffer):
        Microcomputador.__init__(self, codigo_implementacao, descricao, capacidade_do_hd, quantidade_de_ram, estacao)
        self.quantidade_maxima_de_buffer = quantidade_maxima_de_buffer
        self.impressoras_conectadas = 0
        Servidor.adicionar_servidor(self)

    @staticmethod
    def adicionar_servidor(servidor):
        Servidor.servidores.append(servidor)
