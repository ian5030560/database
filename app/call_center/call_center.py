from db.db import cursor
import tkinter as tk
from database.app.customer.ui import App


def refresh(app: App):
    tree = app.infoView
    for child in tree.get_children():
        tree.delete(child)
        
def display(app: App, dataSet: list):
    tree = app.infoView
    
    for data in dataSet:
        tree.insert("", "end", data)

def search(app: App):
    refresh(app)
    name = app.nameEntry.get()
    address = app.addressEntry.get()
    
    if name and address:
        ins = "SELECT `name`, `address`, `phone` FROM online_customer WHERE `name` = '{}', `address` = '{}'".format(name, address)
    elif name:
        ins = "SELECT `name`, `address`, `phone` FROM online_custom WHERE `name` = '{}'".format(name)
    else:
        ins = "SELECT `name`, `address`, `phone` FROM online_custom WHERE `address` = '{}'".format(address)
    cursor.execute(ins)
    
    dataSet = cursor.fetchall()
    display(app, dataSet)

if __name__ == "__main__":
    win = tk.Tk()
    app = App(win)
    win.title("客服人員")
    app.search["command"] = lambda: search(app)
    app.infoView["columns"] = ["name", "address", "phone"]
    app.infoView.heading("name", text = "姓名")
    app.infoView.heading("address", text = "地址")
    app.infoView.heading("phone", text = "電話")
    win.mainloop()