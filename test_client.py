#!/usr/local/bin/python3
import unittest
from client import client, p


class TestClient(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test0(self):
        self.assertEqual(client(2000, False, 'some0', '1'), '[done]')

    def test1(self):
        self.assertEqual(client(2000, False, 'some0', None), '[done]')

    def test2(self):
        self.assertEqual(client(2000, True, None, None), 'some0\n'
                                                         '[done]')

    def test3(self):
        self.assertEqual(client(2000), p.print_help())

    def test4(self):
        self.assertEqual(client(2000, True, False, 200000), p.print_help())



if __name__ == '__main__':
    unittest.main()
