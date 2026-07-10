# Type hints: permite que você declare explicitamente qual é o tipo de dado esperado para variaveis, parametros de funções e retornos.

#Em baixo mostrarei um exemplo sendo que um vai ter e outro não, e você vai ver a diferença.

#1º exemplo sem type hints:
def Calcular_desconto (preco, desconto):
    return preco - (preco * desconto)

#2º exemplo com type hints:
def Calcular_desconto (preco: float, desconto: float) -> float:
    return preco - (preco * desconto)