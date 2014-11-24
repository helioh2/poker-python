'''
Created on 24/11/2014

@author: helio
'''
import unittest
from poker.poker import poker, rank_mao
from poker.dados import straight_flush2, quadra1, full_house1


class Test(unittest.TestCase):


    def testPoker(self):
        self.assertEqual(poker([straight_flush2, quadra1]), straight_flush2)
        self.assertEqual(poker([full_house1, quadra1]), quadra1)
        self.assertEqual(poker([straight_flush2, full_house1]), straight_flush2)
        #self.assertEqual(poker([straight_flush2, straight_flush2]), None)
        
    def testRank_mao(self):
        self.assertEqual(rank_mao(straight_flush2), 9)
        self.assertEqual(rank_mao(quadra1), 8)
        self.assertEqual(rank_mao(full_house1), 7)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPoker']
    unittest.main()