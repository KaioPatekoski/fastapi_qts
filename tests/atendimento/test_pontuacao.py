from app.atendimento.pontuacao import calcular_pontuacao_atendimento, classificar_atendimento

def test_calculo_pontuacao_tempo_zero():
    assert calcular_pontuacao_atendimento(0, True, False) == 0

def test_calculo_pontuacao_tempo_negativo():
    assert calcular_pontuacao_atendimento(-3, True, False) == 0

def test_calculo_pontuacao_resolvido_ate_dez_minutos():
    assert calcular_pontuacao_atendimento(10, True, False) == 10

def test_calculo_pontuacao_resolvido_entre_onze_e_vinte_minutos():
    assert calcular_pontuacao_atendimento(11, True, False) == 8

def test_calculo_pontuacao_resolvido_acima_de_vinte_minutos_com_reincidencia():
    assert calcular_pontuacao_atendimento(21, True, True) == 4

def test_calculo_pontuacao_nao_resolvido_ate_dez_minutos():
    assert calcular_pontuacao_atendimento(10, False, False) == 5

def test_calculo_pontuacao_nao_resolvido_entre_onze_e_vinte_minutos_com_reincidencia():
    assert calcular_pontuacao_atendimento(15, False, True) == 1

def test_calculo_pontuacao_nao_resolvido_acima_de_vinte_minutos_com_reincidencia():
    assert calcular_pontuacao_atendimento(25, False, True) == -1

def test_classificacao_excelente():
    pontuacao = calcular_pontuacao_atendimento(10, True, False)
    assert classificar_atendimento(pontuacao) == "Excelente"

def test_classificacao_bom():
    pontuacao = calcular_pontuacao_atendimento(11, True, False)
    assert classificar_atendimento(pontuacao) == "Bom"

def test_classificacao_regular():
    pontuacao = calcular_pontuacao_atendimento(21, True, True)
    assert classificar_atendimento(pontuacao) == "Regular"

def test_classificacao_critico():
    pontuacao = calcular_pontuacao_atendimento(25, False, True)
    assert classificar_atendimento(pontuacao) == "Critico"