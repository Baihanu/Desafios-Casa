def somar(a: float, b: float) -> float:
    """Retorna a soma entre dois números."""
    ...

def subtrair(a: float, b: float) -> float:
    """Retorna a subtração entre dois números."""
    ...

def multiplicar(a: float, b: float) -> float:
    """Retorna a multiplicação entre dois números."""
    ...

def dividir(a: float, b: float) -> float | None:
    """Retorna a divisão entre dois números. Se b = 0, retorna None."""
    ...


def test_calculadora():
    """
    Testa as operações básicas da calculadora.
    """
    assert somar(2, 3) == 5
    assert subtrair(5, 2) == 3
    assert multiplicar(2, 4) == 8
    assert dividir(10, 2) == 5
    assert dividir(10, 0) is None
