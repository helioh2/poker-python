'''
Created on 24/11/2014

@author: helio
'''


'''
Carta eh Carta(Natural[2,14], {"C","E","O","P"})
'''
class Carta(object):
    
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe     

'''Exemplos'''
dez_copas = Carta(10,"C")
valete_copas = Carta(11, "C")


'''INICIO Funcoes auxiliares para testes'''

def string_to_mao(str):
    ''' String -> Mao
     Exemplo: "8C 9C DC JC QC" -> [Carta(8,"C"), Carta(9, "C"), Carta(10, "C")
         Carta(11, "C"), Carta(12, "C")]
     '''
    return [Carta(char_to_valor(k[0]),k[1]) for k in str.split()]

def char_to_valor(char):
    return "--23456789DJQKA".index(char)

#print char_to_valor("D")

#straight_flush2 = "8C 9C DC JC QC"

def print_carta(carta):
    for c in carta:
        print "Valor= "+str(c.valor)+" Naipe= "+c.naipe
        
#print_carta(string_to_mao(straight_flush2))

'''FIM Funcoes auxiliares para testes'''


''' 
Mao eh lista de Carta
'''
'''Exemplos'''
straight_flush1 = [dez_copas, valete_copas, Carta(12, "C"), 
                   Carta(13, "C"), Carta(14, "C")]
straight_flush2 = string_to_mao("8C 9C DC JC QC")
quadra1 = string_to_mao("4E 4C 4P 4O 6C")
full_house1 = string_to_mao("KE KC KP DC DP")

