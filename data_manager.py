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
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Data file not found. Ensure the file is in the correct location.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding JSON from the data file.")
            return {}

    def get_verses(self, mood):
        """Retrieve verses based on the provided mood."""
        return self.data.get(mood, [])
