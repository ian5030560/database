import tkinter as tk
from ui import UI
from updatewindow import UpdateWindow, DatePicker
import datetime as dt
from db_access import db_search, db_update, db_delete

def refresh(app: UI):
    tree = app.infoTable
    for child in tree.get_children():
        tree.delete(child)

def display(app: UI, dataSet: list):
    tree = app.infoTable
    
    for data in dataSet:
        tree.insert("", "end", values = data)

def search(app: UI):
    
    refresh(app)
    
    condition = {
        "warehouse_uid": app.wareEntry.get(),
        "store_uid": app.storeEntry.get(),
        "product_uid": app.productEntry.get(),
        "shipper_uid": app.shipperEntry.get(),
        "current_amount": app.currentEntry.get(),
        "update_amount": app.updateEntry.get(),
        "cost": app.costEntry.get(),
        "arrived": app.arrivedEntry.get(),
        "set_off": app.setOffEntry.get()
    }
    
    display(app, db_search(condition))

def select(app: UI):

    focus = app.infoTable.focus()

    if focus:
        item = app.infoTable.item(focus)
        arrived = item["values"][7]
        setOff = item["values"][8]

        win = UpdateWindow()
        
        def update():
            data = [
                win.wareEntry.get(),
                win.storeEntry.get(),
                win.productEntry.get(),
                win.shipperEntry.get(),
                win.currentEntry.get(),
                win.updateEntry.get(),
                win.costEntry.get(),
                win.arrivedLabel["text"],
                win.setOffLabel["text"]
            ]
            
            db_update(list(item["values"]), data)
            app.infoTable.item(app.infoTable.focus(), values = data)
            
            win.destroy()
        
        def datePick(label: tk.Label, dateTime: str):
            datetime = dt.datetime.strptime(dateTime, "%Y-%m-%d")
            picker = DatePicker(win, datetime.year, datetime.month, datetime.day)
            picker.calendar.bind("<<CalendarSelected>>", lambda event: label.config(text = picker.calendar.selection_get()))
        
        win.arrivedButton["command"] = lambda: datePick(win.arrivedLabel, arrived)
        win.setOffButton["command"] = lambda: datePick(win.setOffLabel, setOff)
        win.summitButton["command"] = update
        win.cancelButton["command"] = win.destroy
        win.wait_window(win)

def delete(app: UI):
    focus = app.infoTable.focus()
    
    if focus:
        data = app.infoTable.item(focus)["values"]
        app.infoTable.delete(focus)
        db_delete(data)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("倉管人員")
    app = UI(root)
    app.infoTable["columns"] = ["warehouse_uid", "store_uid", "product_uid", "shipper_uid", "current", "update", "cost", "arrived", "set_off"]
    for col in app.infoTable["columns"]:
        app.infoTable.heading(col, text = col)

    app.infoTable.insert("", "end", values = [1, 2, 3, 4, 5, 6, 7, 8, 9])
    app.infoTable.bind("<Double-Button-1>", lambda event: select(app))
    app.searchButton["command"] = lambda: search(app)
    
    menu = tk.Menu(root, tearoff = False)
    menu.add_command(label = "修改", command = lambda: select(app))
    menu.add_command(label = "刪除", command = lambda: delete(app))
        
    app.infoTable.bind("<Button-3>", lambda event: menu.tk_popup(event.x_root, event.y_root))
    app.run()