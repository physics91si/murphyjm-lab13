#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import unittest
import calc

class CalcTest(unittest.TestCase):
    # TODO implement tests here to verify that your functions work!
    # TODO: def testSyntax(self):

    def testAddition(self):
        self.assertEqual(calc.calc('1+1'), 2)

    def testFloats(self):
        self.assertEqual(calc.calc('2.5+1.4'), 3.9)

    def testMultiDigit(self):
        self.assertEqual(calc.calc('15+512'), 527)

    def testSubtraction(self):
        self.assertEqual(calc.calc('3-1'), 2)

    def testNegativeSum(self):
        self.assertEqual(calc.calc('3-4', -1))

    def testMultiplciation(self):
        self.assertEqual(calc.calc('2*4'), 8)
 
    def testDivision(self):
        self.assertEqual(calc.calc('6/3'), 2)

if __name__ == '__main__':
    unittest.main()

