import sys
import os

sys.path.append(sys.path[0]+"/...")
sys.path.append(os.getcwd())

from unittest import TestLoader,TestSuite,TextTestRunner
from pyunit_Dir.test_Google_Search import Google_Search
from pyunit_Dir.test_Home_Page import Google_Homepage
from pyunit_Dir import test_Home_Page



if __name__=='__main__':
    test_loader=TestLoader()
    test_suite=TestSuite((
        test_loader.loadTestsFromTestCase(Google_Homepage),
        test_loader.loadTestsFromTestCase(Google_Search),
    ))


    test_runner=TextTestRunner(verbosity=2)
    test_runner.run(test_suite)