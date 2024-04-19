import unittest
from unittest.mock import patch
from app.controller.postcodes_api import get_postcode

class TestGetPostcode(unittest.TestCase):

    @patch('postcodes_api.requests.get')
    def test_get_postcode(self, mock_get):
        mock_get.return_value.json.return_value = {'result': [{'postcode': 'BS39 4HU'}]}
        
        result = get_postcode({'lon': -2.528614, 'lat': 51.377773})
        expected_postcode = (['BS39 4HU'], {'result': [{'postcode': 'BS39 4HU'}]})
        self.assertEqual(result, expected_postcode)

if __name__ == '__main__':
    unittest.main()
