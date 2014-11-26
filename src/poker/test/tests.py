'''
Created on 24/11/2014

@author: helio
'''
import unittest
from poker.poker import poker, rank_mao, straigth
from poker.dados import straight_flush2, quadra1, full_house1, flush1, straigh1,\
    um_par1, doi_pares1, trinca1, carta_alta1


class Test(unittest.TestCase):


    def testPoker(self):
        self.assertEqual(poker([straight_flush2, quadra1]), straight_flush2)
        self.assertEqual(poker([full_house1, quadra1]), quadra1)
        self.assertEqual(poker([straight_flush2, full_house1]), straight_flush2)
        #self.assertEqual(poker([straight_flush2, straight_flush2]), None)
        
        self.assertEqual(poker[(flush1, straigh1)], flush1)
        self.assertEqual(poker[(straigh1, um_par1)], straigh1)
        self.assertEqual(poker[(trinca1, doi_pares1)], trinca1)
        self.assertEqual(poker[(um_par1, doi_pares1)], doi_pares1)
        self.assertEqual(poker[(doi_pares1, flush1)], flush1)
        self.assertEqual(poker[(carta_alta1, um_par1)], um_par1)
        self.assertEqual(poker[(um_par1, carta_alta1)], um_par1)
        self.assertEqual(poker[(straight_flush2, trinca1)], straight_flush2)
        self.assertEqual(poker[(straight_flush2, carta_alta1)], straight_flush2)
         
    def testRank_mao(self):
        self.assertEqual(rank_mao(straight_flush2), 9)
        self.assertEqual(rank_mao(quadra1), 8)
        self.assertEqual(rank_mao(full_house1), 7)
        
    def testStraigth(self):
        self.assertEqual(straigth([12,11,10,9,8]), True)
        self.assertEqual(straigth([12,11,11,9,8]), False)
        self.assertEqual(straigth([4,4,4,4,6]), False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPoker']
    unittest.main()