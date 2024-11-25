"""
This module manages the graphical user interface for the Bible Mood app.
"""

import tkinter as tk
from data_manager import DataManager


class BibleMoodApp:
    def __init__(self, root, data_manager):
        self.root = root
        self.data_manager = data_manager
        self.setup_gui()

    def setup_gui(self):
        """Sets up the GUI with flair and pizzaz."""
        self.root.title("Bible Mood App")
        self.root.geometry("400x300")

        self.mood_label = tk.Label(self.root, text="Enter Your Mood:")
        self.mood_label.pack()

        self.mood_entry = tk.Entry(self.root)
        self.mood_entry.pack()

        self.submit_button = tk.Button(self.root, text="Find Verse", command=self.find_verse)
        self.submit_button.pack()

        self.result_display = tk.Text(self.root, wrap='word', width=50, height=10)
        self.result_display.pack()

    def find_verse(self):
        """Finds and displays verses based on user mood input."""
        mood = self.mood_entry.get().lower()
        verses = self.data_manager.get_verses(mood)

        self.result_display.delete(1.0, tk.END)  # Clear previous results
        if verses:
            for verse in verses:
                self.result_display.insert(tk.END, verse + "\n")
        else:
            self.result_display.insert(tk.END, f"No verses found for mood: {mood}")


if __name__ == "__main__":
    root = tk.Tk()
    data_manager = DataManager('moods_verses.json')
    app = BibleMoodApp(root, data_manager)
    root.mainloop()