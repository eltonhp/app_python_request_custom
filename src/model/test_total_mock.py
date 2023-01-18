import unittest
from unittest.mock import patch
from .total import Total




class TestTotal(unittest.TestCase):

    def test_calculate_total(self):
        with patch('total.read') as mock_read:
            mock_read.return_value = [1, 2, 3]
            total = Total()
            result = total.calculate_total('')
            self.assertEqual(result, 6)