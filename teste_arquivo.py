import unittest
from should_dsl import should
from arquivo import Arquivo
from usuario import Usuario
from impressora import Impressora

class TestArquivo(unittest.TestCase):

    def teste_deve_criar_um_usuario(self):
        usuario = Usuario(nome_de_guerra='@usuario', senha='senha')
        usuario.nome_de_guerra |should| equal_to('@usuario')
        usuario.senha |should| equal_to('senha')

    def teste_deve_criar_uma_impressora(self):
        impressora = Impressora(10, 'impressora', 100)
        impressora.codigo_patrimonio |should| equal_to(10)
        impressora.descricao |should| equal_to('impressora')
        impressora.velocidade |should| equal_to(100)

    def teste_deve_criar_um_arquivo(self):
        usuario = Usuario(nome_de_guerra='@usuario', senha='senha')
        impressora = Impressora(10, 'impressora', 100)
        arquivo = Arquivo(nome='file', proprietario=usuario, impressora_destino=impressora)
        arquivo.nome |should| equal_to('file')
        arquivo.proprietario.nome_de_guerra |should| equal_to('@usuario')
        arquivo.impressora_destino.codigo_patrimonio |should| equal_to(10)

if __name__ == "__main__":
    unittest.main()

