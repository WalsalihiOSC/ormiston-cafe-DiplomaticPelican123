import csv
from tkinter import *
from PIL import ImageTk,Image

class FileHandling:
  def __init__(self):
    self.csv_data = self.text_file_manager()

  def text_file_manager(self):
    data = []
    with open("Data/data.csv", "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
        data.append(row)
    return(data)

class Main:
  def __init__(self, root):
    self.root = root

    self.intro_frame = Frame(root, width = 250, height = 250, highlightbackground = "black", highlightthickness = 1)
    self.intro_frame.place(x = 500, y = 100)

    intro_label = Label(self.intro_frame, text = "Ormiston Senior College Maca's", anchor = CENTER)
    intro_label.place(x = 35  , y = 110)

    start_button = Button(self.intro_frame, text = "Order Now", command = self.menu)
    start_button.place(x = 179, y = 222)

  def menu(self):
    self.intro_frame.destroy()
    Menu(root)


class Menu:
  def __init__(self, root):
    self.root = root
    self.database = FileHandling()
    self.csv_data = self.database.csv_data

    ''' Main Frames '''
    self.master_frame = Frame(root, highlightbackground="black", highlightthickness = 1)
    self.side_fliter = Frame(root)
    self.order_frame = Frame(root, highlightbackground="black", highlightthickness = 1)
    self.master_frame.place(x = 500, y = 0)
    self.side_fliter.grid(row = 0 ,column = 0)
    self.order_frame.place(x = 1100, y = 0)

    ''' Menu Frames '''
    test = Label(self.order_frame, text = "Order List ://")
    test.grid()
    self.burger_frame = Frame(self.master_frame)
    self.withrice_frame = Frame(self.master_frame)
    self.salads_frame = Frame(self.master_frame)
    self.dessert_frame = Frame(self.master_frame)
    self.drink_frame = Frame(self.master_frame)

    ''' Burger Options '''
    x = y = 0
    for entry in self.csv_data:
      if entry["category"] != "Burger":
        break
      if x == 3:
        x = 0
        y +=1
      name = entry["name"]
      Label(self.burger_frame, text = f"{name}").grid(column = x, row = y)
      x +=1

    ''' With Rice Options '''
    x = y = 0
    for entry in self.csv_data:
      if entry["category"] != "Withrice":
        break
      if x == 3:
        x = 0
        y +=1
        name = entry["name"]
        Label(self.withrice_frame, text = f"{name}").grid(column = x, row = y)
        x +=1

    ''' Salad Options '''
    x = y = 0
    for entry in self.csv_data:
      if entry["category"] != "Salad":
        break
      if x == 3:
        x = 0
        y +=1
        name = entry["name"]
        Label(self.salads_frame, text = f"{name}").grid(column = x, row = y)
        x +=1

    ''' Dessert Options '''
    x = y = 0
    for entry in self.csv_data:
      if entry["category"] != "Dessert":
        break
      if x == 3:
        x = 0
        y +=1
        name = entry["name"]
        Label(self.dessert_frame, text = f"{name}").grid(column = x, row = y)
        x +=1

    ''' Drink Options '''
    x = y = 0
    for entry in self.csv_data:
      if entry["category"] != "Drink":
        break
      if x == 3:
        x = 0
        y +=1
        name = entry["name"]
        Label(self.drink_frame, text = f"{name}").grid(column = x, row = y)
        x +=1

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

    ''' Displaying Menu's Functions and other Functions '''
  def burger(self):
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    self.burger_frame.grid()

  def withrice(self):
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    self.withrice_frame.grid()

  def salad(self):
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    self.salads_frame.grid()
  
  def dessert(self):
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    self.dessert_frame.grid()

  def drink(self):
    for child in self.master_frame.winfo_children():
      child.grid_forget()
    self.drink_frame.grid()

  def checkout(self):
    self.master_frame.destroy()
    self.side_fliter.destroy()
    Checkout(root)


class Checkout:
  def __init__(self, root):
    self.root = root

    ''' Main Frames '''
    self.checkout_frame = Frame(root, height = 250, width = 250, highlightbackground = "black", highlightthickness = 1)
    self.checkout_frame.place(x = 525, y = 150)

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
  Main(root)
  root.title("Ormiston Senior College Cafe")
  root.geometry("1250x500")
  root.update()
  root.minsize(root.winfo_width(), root.winfo_height())
  root.mainloop()