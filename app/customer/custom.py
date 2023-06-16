import tkinter as tk
from ui import UI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("顧客")
    app = UI(root)
    app.run()