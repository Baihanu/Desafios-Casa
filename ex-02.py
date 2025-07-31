def par_ou_impar(n: int) -> str:
    """
    Determina se um número é par ou ímpar.

    Parâmetros:
    - n (int): número a ser verificado

    Retorna:
    - str: "par" se for par, "ímpar" se for ímpar
    """
    ...


def test_par_ou_impar():
    """
    Testa a função par_ou_impar com diferentes casos de entrada.
    """
    assert par_ou_impar(2) == "par"
    assert par_ou_impar(3) == "ímpar"
    assert par_ou_impar(0) == "par"
