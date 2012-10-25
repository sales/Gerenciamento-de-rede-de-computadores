import unittest
from should_dsl import should
from usuario import Usuario
from conexao import Conexao
from arquivo import Arquivo
from impressora import Impressora
from servidor import Servidor

class TestUsuario(unittest.TestCase):

    def teste_deve_criar_um_usuario(self):
        usuario = Usuario(nome_de_guerra='@usuario', senha='senha')
        usuario.nome_de_guerra |should| equal_to('@usuario')
        usuario.senha |should| equal_to('senha')
        usuario.esta_conectado |should| equal_to(False)

    def teste_usuario_deve_se_conectar(self):
        usuario = Usuario(nome_de_guerra='@usuario', senha='senha')
        usuario.esta_conectado |should| equal_to(False)
        usuario.conectar()
        usuario.esta_conectado |should| equal_to(True)
        usuario.conexao |should| be_instance_of(Conexao)

    def teste_usuario_deve_enviar_arquivo(self):
        usuario = Usuario(nome_de_guerra='@usuario', senha='senha')
        servidor = Servidor(codigo_implementacao=10, descricao='oi', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1, quantidade_maxima_de_buffer=10)        
        impressora = Impressora(10, 'impressora', 100)
        impressora.conectar_ao_servidor()
        arquivo = Arquivo(nome='file', proprietario=usuario, impressora_destino=impressora)
        usuario.conectar()
        usuario.enviar_arquivo(arquivo, 1)
        usuario.conexao.arquivos_enviados |should| equal_to({arquivo.nome: 1})

    def teste_usuario_deve_enviar_duas_copias(self):
        usuario = Usuario(nome_de_guerra='@usuario', senha='senha')
        servidor = Servidor(codigo_implementacao=10, descricao='oi', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1, quantidade_maxima_de_buffer=10)        
        impressora = Impressora(10, 'impressora', 100)
        impressora.conectar_ao_servidor()
        arquivo = Arquivo(nome='file', proprietario=usuario, impressora_destino=impressora)
        usuario.conectar()
        usuario.enviar_arquivo(arquivo, 1)
        usuario.enviar_arquivo(arquivo, 1)
        usuario.conexao.arquivos_enviados |should| equal_to({arquivo.nome: 2})
        


if __name__ == "__main__":
    unittest.main()
