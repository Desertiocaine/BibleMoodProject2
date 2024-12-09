"""
Test module for the data_manager.py functions.
"""

import unittest
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('mood_verses.json')

    def test_load_data(self):
        """Test that data is loaded correctly and is a dictionary."""
        self.assertIsInstance(self.data_manager.data, dict)

    def test_get_verses(self):
        """Test that at least two unique verses are retrieved correctly for different moods."""
        moods = ['happy', 'sad', 'anxious', 'grateful']
        for mood in moods:
            with self.subTest(mood=mood):
                verses = self.data_manager.get_verses(mood)
                self.assertIsInstance(verses, list)
                self.assertGreaterEqual(len(verses), 2)
                self.assertNotEqual(verses[0], verses[1])

    def test_get_empty_verses(self):
        """Test that an empty list is returned for a nonexistent mood."""
        verses = self.data_manager.get_verses('nonexistentmood')
        self.assertEqual(verses, [])

if __name__ == '__main__':
    unittest.main()