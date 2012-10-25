import unittest
from should_dsl import should
from microcomputador import Microcomputador

class TestMicrocomputador(unittest.TestCase):

    def teste_deve_criar_um_microcomputador(self):
        micro = Microcomputador(codigo_implementacao=9, descricao='oi', capacidade_do_hd=500, quantidade_de_ram=2, estacao=1)
        micro.codigo_implementacao |should| equal_to(9)
        micro.descricao |should| equal_to('oi')
        micro.capacidade_do_hd |should| equal_to(500)
        micro.quantidade_de_ram |should| equal_to(2)
        micro.estacao |should| equal_to(1)


if __name__ == "__main__":
    unittest.main()
