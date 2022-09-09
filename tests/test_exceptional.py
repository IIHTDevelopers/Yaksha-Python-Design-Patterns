#import os
import unittest
#import numpy as np
#file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_exception_revised.txt'
from tests.TestUtils import TestUtils
class ExceptionalTests(unittest.TestCase):
    def test_dummy_exceptional_testcase(self):
        test_obj = TestUtils()
        try:
            test_obj.yakshaAssert("TestDummyExceptionalTestCase",True,"exception")
            print("TestDummyExceptionalTestCase= Passed")
        except (ValueError,OutOfBoundaryMarksError):
            test_obj.yakshaAssert("TestDummyExceptionalTestCase",False,"exception")
            print("TestDummyExceptionalTestCase = Failed")
