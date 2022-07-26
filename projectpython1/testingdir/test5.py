import unittest

class Example(unittest.TestCase):

    @classmethod
    def setUpClass(class_name):
        print("setUpClass executed")
    def setUp(self):
        print("setUp executed")
    def test_z(self):
        print("test-z executed")
    def test_b(self):
        print("test-b executed")
    def test_a(self):
        print("test-a executed")
    def tearDown(self):
        print("tearDown executed")

    @classmethod
    def tearDownClass(class_name):
        print("tearDownClass executed")

