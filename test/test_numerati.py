import unittest
from numerati import Main

class testMain(unittest.TestCase):
    def setUp(self):
        self.placeHolder = Widget('widget')


    def simpleTest(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    testMain.main()