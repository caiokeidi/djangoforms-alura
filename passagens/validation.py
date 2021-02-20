
def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não devem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum caractere numérico no campo"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números nesse campo.'


