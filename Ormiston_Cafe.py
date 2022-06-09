import json
from tkinter import *
from PIL import ImageTk,Image # Make sure to "pip install PILLOW"

''' Class 1 '''
class Menu:
  def __init__(self, root):
    self.root = root
    with open("data.json", "r") as file:
      self.database = json.load(file)

    IMG_LIST = [
      ImageTk.PhotoImage(Image.open("Image/osc.jpg")),

    ]

    ''' Main Frames '''
    self.master_frame = Frame(root, highlightbackground="black", highlightthickness = 1)
    self.side_fliter = Frame(root)
    self.order_frame = Frame(root, highlightbackground="black", highlightthickness = 1)
    self.master_frame.place(relx = 0.5, rely = 0, anchor = N)
    self.side_fliter.grid(row = 0 ,column = 0)
    self.order_frame.place(relx = 0.9, rely = 0)

    ''' Menu Frames '''
    test = Label(self.order_frame, text = "Order List ://")
    test.grid()
    self.burger_frame = Frame(self.master_frame)
    self.withrice_frame = Frame(self.master_frame)
    self.salads_frame = Frame(self.master_frame)
    self.dessert_frame = Frame(self.master_frame)
    self.drink_frame = Frame(self.master_frame)

    ''' Menu Filters (Buttons) '''
    btn1 = Button(self.side_fliter, text = "Burger", relief = "groove", command = self.burger)
    btn2 = Button(self.side_fliter, text = "With Rice", relief = "groove", command = self.withrice)
    btn3 = Button(self.side_fliter, text = "Salads", relief = "groove", command = self.salad)
    btn4 = Button(self.side_fliter, text = "Desserts", relief = "groove", command = self.dessert)
    btn5 = Button(self.side_fliter, text = "Drinks", relief = "groove", command = self.drink)
    btn6 = Button(self.side_fliter, text = "Checkout", command = self.checkout)
    btn1.grid(sticky = "NW")
    btn2.grid(sticky = "NW")
    btn3.grid(sticky = "NW")
    btn4.grid(sticky = "NW")
    btn5.grid(sticky = "NW")
    btn6.grid(sticky = "SE")

    ''' Displaying Menu's Items '''
  def burger(self):
    x = y = 0   # Using this to Grid my Menu Items
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
        if i['category'] == 'Burger':
          txt = i["name"]
          if x == 3:
            x = 0
            y = y+1
          Button(self.burger_frame, text = txt).grid(column = x, row = y)
          x = x+1
    self.burger_frame.grid()

  def withrice(self):
    x = y = 0   # Using this to Grid my Menu Items
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
      if i["category"] == "Withrice":
        txt = i["name"]
        if x == 3:
          x = 0
          y = y+1
        Button(self.withrice_frame, text = txt).grid(column = y, row = x)
        x = x+1
    self.withrice_frame.grid()

  def salad(self):
    x = y = 0  # Using this to Grid my Menu Items
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
      if i["category"] == "Salad":
        txt = i["name"]
        if x == 3:
          x = 0
          y = y+1
        Button(self.salads_frame, text = txt).grid(column = y, row = x)
        x = x+1
    self.salads_frame.grid()
  
  def dessert(self):
    x = y = 0  # Using this to Grid my Menu Items
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
      if i["category"] == "Dessert":
        txt = i["name"]
        if x == 3:
          x = 0
          y = y+1
        Button(self.dessert_frame, text = txt).grid(column = y, row = x)
        x = x+1
    self.dessert_frame.grid()

  def drink(self):
    x = y = 0
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
      if i["category"] == "Drink":
        txt = i["name"]
        if x == 3:
          x = 0
          y = y+1
        Button(self.drink_frame, text = txt).grid(column = y, row = x)
        x = x+1
    self.drink_frame.grid()

  def checkout(self):
    self.master_frame.destroy()
    self.side_fliter.destroy()
    Checkout(root)


''' Class 2 '''
class Checkout:
  def __init__(self, root):
    self.root = root

    ''' Main Frames '''
    self.checkout_frame = Frame(root, height = 250, width = 250, highlightbackground = "black", highlightthickness = 1)
    self.checkout_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    ''' Displaying Elements '''
    money = Label(self.checkout_frame, text = "Give Money Here:")
    order_price = Label(self.checkout_frame, text = "Order Price:")
    change = Label(self.checkout_frame, text = "Change:")
    btn = Button(self.checkout_frame, text = "Calculate Change", command = None)
    money.grid(row = 0, column = 0)
    order_price.grid(row = 1, column = 0)
    change.grid(row = 2, column = 0)
    btn.grid(row = 3, column = 1, sticky = "E")

    ''' Displaying Elements (Again) '''
    money_owing = Entry(self.checkout_frame)
    order_price_display = Label(self.checkout_frame, text = None)
    change_display = Label(self.checkout_frame, text = None)
    money_owing.grid(row = 0, column = 1)
    order_price_display.grid(row = 1, column = 1)
    change_display.grid(row = 2, column = 1)

    ''' Buttons '''
    new_order_btn = Button(self.checkout_frame, text = "New Order", command = self.new_order)
    quit_btn = Button(self.checkout_frame, text = "Quit", command = self.quit)
    new_order_btn.grid(row = 4, column = 0, sticky = "W")
    quit_btn.grid(row = 4, column = 1, sticky = "E")

    ''' Functions '''
  def quit(self):
    self.root.destroy()

  def new_order(self):
    self.checkout_frame.destroy()
    Menu(root)


if __name__ == "__main__":
  root = Tk()
  Menu(root)
  root.title("Ormiston Senior College Cafe")
  root.geometry("800x600")
  root.update()
  root.minsize(root.winfo_width(), root.winfo_height())
  root.mainloop()