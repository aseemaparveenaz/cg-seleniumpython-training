import unittest

class Example(unittest.TestCase):

    @classmethod
    def setUpClass(class_name):
        print("setUpClass executed")
    def setUp(self):
        print("setUp executed")
    def test_1(self):
        print("test-1 executed")
    def test_2(self):
        print("test-2 executed")
    def tearDown(self):
        print("tearDown executed")

    @classmethod
    def tearDownClass(class_name):
        print("tearDownClass executed")

