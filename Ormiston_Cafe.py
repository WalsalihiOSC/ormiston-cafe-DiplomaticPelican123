import json
from tkinter import *
from PIL import ImageTk,Image # Make sure to "pip install PILLOW"

''' Data Class '''
class Data:
  def __init__(self):

    ''' Variables '''
    self.change_var = IntVar()
    self.price_list = []

''' Class 1 '''
class Menu:
  def __init__(self, root):
    self.root = root
    self.data = Data()

    ''' JSON File '''
    with open("data.json", "r") as file:
      self.database = json.load(file)

    ''' Image List '''
    IMG_LIST = [
      ImageTk.PhotoImage(Image.open("Image/osc.jpg"))]

    ''' Main Frames '''
    self.master_frame = Frame(root, highlightbackground="black", highlightthickness = 1)
    self.side_fliter = Frame(root)
    self.order_frame = Frame(root, highlightbackground="black", highlightthickness = 1)
    self.checkout_frame = Frame(root, height = 250, width = 250, highlightbackground = "black", highlightthickness = 1)
    self.master_frame.place(relx = 0.5, rely = 0, anchor = N)
    self.side_fliter.grid(row = 0 ,column = 0)
    self.order_frame.place(relx = 0.8)

    ''' Menu Frames '''
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

    ''' Menu List Buttons '''
    self.order = Label(self.order_frame, text = "Order List")
    self.order.grid()

    self.clear_btn = Button(self.order_frame, text = "Clear All", command = self.clear_menu)
    self.clear_btn.grid(sticky = S)

    ''' Displaying Menu's Items '''  
  def burger(self):
    x = y = 0   # Using this to Grid my Menu Items
    for child in self.master_frame.winfo_children():  # Checking for widgets in the frame selected
      child.grid_forget()   # Deleting all the widgets in the frame
    for i in self.database:
        if i['category'] == 'Burger':
          txt = i["name"] # Putting all the menu items in a variable that equal to burger so I can use it later
          price = i["price"]
          if x == 3:
            x = 0 # column = 0 once the widgets placed in 3x3 grid
            y = y+2 # Puts the next set of menu items in the next row
          Label(self.burger_frame, text = txt).grid(column = x, row = y)
          Button(self.burger_frame, text = f"${price}", command = lambda i=i:self.display_info(i)).grid(column = x, row = y+1)
          x = x+1
    self.burger_frame.grid()  # Griding the desired frame

  def withrice(self):
    x = y = 0   # Using this to Grid my Menu Items
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
      if i["category"] == "Withrice":
        txt = i["name"]
        price = i["price"]
        if x == 3:
          x = 0
          y = y+2
        Label(self.withrice_frame, text = txt).grid(column = x, row = y)
        Button(self.withrice_frame, text = f"${price}", command = lambda i=i:self.display_info(i)).grid(column = x, row = y+1)
        x = x+1
    self.withrice_frame.grid()

  def salad(self):
    x = y = 0  # Using this to Grid my Menu Items
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
      if i["category"] == "Salad":
        txt = i["name"]
        price = i["price"]
        if x == 3:
          x = 0
          y = y+2
        Label(self.salads_frame, text = txt).grid(column = x, row = y)
        Button(self.salads_frame, text = f"${price}", command = lambda i=i:self.display_info(i)).grid(column = x, row = y+1)
        x = x+1
    self.salads_frame.grid()
  
  def dessert(self):
    x = y = 0  # Using this to Grid my Menu Items (labels)
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
      if i["category"] == "Dessert":
        txt = i["name"]
        price = i["price"]
        if x == 3:
          x = 0
          y = y+2
        Label(self.dessert_frame, text = txt).grid(column = x, row = y)
        Button(self.dessert_frame, text = f"${price}", command = lambda i=i:self.display_info(i)).grid(column = x, row = y+1)
        x = x+1
    self.dessert_frame.grid()

  def drink(self):
    x = y = 0
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    for i in self.database:
      if i["category"] == "Drink":
        txt = i["name"]
        price = i["price"]
        if x == 3:
          x = 0
          y = y+2
        Label(self.drink_frame, text = txt).grid(column = x, row = y)
        Button(self.drink_frame, text = f"${price}", command = lambda i=i:self.display_info(i)).grid(column = x, row = y+1)
        x = x+1
    self.drink_frame.grid()

  ''' Button Functions '''
  def display_info(self, info):
    Label(self.order_frame, text = info["name"]).grid()
    self.data.price_list.append(info["price"])

  def clear_menu(self):
    for child in self.order_frame.winfo_children():
      child.grid_forget()
    self.order.grid()
    self.clear_btn.grid(sticky = S)

  def checkout(self):
    self.clear_btn.configure(state = DISABLED)
    self.master_frame.destroy()
    self.side_fliter.destroy()
    self.checkout_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    self.price = sum(self.data.price_list)

    ''' Displaying Elements '''
    money = Label(self.checkout_frame, text = "Give Money Here:")
    order_price = Label(self.checkout_frame, text = "Order Price:")
    change = Label(self.checkout_frame, text = "Change:")
    btn = Button(self.checkout_frame, text = "Calculate Change", command = self.calculate)
    money.grid(row = 0, column = 0)
    order_price.grid(row = 1, column = 0)
    change.grid(row = 2, column = 0)
    btn.grid(row = 3, column = 1, sticky = "E")

    ''' Displaying Elements (Data) '''
    money_owing = Entry(self.checkout_frame, textvariable = self.data.change_var)
    order_price_display = Label(self.checkout_frame, text = f"${self.price}")
    self.change_display = Label(self.checkout_frame, text = None)
    money_owing.grid(row = 0, column = 1)
    order_price_display.grid(row = 1, column = 1)
    self.change_display.grid(row = 2, column = 1)

    ''' Buttons '''
    new_order_btn = Button(self.checkout_frame, text = "New Order", command = self.new_order)
    quit_btn = Button(self.checkout_frame, text = "Quit", command = self.quit)
    new_order_btn.grid(row = 4, column = 0, sticky = "W")
    quit_btn.grid(row = 4, column = 1, sticky = "E")

    ''' Functions '''
  def calculate(self):
    try:
     x = self.data.change_var.get()
     y = x - self.price
     self.change_display.configure(text = f"${y}")

     if x <self.price:
      self.change_display.configure(text = "Gimmie More Money!!!")
     elif x == self.price:
      self.change_display.configure(text = "No Change")
    except ValueError():
      pass

  def quit(self):
    self.root.destroy()

  def new_order(self):
    self.checkout_frame.destroy()
    self.data.price_list.clear()
    self.order_frame.destroy()
    Menu(root)

''' Main Routine '''
if __name__ == "__main__":
  root = Tk()
  Menu(root)
  root.title("Ormiston Senior College Cafe")
  root.geometry("800x600")
  root.update()
  root.minsize(root.winfo_width(), root.winfo_height())
  root.mainloop()