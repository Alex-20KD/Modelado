# main.py
import tkinter as tk
from view import MiniMundoEscolarApp

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniMundoEscolarApp(root)
    root.mainloop()