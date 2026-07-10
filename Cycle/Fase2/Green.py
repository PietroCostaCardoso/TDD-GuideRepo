# Nessa parte aqui você escreve o código mais simples possível para fazer o teste passar (ficar verde).

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, preco):
        self.itens.append(preco)  

    def calcular_total(self):
        return sum(self.itens)
    

# Se agora você rodar o pytest agora, o teste vai passar e portanto ficar 'green'. Só que ainda falta o refactor.

# então agora você vai refatorar o código, ou seja, melhorar a estrutura do código sem mudar o comportamento. Por exemplo,nesse que fizemos anteriormente, a classe Carrinho está funcionando, mas não está muito bem estruturada. Então vamos refatorar para melhorar a estrutura do código.
 
 #class Carrinho:
   # def __init__(self):
        #self.itens = []

    #def adicionar_item(self, nome, preco):
        #self.itens.append({"nome": nome, "preco": preco})

    #def calcular_total(self):
        #return sum(item["preco"] for item in self.itens)