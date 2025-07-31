def ordenar_nomes(nomes: list[str]) -> list[str]:
    """
    Ordena uma lista de nomes em ordem alfabética.

    Parâmetros:
    - nomes (list[str]): lista de nomes

    Retorna:
    - list[str]: lista ordenada alfabeticamente
    """
    ...


def test_ordenar_nomes():
    """
    Testa se a função ordenar_nomes retorna a lista em ordem alfabética.
    """
    assert ordenar_nomes(["casa", "ana", "bruno", "zeca"]) == ["ana", "bruno", "casa", "zeca"]
    assert ordenar_nomes(["x", "a", "m"]) == ["a", "m", "x"]
