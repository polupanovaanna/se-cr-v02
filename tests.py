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

unittest.main()
