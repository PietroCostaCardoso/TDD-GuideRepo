# Ferramenta usada para verificar se uma condição é verdadeira no seu código. Se a condição for verdadeira, o programa continua rodando normalmente. Se for falsa, o programa para imediatamente e joga um erro.
# exemplo:
 
def soma (x,y):
    assert isinstance(x, (int, float)), "O primeiro argumento deve ser um número"
    assert isinstance(y, (int, float)), "O segundo argumento deve ser um número"
    return x + y   

print(soma(10, 5))    
print(soma(40, 5))  

#então tipo aqui se der erro em alguma dessas linhas vai mostrar que o primeiro ou segundo argumento devem ser numeros 
