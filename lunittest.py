#encoding: utf-8
'''了解，unittest
'''
import unittest

def success():
    return 1

def failure():
    return 0


class TestProduct(unittest.TestCase):

    def test_success(self):
        self.assertEqual(success(), 1)

    def test_failure(self):
        self.assertEqual(failure(), 0)


if __name__ == '__main__':
    unittest.main()
