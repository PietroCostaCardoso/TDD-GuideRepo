# O Coverage serve para verificar se você esqueceu de testar alguma parte do código.

import unittest

# O que vai ser testado
def acesso (usuario_cadastrado: bool) -> str:
    if usuario_cadastrado:
        return "Bem vindo!"
    else:
        return "Acesso Negado"


#  O teste que vai esquecer
class TesteAcesso(unittest.TestCase):

    def test(self):
        resultado = acesso(usuario_cadastrado=True)
        self.assertEqual(resultado, "Bem vindo!")


if __name__ == '__main__':
    unittest.main()

# então, geralmente nós só testamos o que acontece quando o usuário é cadastrado. Esquecemos completamente de testar o False e o coverage vai mostrar a parte que não foi testada. 
