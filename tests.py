from unittest import TestCase
import unittest
from main import *


class RateTests(TestCase):

    def test_matching_orphelins(self):
        rate = Rate(RateType.Orphelins, None)
        self.assertTrue(rate.is_matching_number(1))
        self.assertTrue(rate.is_matching_number(14))
        self.assertTrue(rate.is_matching_number(9))
        self.assertTrue(rate.is_matching_number(17))
        self.assertTrue(rate.is_matching_number(6))

        self.assertFalse(rate.is_matching_number(25))
        self.assertFalse(rate.is_matching_number(32))
        self.assertFalse(rate.is_matching_number(33))
        self.assertFalse(rate.is_matching_number(27))

    def test_matching_tier(self):
        rate = Rate(RateType.Tier, None)
        self.assertTrue(rate.is_matching_number(33))
        self.assertTrue(rate.is_matching_number(27))
        self.assertTrue(rate.is_matching_number(8))

        self.assertFalse(rate.is_matching_number(0))
        self.assertFalse(rate.is_matching_number(6))
        self.assertFalse(rate.is_matching_number(1))

    def test_matching_voisins_de_zero(self):
        rate = Rate(RateType.VoisinsDeZero, None)
        self.assertTrue(rate.is_matching_number(25))
        self.assertTrue(rate.is_matching_number(22))
        self.assertTrue(rate.is_matching_number(0))

        self.assertFalse(rate.is_matching_number(17))
        self.assertFalse(rate.is_matching_number(9))
        self.assertFalse(rate.is_matching_number(10))

    def test_matching_parity(self):
        rate = Rate(RateType.Parity, 1)
        self.assertTrue(rate.is_matching_number(25))
        self.assertTrue(rate.is_matching_number(23))
        self.assertTrue(rate.is_matching_number(1))

        self.assertFalse(rate.is_matching_number(16))
        self.assertFalse(rate.is_matching_number(0))
        self.assertFalse(rate.is_matching_number(10))

        rate = Rate(RateType.Parity, 0)
        self.assertFalse(rate.is_matching_number(25))
        self.assertFalse(rate.is_matching_number(23))
        self.assertFalse(rate.is_matching_number(1))

        self.assertTrue(rate.is_matching_number(16))
        self.assertTrue(rate.is_matching_number(0))
        self.assertTrue(rate.is_matching_number(10))

    def test_matching_color(self):
        rate = Rate(RateType.Color, 'R')
        self.assertTrue(rate.is_matching_number(32))
        self.assertTrue(rate.is_matching_number(5))
        self.assertTrue(rate.is_matching_number(14))

        self.assertFalse(rate.is_matching_number(15))
        self.assertFalse(rate.is_matching_number(0))
        self.assertFalse(rate.is_matching_number(4))

        rate = Rate(RateType.Color, 'B')
        self.assertTrue(rate.is_matching_number(28))
        self.assertTrue(rate.is_matching_number(20))
        self.assertTrue(rate.is_matching_number(11))

        self.assertFalse(rate.is_matching_number(3))
        self.assertFalse(rate.is_matching_number(0))
        self.assertFalse(rate.is_matching_number(12))

        rate = Rate(RateType.Color, 'G')
        self.assertTrue(rate.is_matching_number(0))


        self.assertFalse(rate.is_matching_number(1))
        self.assertFalse(rate.is_matching_number(2))
        self.assertFalse(rate.is_matching_number(3))

class GameRoundTests(TestCase):
    def test_1(self):
        rates = [Rate(RateType.Orphelins, None), Rate(RateType.Color, 'G'), 
                 Rate(RateType.Tier, None), Rate(RateType.Parity, 1), Rate(RateType.Parity, 0)]
        results = GameRound(rates, DetermenisticRandomizer(0)).get_round_result()
        self.assertListEqual(results.is_winner, [False, True, False, False, True])
        self.assertEqual(results.result_number, 0)

    def test_2(self):
        rates = [Rate(RateType.Orphelins, None), Rate(RateType.Color, 'G'), 
                 Rate(RateType.Tier, None), Rate(RateType.Parity, 1), 
                 Rate(RateType.Parity, 0), Rate(RateType.Color, 'R'), Rate(RateType.Color, 'B')]
        results = GameRound(rates, DetermenisticRandomizer(14)).get_round_result()
        self.assertListEqual(results.is_winner, [True, False, False, False, True, True, False])
        self.assertEqual(results.result_number, 14)

    def test_3(self):
        class Randomizer:
            lst: List[int]
            def __init__(self) -> None:
                self.lst = [0, 32, 15, 19, 4, 21, 2, 25]
                self.lst += [22,18, 29, 7, 28, 12, 35, 3, 26]
            def get_number(self) -> int:
                return random.choice(self.lst)
            
        rates = [Rate(RateType.VoisinsDeZero, None)]
        for i in range(100):
            self.assertEqual(GameRound(rates, Randomizer()).get_round_result().is_winner, [True]) 

unittest.main()
