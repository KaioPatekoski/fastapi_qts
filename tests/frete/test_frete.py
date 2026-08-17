import pytest

from app.frete.frete import classificar_frete

@pytest.mark.parametrize(
    "peso_kg, regiao, premium, retorno_esperado",
    [
        (0,"local", True, "Invalido"),
        (-1,"estadual", False, "Invalido"),
        (5,"internacional", False, "Regiao invalida"),
        (2,"local", True, "Frete gratis"),
        (3,"local", False, "Frete reduzido"),
        (3,"estadual", False, "Frete padrão"),
        (3,"nacional", False, "Frete padrão")
    ]
)
def test_classificar_frete_caixa_preta(
    peso_kg, regiao, premium, retorno_esperado
):
    assert classificar_frete(peso_kg, regiao, premium) == retorno_esperado