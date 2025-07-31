def tabuada(n: int) -> list[int]:
    """
    Gera a tabuada de um número de 1 a 10.

    Parâmetros:
    - n (int): número para gerar a tabuada

    Retorna:
    - list[int]: lista com os resultados da multiplicação de n por 1 a 10
    """
    ...


def test_tabuada():
    """
    Testa se a função tabuada retorna os múltiplos corretos de 1 a 10.
    """
    assert tabuada(2) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert tabuada(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
