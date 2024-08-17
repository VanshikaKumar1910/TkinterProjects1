from tkinter import *


def hello(event):
  print(f"You clicked the button at {event.x}, {event.y}")


root = Tk()
root.title("Events in Tkinter")
root.geometry("666x333")

widget = Button(root, text="Click me please")
widget.pack()

widget.bind('<Button-1>', hello)

root.mainloop()
