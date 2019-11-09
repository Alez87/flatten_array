import unittest
import sys
import importlib
import json

TARGET = importlib.import_module('flatten_array')

def checkEqual(L1, L2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)

class TestFlattenArray(unittest.TestCase):

    ARRAY = []

    def test_array(self):
        result = TARGET.main()
        target_array=json.loads(self.ARRAY)
        print('result: ' + str(result))
        print('array: ' + str(target_array))
        self.assertTrue(type(result) is list)
        self.assertTrue(checkEqual(result, target_array))

if __name__ == '__main__':
#    unittest.main(argv=['TestFlattenArray.test_empty_array ']+sys.argv[2:], exit=False)
    if len(sys.argv) > 1:
        TestFlattenArray.ARRAY = sys.argv.pop()
    unittest.main(argv=['TestFlattenArray.test_empty_array ']+sys.argv[2:], exit=False)
