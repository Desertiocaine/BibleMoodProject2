from data_manager import DataManager
from gui import BibleMoodApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    data_manager = DataManager('mood_verses.json')
    app = BibleMoodApp(root, data_manager)
    root.mainloop()