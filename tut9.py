import tkinter as tk
from tkinter import ttk, messagebox
import random


class EnhancedEventGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Event Handling in Tkinter")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.click_count = 0
        self.last_click_pos = None

        self.create_widgets()
        self.setup_bindings()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Styled button
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=10)
        self.click_button = ttk.Button(main_frame,
                                       text="Click me please!",
                                       command=self.button_click)
        self.click_button.pack(pady=20)

        # Labels
        self.click_label = ttk.Label(main_frame,
                                     text="Click count: 0",
                                     font=("Arial", 12))
        self.click_label.pack()

        self.pos_label = ttk.Label(main_frame,
                                   text="Last click position: None",
                                   font=("Arial", 12))
        self.pos_label.pack()

        # Canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=400, height=200, bg="white")
        self.canvas.pack(pady=20)

        # Color change button
        self.color_button = ttk.Button(main_frame,
                                       text="Change Canvas Color",
                                       command=self.change_canvas_color)
        self.color_button.pack()

    def setup_bindings(self):
        self.click_button.bind('<Button-1>', self.left_click)
        self.click_button.bind('<Button-3>', self.right_click)
        self.canvas.bind('<B1-Motion>', self.draw)

    def button_click(self):
        self.click_count += 1
        self.click_label.config(text=f"Click count: {self.click_count}")

    def left_click(self, event):
        self.last_click_pos = (event.x, event.y)
        self.pos_label.config(
            text=f"Last click position: {self.last_click_pos}")
        messagebox.showinfo("Left Click",
                            f"You left-clicked at {event.x}, {event.y}")

    def right_click(self, event):
        self.last_click_pos = (event.x, event.y)
        self.pos_label.config(
            text=f"Last click position: {self.last_click_pos}")
        messagebox.showinfo("Right Click",
                            f"You right-clicked at {event.x}, {event.y}")

    def draw(self, event):
        x, y = event.x, event.y
        r = 5  # Radius of the circle
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")

    def change_canvas_color(self):
        colors = ["#FFD1DC", "#E0BBE4", "#957DAD", "#D291BC", "#FEC8D8"]
        self.canvas.config(bg=random.choice(colors))


if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedEventGUI(root)
    root.mainloop()
