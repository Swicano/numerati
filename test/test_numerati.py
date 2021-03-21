import unittest
from numerati import Main

class testMain(unittest.TestCase):



    def testSimpleTest(self):

        A = 5
        B = 3
        C = 2

        D = B + C
        self.assertEqual(A, D)

if __name__ == '__main__':
    testMain.simpleTest()