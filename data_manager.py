"""
This module handles data loading and saving for the Bible Mood app.
"""

import json

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
        print(self.data)

    def load_data(self):
        """Load mood and verse data from a JSON file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("The JSON file was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return {}

    def get_verses(self, mood):
        """Retrieve verses based on the provided mood."""
        return self.data.get(mood, [])
