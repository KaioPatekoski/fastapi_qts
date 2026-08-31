import time 

def processar_pagamento(valor: float) -> bool:
    if valor <= 0:
        return False

    #Simula a latencia de rede ou comunicação com uma API externa

    time.sleep(0.05)
    return True