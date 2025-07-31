def validar_cpf(cpf: str) -> bool:
    """
    Valida se um CPF brasileiro está correto com base nos dígitos verificadores.

    Parâmetros:
    - cpf (str): CPF em formato de string, com ou sem pontuação

    Retorna:
    - bool: True se for válido, False se inválido
    """
    ...


def test_validar_cpf():
    """
    Testa a função validar_cpf com CPFs válidos e inválidos.
    """
    assert validar_cpf("529.982.247-25") is True
    assert validar_cpf("123.456.789-00") is False
    assert validar_cpf("11111111111") is False
