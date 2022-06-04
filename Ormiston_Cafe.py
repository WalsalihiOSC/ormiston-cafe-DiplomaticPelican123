from tkinter import *

class Main:
  def __init__(self, root):

    self.root = root

    self.intro_frame = Frame(root, width = 250, height = 250, highlightbackground = "black", highlightthickness = 1)
    self.intro_frame.place(x = 250, y = 100)

    intro_label = Label(self.intro_frame, text = "Ormiston Senior College Maca's", anchor = CENTER)
    intro_label.place(x = 35, y = 110)

    start_button = Button(self.intro_frame, text = "Order Now", command = self.menu)
    start_button.place(x = 179, y = 222)

  def menu(self):
    self.intro_frame.destroy()
    Menu(root)


class Menu:
  def __init__(self, root):
    self.root = root

    self.menu_frame = Frame(root)
    self.side_fliter = Frame(root)

    self.menu_frame.place(x = 325, y = 0)
    self.side_fliter.grid(row = 0 ,column = 0)

    btn1 = Button(root, text = "Sandwich", relief = "groove", command = None)
    btn2 = Button(root, text = "With Rice", relief = "groove", command = None)
    btn3 = Button(root, text = "Salads", relief = "groove", command = None)
    btn4 = Button(root, text = "Desserts", relief = "groove", command = None)
    btn5 = Button(root, text = "Drinks", relief = "groove")

    btn1.grid(sticky = "NW")
    btn2.grid(sticky = "NW")
    btn3.grid(sticky = "NW")
    btn4.grid(sticky = "NW")
    btn5.grid(sticky = "NW")
    







if __name__ == "__main__":
  root = Tk()
  root.title("Ormiston Senior College Cafe")
  root.geometry("750x500")
  root.update()
  root.minsize(root.winfo_width(), root.winfo_height())
  Menu(root)
  root.mainloop()