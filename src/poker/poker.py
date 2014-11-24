
''' Funcao poker e auxiliares '''


def rank_mao(mao):
    '''
    Mao -> Natural[1,9]
    Retorna o rank da mao de acordo com as regras do poker
    Por exemplo: straight_flush retorna 9, quadra retorna 8,
    e assim por diante.
    '''
    pass

def poker(maos):
    '''
    ListaDeMao -> Mao
    Retorna mao mais forte (com maior rank)
    '''
    return max(maos, key=rank_mao)