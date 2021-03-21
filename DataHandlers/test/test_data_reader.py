from DataHandlers.data_reader import DataReader


class TestDataReader:
    def testSimpleTest(self):
        """
        a placeholder test, demonstrating basic structurer
        """
        A = 5
        B = 3
        C = 2
        E = B + C
        assert(A == E)


if __name__ == '__main__':
    TestDataReader.simpleTest()