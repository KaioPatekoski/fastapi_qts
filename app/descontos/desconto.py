def calcular_desconto(valor, cliente_vip):
    if valor <= 0:
        return 0
    if cliente_vip == True:
        return valor - valor * 0.2
    if cliente_vip == False:
        return valor - valor * 0.1
    return "Valor invalido"