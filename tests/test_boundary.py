import unittest
from tests.TestUtils import TestUtils
class BoundaryTests(unittest.TestCase):
    def test_dummy_boundary_testcase(self):
        test_obj = TestUtils()
        try:
            test_obj.yakshaAssert("TestDummyBoundaryTestCase",True,"boundary")
            print("TestDummyBoundaryTestCase = Passed")
        except (ValueError,OutOfBoundaryMarksError):
            test_obj.yakshaAssert("TestDummyBoundaryTestCase",False,"boundary")
            print("TestDummyBoundaryTestCase = Failed")
