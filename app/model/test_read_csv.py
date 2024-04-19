import unittest
from unittest.mock import patch
import pandas as pd
from read_csv import read_csv

class TestReadCSV(unittest.TestCase):

    @patch('read_csv.pd.read_csv')
    @patch('read_csv.os.getenv')
    def test_read_csv(self, mock_getenv, mock_read_csv):
        mock_getenv.return_value = './coordenates.csv'

        csv_data = str(pd.DataFrame({'lat': ["''52,923454''", "''53,457321''"],
                                 'lon': ["''-1,474217''", "''-2,262773''"]}))

        mock_read_csv.return_value = csv_data
        data = read_csv()
        expected_data = [{'lat': 52.923454, 'lon': -1.474217}, {'lat': 53.457321, 'lon': -2.262773}]
        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()
