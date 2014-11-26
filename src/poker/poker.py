
''' Funcao poker e auxiliares '''


def flush(mao):
    '''
    Mao -> Boolean
    Facam o codigo e os testes para flush (entrega dia 01/12)
    '''


def straigth(valores):
    '''
    ListaDeValor -> Boolean
    Retorna true se mao representa um straight 
    (cinco cartas com valores sequenciais)
    '''
    #valores = []
    #for carta in mao:
    #    valores.append(carta.valor)
    
    # EXEMPLOS valores = seq=[12,11,10,9,8] ; nao-seq=[12,11,11,9,8]; nao-seq2=[12,10,7,5,4]
  
#     valores.sort(reverse=True)    
#     for k in range(len(valores)-1):
#         if valores[k] - 1 != valores[k+1]:
#             return False
#     return True    ##ESTAH CERTO ASSIM TAMBEM
    return max(valores)-min(valores)==4 and len(set(valores)) == 5
       

def mesmo_valor(quant, mao):
    pass


def rank_mao(mao):
    '''
    Mao -> Natural[1,9]
    Retorna o rank da mao de acordo com as regras do poker
    Por exemplo: straight_flush retorna 9, quadra retorna 8,
    e assim por diante.
    '''
    valores = [carta.valor for carta in mao]  #extrair metodo
    if straigth(valores) and flush(mao):
        return 9
    elif mesmo_valor(4, mao):
        return 8
    elif mesmo_valor(3, mao) and mesmo_valor(2, mao):
        return 7
    else:
        return 0

def poker(maos):
    '''
    ListaDeMao -> Mao
    Retorna mao mais forte (com maior rank)
    '''
    return max(maos, key=rank_mao)