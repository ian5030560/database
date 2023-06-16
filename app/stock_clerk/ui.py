#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class UI:
    def __init__(self, master=None):
        # build ui
        frame1 = ttk.Frame(master)
        frame1.configure(height=200, width=200)
        frame2 = ttk.Frame(frame1)
        frame2.configure(height=200, width=200)
        frame4 = ttk.Frame(frame2)
        frame4.configure(height=200, width=200)
        label1 = ttk.Label(frame4)
        label1.configure(text='warehouse_uid')
        label1.pack(fill="x", side="left")
        self.wareEntry = ttk.Entry(frame4)
        self.wareEntry.pack(expand="true", fill="x", side="left")
        label5 = ttk.Label(frame4)
        label5.configure(text='store_uid')
        label5.pack(fill="x", side="left")
        self.storeEntry = ttk.Entry(frame4)
        self.storeEntry.pack(expand="true", fill="x", side="left")
        frame4.pack(fill="x", pady=5, side="top")
        frame5 = ttk.Frame(frame2)
        frame5.configure(height=200, width=200)
        label2 = ttk.Label(frame5)
        label2.configure(text='product_uid')
        label2.pack(fill="x", side="left")
        self.productEntry = ttk.Entry(frame5)
        self.productEntry.pack(expand="true", fill="x", side="left")
        label6 = ttk.Label(frame5)
        label6.configure(text='shipper_uid')
        label6.pack(fill="x", side="left")
        self.shipperEntry = ttk.Entry(frame5)
        self.shipperEntry.pack(expand="true", fill="x", side="left")
        frame5.pack(fill="x", pady=5, side="top")
        frame6 = ttk.Frame(frame2)
        frame6.configure(height=200, width=200)
        label3 = ttk.Label(frame6)
        label3.configure(text='current')
        label3.pack(fill="x", side="left")
        self.currentEntry = ttk.Entry(frame6)
        self.currentEntry.pack(expand="true", fill="x", side="left")
        label7 = ttk.Label(frame6)
        label7.configure(text='update')
        label7.pack(fill="x", side="left")
        self.updateEntry = ttk.Entry(frame6)
        self.updateEntry.pack(expand="true", fill="x", side="left")
        frame6.pack(fill="x", pady=5, side="top")
        frame11 = ttk.Frame(frame2)
        frame11.configure(height=200, width=200)
        label10 = ttk.Label(frame11)
        label10.configure(text='arrived')
        label10.pack(fill="x", side="left")
        self.arrivedEntry = ttk.Entry(frame11)
        self.arrivedEntry.pack(expand="true", fill="x", side="left")
        label11 = ttk.Label(frame11)
        label11.configure(text='set off')
        label11.pack(fill="x", side="left")
        self.setOffEntry = ttk.Entry(frame11)
        self.setOffEntry.pack(expand="true", fill="x", side="left")
        frame11.pack(fill="x", pady=5, side="top")
        frame9 = ttk.Frame(frame2)
        frame9.configure(height=200, width=200)
        label9 = ttk.Label(frame9)
        label9.configure(text='cost')
        label9.pack(fill="x", side="left")
        self.costEntry = ttk.Entry(frame9)
        self.costEntry.pack(fill="x", side="top")
        frame9.pack(fill="x", pady=5, side="top")
        frame8 = ttk.Frame(frame2)
        frame8.configure(height=200, width=200)
        self.searchButton = ttk.Button(frame8)
        self.searchButton.configure(text='查詢')
        self.searchButton.pack(expand="true", fill="x", side="left")
        frame8.pack(fill="x", pady=5, side="top")
        frame2.pack(fill="both", side="top")
        self.infoTable = ttk.Treeview(frame1)
        self.infoTable.configure(selectmode="extended", show="headings")
        self.infoTable.pack(expand="true", fill="both", side="left")
        scrollbar1 = ttk.Scrollbar(frame1)
        scrollbar1.configure(orient="vertical", command = self.infoTable.yview)
        self.infoTable.configure(yscrollcommand = scrollbar1.set)
        scrollbar1.pack(expand="true", fill="y", side="top")
        frame1.pack(expand="true", fill="both", side="top")

        # Main widget
        self.mainwindow = frame1

    def run(self):
        self.mainwindow.mainloop()