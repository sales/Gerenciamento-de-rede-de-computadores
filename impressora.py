# encoding: utf-8

from servidor import Servidor

class Impressora(object):

    def __init__(self, codigo_patrimonio, descricao, velocidade):
        self.codigo_patrimonio = codigo_patrimonio
        self.descricao = descricao
        self.velocidade = velocidade
        self.fila_de_impressao = []

    def conectar_ao_servidor(self):
        for servidor in Servidor.servidores:
            if servidor.impressoras_conectadas < 3:
                servidor.impressoras_conectadas += 1
                break
        else:
            raise ErroConexao('Não há servidores disponíveis!')

class ErroConexao(Exception):
    pass
