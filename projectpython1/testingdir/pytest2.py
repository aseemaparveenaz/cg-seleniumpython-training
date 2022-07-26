import unittest
class Example(unittest.TestCase):
    @classmethod
    def setUpClass(class_name):
        print("setupclass executed")
    def setUp(self):
        print("setup exuted")
    def test_1(self):
        print("test-1 executed")
    def test_2(self):
        print("test-2 executed")
    @classmethod
    def tearDown(self):
        print("tear down executed")
if __name__=='__main__':
    unittest.main()