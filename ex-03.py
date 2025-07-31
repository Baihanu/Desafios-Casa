def contar_ate_dez() -> list[int]:
    """
    Retorna uma lista com os números de 1 até 10.

    Retorna:
    - list[int]: lista com os números de 1 a 10
    """
    ...


def test_contar_ate_dez():
    """
    Testa se a função contar_ate_dez retorna corretamente a sequência de 1 a 10.
    """
    assert contar_ate_dez() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
