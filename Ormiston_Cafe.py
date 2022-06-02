from tkinter import *

class Main:
  def __init__(self, root):

    self.root = root

    intro_frame = Frame(root, width = 250, height = 250, highlightbackground = "black", highlightthickness = 1)
    intro_frame.place(x = 250, y = 100)

    intro_label = Label(intro_frame, text = "Ormiston Senior College Maca's", anchor = CENTER)
    intro_label.place(x = 35, y = 110)

    osc_logo = PhotoImage("Image/osc_logo.jpg")

    img_label = Label(root, image = osc_logo, width=250, height=250)
    img_label.grid()
    







if __name__ == "__main__":
  root = Tk()
  root.title("Ormiston Senior College Cafe")
  root.geometry("750x500")
  Main(root)
  root.mainloop()