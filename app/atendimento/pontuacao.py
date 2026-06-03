def calcular_pontuacao_atendimento(tempo_minuto, resolvido_primeiro_contato, reincidencia):
    if tempo_minuto <= 0:
        return 0
    
    if resolvido_primeiro_contato and tempo_minuto <= 10: 
        base = 10

    if resolvido_primeiro_contato and  11 <= tempo_minuto <= 20: 
        base = 8

    if resolvido_primeiro_contato and tempo_minuto > 20:
        base = 6
    
    if resolvido_primeiro_contato == False and tempo_minuto <= 10: 
        base = 5

    if resolvido_primeiro_contato == False and  11 <= tempo_minuto <= 20: 
        base = 3

    if resolvido_primeiro_contato == False and tempo_minuto > 20:
        base = 1

    if reincidencia:
        base -= 2

    return base

def classificar_atendimento(pontuacao):
    if pontuacao >= 9:
        return "Excelente"
    
    if pontuacao >= 7:
        return "Bom"
    
    if pontuacao >= 4:
        return "Regular"
    
    return "Critico"