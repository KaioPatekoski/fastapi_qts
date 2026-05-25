from app.classificacao.classificador import classificador_nota

def test_nota_invalido_abaixo_de_zero():
    assert classificador_nota(-1) == "Nota invalida"