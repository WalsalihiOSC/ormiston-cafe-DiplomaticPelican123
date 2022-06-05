from tkinter import *
from PIL import ImageTk,Image

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
    chicken = Label(self.burger_frame, text = "Chicken Burger")
    beef = Label(self.burger_frame, text = "Beef Burger")
    vege = Label(self.burger_frame, text = "Vegetarian Burger")
    butter_chicken = Label(self.burger_frame, text = "Butter Chicken Burger")
    pizza_burger = Label(self.burger_frame, text = "Pizza Burger")
    supreme_burger = Label(self.burger_frame, text = "Supreme Burger")
    potato_corn = Label(self.burger_frame, text = "Potato Corn")
    chilli_pepper = Label(self.burger_frame, text = "Chilli Pepper Radish")
    lamb = Label(self.burger_frame, text = "Lamb Burger")
    chicken.grid(row = 0, column = 0)
    beef.grid(row = 0, column = 1)
    vege.grid(row = 0, column = 2)
    butter_chicken.grid(row = 1, column = 0)
    pizza_burger.grid(row = 1, column = 1)
    supreme_burger.grid(row = 1, column = 2)
    potato_corn.grid(row = 2, column = 0)
    chilli_pepper.grid(row = 2, column = 1)
    lamb.grid(row = 2, column = 2)

    ''' With Rice Options '''
    butter_chicken_rice = Label(self.withrice_frame, text = "Butter Chicken")
    lamb_curry = Label(self.withrice_frame, text = "Lamb Curry")
    potato_curry = Label(self.withrice_frame, text = "Potato Curry")
    butter_chicken_rice.grid(row = 0, column = 0)
    lamb_curry.grid(row = 0, column = 1)
    potato_curry.grid(row = 0, column = 2)

    ''' Salad Options '''


    ''' Dessert Options '''


    ''' Drink Options '''
    coke = Label(self.drink_frame, text = "Coke")
    sprite = Label(self.drink_frame, text = "Sprite")
    fanta = Label(self.drink_frame, text = "Fanta")
    nz_drink = Label(self.drink_frame, text = "L&P")
    seven_up = Label(self.drink_frame, text = "7-UP")
    lift = Label(self.drink_frame, text = "Lift")
    coke.grid(row = 0, column = 0)
    sprite.grid(row = 0, column = 1)
    fanta.grid(row = 0, column = 2)
    nz_drink.grid(row = 1, column = 0)
    seven_up.grid(row = 1, column = 1)
    lift.grid(row = 1, column = 2)

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