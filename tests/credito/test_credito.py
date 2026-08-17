import pytest

from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 1, True, "renda invalida"),
        (0, -1, True, "renda invalida"),
        (1, -1, False, "score invalido"),
        (1, 1500, False, "score invalido"),
        (1, 500, True, "reprovado"),
        (1, 200, False, "reprovado"),
        (1, 500, False, "aprovado padrao"),
        (1, 800, False, "aprovado premium")
    ]
)
def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 1, True, "renda invalida"),
        (0.01, 1, True, "reprovado"),
        (1, 0, False, "reprovado"),
        (1, -1, False, "score invalido"),
        (1, 399, False, "reprovado"),
        (1, 400, False, "aprovado padrao"),
        (1, 699, False, "aprovado padrao"),
        (1, 700, False, "aprovado premium"),
        (1, 1000, False, "aprovado premium"),
        (1, 1001, False, "score invalido"),
    ]
)
def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado


