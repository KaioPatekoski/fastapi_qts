import pytest
import time
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, retorno_esperado",
    [
        (0.0, "BASICO", 1, -1.0),
        (10.0, "BASICO", -1, -1.0),
        (10.0, "AVANCADO", 1, -2.0),
        (10.0, "", 1, -2.0),
        (100.0, "BASICO", 0, 100.0),
        (100.0, "PREMIUM", 0, 90.0),
        (100.0, "EMPRESARIAL", 0, 80.0),
    ],
)
def test_calcular_faturamento(valor_base, plano, dias_atraso, retorno_esperado):
    assert processar_cobranca(valor_base, plano, dias_atraso) == retorno_esperado

#BASICO
def test_tempo_processamento_cobranca_sem_atraso_BASICO():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "BASICO", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 100.0

def test_tempo_processamento_cobranca_com_atraso_1_a_30_dias_BASICO():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "BASICO", 1)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 105.5

def test_tempo_processamento_cobranca_com_atraso_mais_de_30_dias_BASICO():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "BASICO", 31)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 156.0

#PREMIUM
def test_tempo_processamento_cobranca_sem_atraso_PREMIUM():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "PREMIUM", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 90.0

def test_tempo_processamento_cobranca_com_atraso_1_a_30_dias_PREMIUM():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "PREMIUM", 1)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 95.45

def test_tempo_processamento_cobranca_com_atraso_mais_de_30_dias_PREMIUM():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "PREMIUM", 31)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 142.9

#EMPRESARIAL
def test_tempo_processamento_cobranca_sem_atraso_EMPRESARIAL():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "EMPRESARIAL", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 80.0

def test_tempo_processamento_cobranca_com_atraso_1_a_30_dias_EMPRESARIAL():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "EMPRESARIAL", 1)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 85.4

def test_tempo_processamento_cobranca_com_atraso_mais_de_30_dias_EMPRESARIAL():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "EMPRESARIAL", 31)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert tempo_decorrido >= 0.04
    assert tempo_decorrido < 0.1 
    
    assert resultado == 129.8
