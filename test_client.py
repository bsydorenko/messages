#!/usr/local/bin/python3
import unittest
from client import client, p


class TestDefaultPostGet(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_post0(self):
		self.assertEqual(client(2000, False, 'test0', None), '[done]')

	def test_post1(self):
		self.assertEqual(client(2000, False, 'test1', None), '[done]')

	def test_post2(self):
		self.assertEqual(client(2000, False, 'test2', None), '[done]')

	def test_zget0(self):
		self.assertEqual(client(2000, True, None, None), 'test2\n[done]')

	def test_zget1(self):
		self.assertEqual(client(2000, True, None, None), 'test1\n[done]')

	def test_zget2(self):
		self.assertEqual(client(2000, True, None, None), 'test0\n[done]')

class TestNamedQueue(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_post1(self):
		self.assertEqual(client(2000, False, 'test1', '1'), '[done]')

	def test_post11(self):
		self.assertEqual(client(2000, False, 'test11', '11'), '[done]')

	def test_post111(self):
		self.assertEqual(client(2000, False, 'test111', '111'), '[done]')

	def test_post1111(self):
		self.assertEqual(client(2000, False, 'test1111', '1111'), '[done]')

	def test_post9999(self):
		self.assertEqual(client(2000, False, 'test9999', '9999'), '[done]')

	def test_post10000(self):
		self.assertEqual(client(2000, False, 'test10000', '10000'), '[done]')


	def test_zget1(self):
		self.assertEqual(client(2000, True, None, '1'), 'test1\n[done]')

	def test_zget11(self):
		self.assertEqual(client(2000, True, None, '11'), 'test11\n[done]')

	def test_zget111(self):
		self.assertEqual(client(2000, True, None, '111'), 'test111\n[done]')

	def test_zget1111(self):
		self.assertEqual(client(2000, True, None, '1111'), 'test1111\n[done]')

	def test_zget9999(self):
		self.assertEqual(client(2000, True, None, '9999'), 'test9999\n[done]')

	def test_zget10000(self):
		self.assertEqual(client(2000, True, None, '10000'), 'test10000\n[done]')

class Test_ascii_input_output(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_ascii_post(self):
		x = ''.join([chr(i) for i in range(32,126)])
		self.assertEqual(client(2000, False, x, None), '[done]')

	def test_ascii_zget(self):
		x = ''.join([chr(i) for i in range(32,126)])
		self.assertEqual(client(2000, True, None, None), x+'\n[done]')

class Test_z100_limit(unittest.TestCase):
	def setUp(self):
		for i in range(100):
			client(2000, False, str(i), None)

	def tearDown(self):
		for i in range(99):
			client(2000, True, None, None)

	def test_post_over_100(self):
		self.assertEqual(client(2000, False, '101', None), '')

	def test_get_over_100(self):
		self.assertTrue(client(2000, True, None, None) != '101')


class Test_zHelp_tests(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_help0(self):
		self.assertEqual(client(2000), p.print_help())

	def test_help1_wrong_queue(self):
		self.assertEqual(client(2000, False, 'test', '10001'), p.print_help())
		self.assertTrue(client(2000, True, None, '10001') != 'test')

	def test_help2_post_exception(self):
		self.assertEqual(client(2000, False, 'test|||test', None), p.print_help())



if __name__ == '__main__':
	unittest.main()