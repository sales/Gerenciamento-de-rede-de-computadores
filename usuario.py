#encoding: utf-8

from datetime import datetime
from conexao import Conexao
from impressora import ErroConexao

class Usuario(object):
    
    def __init__(self, nome_de_guerra, senha):
        self.nome_de_guerra = nome_de_guerra
        self.senha = senha
        self.esta_conectado = False

    def conectar(self):
        data = "%d/%d/%d" %(datetime.today().day, datetime.today().month, datetime.today().year)
        hora = "%d:%d" %(datetime.today().hour, datetime.today().minute)
        self.conexao = Conexao(self.nome_de_guerra, data=data, hora_inicio=hora)
        self.esta_conectado = True
    
    def enviar_arquivo(self, arquivo_enviado, copias):
        if self.esta_conectado == False:
            raise ErroConexao('Usuário não conectado!')
        else:
            if arquivo_enviado.nome in self.conexao.arquivos_enviados.keys():
                self.conexao.arquivos_enviados[arquivo_enviado.nome] += copias
            else:
                self.conexao.arquivos_enviados.update({arquivo_enviado.nome: copias})
