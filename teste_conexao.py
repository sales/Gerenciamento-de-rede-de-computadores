import unittest
from should_dsl import should
from usuario import Usuario
from conexao import Conexao

class TestConexao(unittest.TestCase):
    
    def teste_deve_criar_uma_conexao(self):
        usuario = Usuario(nome_de_guerra='@usuario', senha='senha')
        usuario.conectar()
        usuario.esta_conectado |should| equal_to(True) 

if __name__ == "__main__":
    unittest.main()
