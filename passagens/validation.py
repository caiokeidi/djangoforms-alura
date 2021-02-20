
def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não devem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum caractere numérico no campo"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números nesse campo.'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """ Verifica se data de ida é maior que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor que data de volta'

def data_ida_menor_que_data_pesquisa(data_ida, data_pesquisa, lista_de_erros):
    """Verifica se a data de ida é menor que data de pesquisa"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de Ida não pode ser inferior a data de hoje.'

