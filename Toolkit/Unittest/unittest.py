# É o framework de testes integrado à biblioteca padrão da linguagem python. Com ele, você automatiza a verificação do seu codigo através de um estrutura de testes.
  # Estrutura: Import unittest, função que você quer testar. e Classe de teste que herda as ferramentas do unittest.TestCase

import unittest

def fazer_suco(fruta):
    if fruta == "laranja":
        return "Suco de Laranja"
    return "Água"

class TesteDaFabrica(unittest.TestCase):

    def test_deve_fazer_suco_de_laranja(self):
        resultado = fazer_suco("laranja")
        self.assertEqual(resultado, "Suco de Laranja")

    def test_deve_retornar_agua_se_nao_for_laranja(self):
        resultado = fazer_suco("maçã")
        self.assertEqual(resultado, "Água")

if __name__ == '__main__':
    unittest.main()


# Portanto se der certo o terminal mostra pontos (..) e diz OK, mas caso der errado, ele mostra um F e um relatório detalhado do erro.