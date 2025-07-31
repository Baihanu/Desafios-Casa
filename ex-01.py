def soma(a: int, b: int) -> int:
    """
    Soma dois números inteiros.

    Parâmetros:
    - a (int): primeiro número
    - b (int): segundo número

    Retorna:
    - int: a soma de a + b
    """
    ...
  


def test_soma():
    """
    Testa se a função soma retorna o valor correto ao somar dois inteiros.
    """
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
