#Nessa parte você escreve um teste para uma funcionalidade que ainda não existe e como o código não existe, o teste vai falhar (ficar vermelho).
 
import pytest
from Cycle.Fase2.Green import Carrinho

def test_deve_calcular_total_do_carrinho():
    carrinho = Carrinho()
    carrinho.adicionar_item("Camiseta", preco=50.0)
    carrinho.adicionar_item("Caneca", preco=30.0)
    
    assert carrinho.calcular_total() == 80.0

# Esse exemplo acima se você rodar ele, vai dar erro, porque a classe Carrinho e o método calcular_total não existem ainda. Então, você vai ter que criar a classe e o método para que o teste passe (ficar verde).