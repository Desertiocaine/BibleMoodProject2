"""
Test module for the data_manager.py functions.
"""

import unittest
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('moods_verses.json')

    def test_load_data(self):
        self.assertIsInstance(self.data_manager.data, dict)

    def test_get_verses(self):
        verses = self.data_manager.get_verses('happy')
        self.assertIsInstance(verses, list)

    def test_get_empty_verses(self):
        verses = self.data_manager.get_verses('nonexistentmood')
        self.assertEqual(verses, [])

if __name__ == '__main__':
    unittest.main()