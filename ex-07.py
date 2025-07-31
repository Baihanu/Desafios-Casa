def tentar_adivinhar(chute: int, segredo: int) -> str:
    """
    Compara o chute do jogador com o número secreto.

    Parâmetros:
    - chute (int): número fornecido pelo jogador
    - segredo (int): número secreto definido

    Retorna:
    - str: mensagem indicando se o chute está 'baixo', 'alto' ou 'acertou'
    """
    ...


def test_tentar_adivinhar():
    """
    Testa a resposta da função ao comparar o chute com o número secreto.
    """
    assert tentar_adivinhar(30, 50) == "Muito baixo!"
    assert tentar_adivinhar(80, 50) == "Muito alto!"
    assert tentar_adivinhar(50, 50) == "Parabéns! Você acertou!"
