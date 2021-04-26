from DataHandlers.data_reader import DataReader
from DataHandlers.data_writer import DataWriter


class TestDataReader:
    def testSimpleTest(self):
        """
        a placeholder test, demonstrating basic structure
        """
        A = 5
        B = 3
        C = 2
        E = B + C
        assert(A == E)
    
    def testdatasetDownload(self):
        """
        Test whether the download tool is downloading and unzipping a dataset,
        and that the dataset has the expected files
        """
        import os
        import shutil
        filepath = os.path.join('..','TestFolder')
        for file in os.listdir(filepath):
            shutil.rmtree(os.path.join(filepath, file))
        # if os.path.isdir(filepath):
        #     files = os.listdir(filepath)
        #     for file in files:
        #         try:
        #             os.remove(os.path.join(filepath, file))
        #         except PermissionError:
        #             pass
        dr = DataReader();
        dr.download_dataset(file_path = filepath)
        
        file1 = os.path.join(filepath, 'dataset','numerai_tournament_data.csv')
        file2 = os.path.join(filepath, 'dataset','example_predictions.csv')
        file3 = os.path.join(filepath, 'dataset','numerai_training_data.csv')
        assert( os.path.isfile(file1))
        assert( os.path.isfile(file2))
        assert( os.path.isfile(file3))
        
        
class TestDataWriter:
    def testUpload(self):
        """
        a placeholder test, demonstrating basic structure
        """
        A = 5
        B = 3
        C = 2
        E = B + C
        assert(A == E)
    
    def testdatasetUpload(self):
        """
        Test whether the upload tool is uploading a prediction properly,
        """
        import os
        import shutil
        filepath = os.path.join('..','TestFolder')
        
        
        file1 = os.path.join(filepath, 'dataset','example_predictions.csv')
        if not os.path.isfile(file1):
            dr = DataReader();
            dr.download_dataset(file_path = filepath)
        dw = DataWriter()
        try:
            dw.upload_prediction(file_path = file1, model_id = None, API_id = 1, tournament = 7)
        except ValueError as e:
            assert(e.args[0] == 'invalid tournament')

if __name__ == '__main__':
    tdr = TestDataReader()
    tdr.testSimpleTest()
    tdr.testdatasetDownload()
    
    tdw = TestDataWriter()
    tdw.testdatasetUpload()
    tdw.testUpload()