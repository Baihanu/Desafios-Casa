def is_palindromo(palavra: str) -> bool:
    """
    Verifica se uma palavra é um palíndromo (lida igual de trás para frente).

    Parâmetros:
    - palavra (str): palavra a ser verificada

    Retorna:
    - bool: True se for palíndromo, False caso contrário
    """
    ...


def test_is_palindromo():
    """
    Testa a função is_palindromo com palavras palíndromas e não palíndromas.
    """
    assert is_palindromo("arara") is True
    assert is_palindromo("Ana") is True
    assert is_palindromo("Python") is False
