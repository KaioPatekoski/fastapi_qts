def calcular_taxa_embalagem(levar_viagem: bool, quantidade_itens: int) -> float:
    """Calcula a taxa de embalagem com base na escolha do cliente."""
    if not  levar_viagem or quantidade_itens <= 0:
        return 0.0

    taxa_fixa = 2.00
    adocional_por_item = quantidade_itens * 0.50
    return round(taxa_fixa + adocional_por_item, 2)