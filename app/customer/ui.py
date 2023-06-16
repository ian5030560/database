#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

# 縣市輸入框: cityEntry
# 店體輸入框: storeEntry
# 查詢按鈕: searchButton
# 結果表格: infoTable

class UI:
    def __init__(self, master=None):
        # build ui
        frame13 = ttk.Frame(master)
        frame13.configure(height=200, width=200)
        frame16 = ttk.Frame(frame13)
        frame16.configure(height=200, width=200)
        frame17 = ttk.Frame(frame16)
        frame17.configure(height=200, width=200)
        label10 = ttk.Label(frame17)
        label10.configure(text='縣市')
        label10.pack(fill="x", side="left")
        self.cityEntry = ttk.Entry(frame17)
        self.cityEntry.pack(fill="x", side="top")
        frame17.pack(fill="x", pady=10, side="top")
        frame18 = ttk.Frame(frame16)
        frame18.configure(height=200, width=200)
        label11 = ttk.Label(frame18)
        label11.configure(text='店體名稱')
        label11.pack(fill="x", side="left")
        self.storeEntry = ttk.Entry(frame18)
        self.storeEntry.pack(fill="x", side="top")
        frame18.pack(fill="x", side="top")
        self.searchButton = ttk.Button(frame16)
        self.searchButton.configure(text='查詢')
        self.searchButton.pack(fill="x", pady=10, side="top")
        separator3 = ttk.Separator(frame16)
        separator3.configure(orient="horizontal")
        separator3.pack(fill="x", pady=30, side="top")
        self.infoTable = ttk.Treeview(frame16)
        self.infoTable.configure(selectmode="extended")
        self.infoTable.pack(expand="true", fill="both", side="left")
        scrollbar3 = ttk.Scrollbar(frame16)
        scrollbar3.configure(orient="vertical", command = self.infoTable.yview)
        self.infoTable.configure(yscrollcommand = scrollbar3.set)
        scrollbar3.pack(expand="true", fill="y", side="top")
        frame16.pack(expand="true", fill="both", side="top")
        frame13.pack(expand="true", fill="both", side="top")

        # Main widget
        self.mainwindow = frame13

    def run(self):
        self.mainwindow.mainloop()