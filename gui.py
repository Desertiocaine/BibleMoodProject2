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
        """Sets up the GUI with flair and pizzazz."""
        self.root.title("Bible Mood App")
        self.root.geometry("600x400")  # Increased window size
        # Set Background Color
        self.root.configure(bg='#b3cde0')  # Pastel blue background

        self.mood_label = tk.Label(self.root, text="Select Your Mood:", font=("Helvetica", 16), bg='#b3cde0', fg='black')
        self.mood_label.pack(pady=10)

        self.moods = ["happy", "sad", "mad", "anxious", "grateful"]
        self.selected_mood = tk.StringVar(self.root)
        self.selected_mood.set(self.moods[0])

        self.mood_menu = tk.OptionMenu(self.root, self.selected_mood, *self.moods)
        self.mood_menu.config(font=("Helvetica", 14), bg='#b3cde0', fg='black', highlightbackground='#b3cde0')
        self.mood_menu.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Find Verse", command=self.find_verse, font=("Helvetica", 14), bg='white', fg='black', highlightbackground='#b3cde0')
        self.submit_button.pack(pady=10)

        self.result_display = tk.Text(self.root, wrap='word', width=70, height=10, font=("Helvetica", 14), bg='white', fg='black')
        self.result_display.pack(pady=10)

    def find_verse(self):
        """Finds and displays one random verse based on user mood input."""
        mood = self.selected_mood.get().lower()  # Get selected mood
        verses = self.data_manager.get_verses(mood)
        self.result_display.delete(1.0, tk.END)
        if verses:
            import random
            random_verse = random.choice(verses)
            self.result_display.insert(tk.END, random_verse + "\n")
        else:
            self.result_display.insert(tk.END, f"No verses found for mood: {mood}")
