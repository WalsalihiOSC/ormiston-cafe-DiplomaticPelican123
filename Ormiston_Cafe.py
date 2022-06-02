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
    







if __name__ == "__main__":
  root = Tk()
  root.title("Ormiston Senior College Cafe")
  root.geometry("750x500")
  Main(root)
  root.mainloop()