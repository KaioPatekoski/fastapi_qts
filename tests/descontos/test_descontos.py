from app.descontos.desconto import calcular_desconto

def test_valor_invalido():
    assert calcular_desconto(-10, True) == 0

def test_cliente_vip_valor_invalido():
    assert calcular_desconto(0, True) == 0

def test_valor_zero():
    assert calcular_desconto(0, True) == 0

def test_valor_positivo_decimal():
    assert calcular_desconto
    round(0.10, True) == 0.8

def test_valor_alto():
    assert calcular_desconto(200, True) == 160

def test_valor_valido_cliente_nao_vip():
    assert calcular_desconto(100, False) == 90

def test_valor_valido_cliente_vip():
    assert calcular_desconto(100, True) == 80