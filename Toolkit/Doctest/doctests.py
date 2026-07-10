# Conceito de adicionar testes já na documentação da função. (permite embutir exemplos de codigo executaveis diretamente na documentação, "documetação viva")

def soma(x, y):
    """ soma dois números

    >>> soma(10,70)
    80
    """

    assert isinstance(x, (int, float)), "O primeiro argumento deve ser um número"
    assert isinstance(y, (int, float)), "O segundo argumento deve ser um número"
    return x + y

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Então se o codigo estiver correto, não vai mostrar nada, mas se tiver algum erro o python vai avisar imediatamente no terminal, mostrando um relatório detalhado do erro.