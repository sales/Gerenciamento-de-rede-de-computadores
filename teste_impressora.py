import unittest
from should_dsl import should
from impressora import Impressora, ErroConexao
from servidor import Servidor

class TestImpressora(unittest.TestCase):

    def setUp(self):
        Servidor.servidores = []

    def teste_deve_criar_uma_impressora(self):
        impressora = Impressora(10, 'impressora', 100)
        impressora.codigo_patrimonio |should| equal_to(10)
        impressora.descricao |should| equal_to('impressora')
        impressora.velocidade |should| equal_to(100)

    def teste_conectar_ao_servidor(self):
        servidor = Servidor(codigo_implementacao=10, descricao='oi', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1, quantidade_maxima_de_buffer=10)
        impressora1 = Impressora(10, 'impressora', 100)
        impressora1.conectar_ao_servidor()
        servidor.impressoras_conectadas |should| equal_to(1)

    def teste_conectar_multiplas_impressoras_no_mesmo_servidor(self):
        servidor = Servidor(codigo_implementacao=10, descricao='oi', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1, quantidade_maxima_de_buffer=10)
        impressora1 = Impressora(10, 'impressora', 100)
        impressora2 = Impressora(10, 'impressora', 100)
        impressora3 = Impressora(10, 'impressora', 100)
        impressora4 = Impressora(10, 'impressora', 100)
        impressora1.conectar_ao_servidor()
        impressora2.conectar_ao_servidor()
        impressora3.conectar_ao_servidor()
        impressora4.conectar_ao_servidor |should| throw(ErroConexao)
        servidor.impressoras_conectadas |should| equal_to(3)

    def teste_conectar_multiplas_impressoras_em_multiplos_servidores(self):
        servidor = Servidor(codigo_implementacao=10, descricao='oi', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1, quantidade_maxima_de_buffer=10)
        servidor2 = Servidor(codigo_implementacao=10, descricao='oi', capacidade_do_hd=5, quantidade_de_ram=8, estacao=1, quantidade_maxima_de_buffer=10)
        impressora1 = Impressora(10, 'impressora', 100)
        impressora2 = Impressora(10, 'impressora', 100)
        impressora3 = Impressora(10, 'impressora', 100)
        impressora4 = Impressora(10, 'impressora', 100)
        impressora5 = Impressora(10, 'impressora', 100)
        impressora6 = Impressora(10, 'impressora', 100)
        impressora1.conectar_ao_servidor()
        impressora2.conectar_ao_servidor()
        impressora3.conectar_ao_servidor()
        impressora4.conectar_ao_servidor()
        impressora5.conectar_ao_servidor()
        impressora6.conectar_ao_servidor()
        servidor.impressoras_conectadas |should| equal_to(3)
        servidor.impressoras_conectadas |should| equal_to(3)

if __name__ == "__main__":
    unittest.main()

