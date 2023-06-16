#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class App:
    def __init__(self, master=None):
        # build ui
        frame1 = ttk.Frame(master)
        frame1.configure(height=200, width=200)
        frame3 = ttk.Frame(frame1)
        frame3.configure(height=200, width=200)
        frame6 = ttk.Frame(frame3)
        frame6.configure(height=200, width=200)
        self.nameLabel = ttk.Label(frame6)
        self.nameLabel.configure(text='姓名')
        self.nameLabel.pack(expand="false", fill="x", side="left")
        self.nameEntry = ttk.Entry(frame6)
        self.nameEntry.pack(expand="true", fill="x", side="top")
        frame6.pack(fill="x", side="top", pady = 10)
        frame9 = ttk.Frame(frame3)
        frame9.configure(height=200, width=200)
        self.addressLabel = ttk.Label(frame9)
        self.addressLabel.configure(text='地址')
        self.addressLabel.pack(expand="false", fill="x", side="left")
        self.addressEntry = ttk.Entry(frame9)
        self.addressEntry.pack(expand="true", fill="x", side="top")
        frame9.pack(fill="x", side="top")
        self.search = ttk.Button(frame3)
        self.search.configure(text='查詢')
        self.search.pack(fill="x", side="top", pady = 10)
        separator1 = ttk.Separator(frame3)
        separator1.configure(orient="horizontal")
        separator1.pack(fill="x", pady=30, side="top")
        self.infoView = ttk.Treeview(frame3)
        self.infoView.configure(selectmode="browse", show = "headings")
        self.infoView.pack(expand="true", fill="both", side="left")
        scrollbar1 = ttk.Scrollbar(frame3)
        scrollbar1.configure(orient="vertical", command = self.infoView.yview)
        scrollbar1.pack(expand="true", fill="y", side="top")
        self.infoView.configure(yscrollcommand = scrollbar1.set)
        frame3.pack(expand="true", fill="both", side="top")
        frame1.pack(expand="true", fill="both", side="top")

        # Main widget
        self.mainwindow = frame1

    def run(self):
        self.mainwindow.mainloop()

