#import os
import unittest
#import pickle
import numpy as np
import concurrent.futures
import singleton, factory, decorator, builder
#file_path = file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_revised.txt'
from tests.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_singleton_pattern(self):
        test_obj = TestUtils()
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(singleton.test_singleton, 'console')
                return_value1 = future.result()
                future = executor.submit(singleton.test_singleton, 'file')
                return_value2 = future.result()
            if (return_value1 == return_value2):
                passed = True
                test_obj.yakshaAssert("TestSingletonPattern", True, "functional")
                print("TestSingletonPattern = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestSingletonPattern", False, "functional")
                print("TestSingletonPattern = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestSingletonPattern", False, "functional")
            print("TestSingletonPattern = Failed")
        #assert passed

    def test_factory_pattern(self):
        test_obj = TestUtils()
        try:
            pf = factory.SavingsFactory("pf")
            ppf = factory.SavingsFactory("ppf")
            elss = factory.SavingsFactory("elss")
            lockin = [pf.lockin_period(), ppf.lockin_period(), elss.lockin_period(),]
            lockin_test = [5, 15, 3]
            interest = [pf.interest_rate(), ppf.interest_rate(), elss.interest_rate(),]
            interest_test = [5.5, 8, 10]
            if (lockin == lockin_test) and (interest == interest_test):
                passed = True
                test_obj.yakshaAssert("TestFactoryPattern", True, "functional")
                print("TestFactoryPattern = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestFactoryPattern", False, "functional")
                print("TestFactoryPattern = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestFactoryPattern", False, "functional")
            print("TestFactoryPattern = Failed")
        #assert passed

    def test_decorator_pattern(self):
        test_obj = TestUtils()
        try:
            actual_bill = decorator.Bill(100)
            final_bill = decorator.AddDeliveryCharge(decorator.AddGST(actual_bill)).generate_bill()
            bill = 100 + 100*0.025
            bill += bill*0.05
            if bill == final_bill:
                passed = True
                test_obj.yakshaAssert("TestDecoratorPattern", True, "functional")
                print("TestDecoratorPattern = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestDecoratorPattern", False, "functional")
                print("TestDecoratorPattern = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestDecoratorPattern", False, "functional")
            print("TestDecoratorPattern = Failed")
        #assert passed

    def test_builder_pattern(self):
        test_obj = TestUtils()
        try:
            data = np.arange(10)
            stats_list = builder.StatsGenerator(data).stats(builder.StatsListBuilder())
            stats_json = builder.StatsGenerator(data).stats(builder.StatsJsonBuilder())
            cond1 = stats_list == [data.sum(), data.mean(), data.min(), data.max()]
            cond2 = (stats_json == {'sum': data.sum(), 'avg': data.mean(), 'min': data.min(), 'max': data.max()})
            if cond1 and cond2:
                passed = True
                test_obj.yakshaAssert("TestBuilderPattern", True, "functional")
                print("TestBuilderPattern= Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestBuilderPattern", False, "functional")
                print("TestBuilderPattern = Failed")
        except:
            passed = False
            test_obj.yakshaAssert("TestBuilderPattern", False, "functional")
            print("TestBuilderPattern = Failed")
        #assert passed
