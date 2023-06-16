import tkinter as tk
from ui import UI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("倉管人員")
    app = UI(root)
    app.run()