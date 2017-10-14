# -*- coding:utf-8 -*-

"""
Regras do FizzBuzz

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio nº
"""

import unittest

def fizzbuzz(numero):
    retorno = ''

    if numero % 3 == 0:
        retorno = 'fizz'

    if numero % 5 == 0:
        retorno += 'buzz'

    if not retorno:
        retorno = str(numero)

    return retorno

class FizzBuzzTest(unittest.TestCase):

    def test_1_return_1(self):
        self.assertEqual(fizzbuzz(1), '1')

    def test_2_return_2(self):
        self.assertEqual(fizzbuzz(2), '2')

    def test_4_return_4(self):
        self.assertEqual(fizzbuzz(4), '4')

    def test_7_return_7(self):
        self.assertEqual(fizzbuzz(7), '7')

    def test_3_return_fizz(self):
        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_6_return_fizz(self):
        self.assertEqual(fizzbuzz(6), 'fizz')

    def test_9_return_fizz(self):
        self.assertEqual(fizzbuzz(9), 'fizz')

    def test_12_return_fizz(self):
        self.assertEqual(fizzbuzz(12), 'fizz')

    def test_5_return_buzz(self):
        self.assertEqual(fizzbuzz(5), 'buzz')

    def test_10_return_buzz(self):
        self.assertEqual(fizzbuzz(10), 'buzz')

    def test_20_return_buzz(self):
        self.assertEqual(fizzbuzz(20), 'buzz')

    def test_25_return_buzz(self):
        self.assertEqual(fizzbuzz(25), 'buzz')

    def test_15_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')

    def test_30_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(30), 'fizzbuzz')

    def test_45_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(45), 'fizzbuzz')

    def test_60_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(60), 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()
