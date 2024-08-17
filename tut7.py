import tkinter as tk
from tkinter import colorchooser, messagebox
import random


class EnhancedCanvasGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Canvas GUI")
        self.canvas_width = 800
        self.canvas_height = 500
        self.root.geometry(f"{self.canvas_width}x{self.canvas_height + 50}"
                           )  # Extra space for buttons

        self.setup_canvas()
        self.create_buttons()
        self.setup_bindings()

    def setup_canvas(self):
        self.canvas = tk.Canvas(self.root,
                                width=self.canvas_width,
                                height=self.canvas_height,
                                bg="white")
        self.canvas.pack()

        # Initial shapes
        self.canvas.create_line(0,
                                0,
                                self.canvas_width,
                                self.canvas_height,
                                tags="deletable")
        self.canvas.create_line(0,
                                self.canvas_height,
                                self.canvas_width,
                                0,
                                tags="deletable")
        self.canvas.create_rectangle(50,
                                     50,
                                     200,
                                     200,
                                     fill="red",
                                     tags="deletable")
        self.canvas.create_text(100,
                                100,
                                text="Hello World",
                                font=("Arial", 14),
                                tags="deletable")
        self.canvas.create_oval(50,
                                50,
                                200,
                                200,
                                outline="blue",
                                width=2,
                                tags="deletable")

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Button(button_frame, text="Clear Canvas",
                  command=self.clear_canvas).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame,
                  text="Add Random Shape",
                  command=self.add_random_shape).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame,
                  text="Change Background",
                  command=self.change_background).pack(side=tk.LEFT, padx=5)

    def setup_bindings(self):
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def clear_canvas(self):
        self.canvas.delete("deletable")

    def add_random_shape(self):
        x1, y1 = random.randint(0, self.canvas_width), random.randint(
            0, self.canvas_height)
        x2, y2 = x1 + random.randint(50, 150), y1 + random.randint(50, 150)
        color = f"#{random.randint(0, 0xFFFFFF):06x}"

        shape = random.choice(["rectangle", "oval", "line", "text"])
        if shape == "rectangle":
            self.canvas.create_rectangle(x1,
                                         y1,
                                         x2,
                                         y2,
                                         fill=color,
                                         tags="deletable")
        elif shape == "oval":
            self.canvas.create_oval(x1,
                                    y1,
                                    x2,
                                    y2,
                                    fill=color,
                                    tags="deletable")
        elif shape == "line":
            self.canvas.create_line(x1,
                                    y1,
                                    x2,
                                    y2,
                                    fill=color,
                                    width=3,
                                    tags="deletable")
        else:
            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2,
                                    text="Random Text",
                                    fill=color,
                                    font=("Arial", 14),
                                    tags="deletable")

    def change_background(self):
        color = colorchooser.askcolor(title="Choose background color")[1]
        if color:
            self.canvas.configure(bg=color)

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        self.canvas.create_line(self.last_x,
                                self.last_y,
                                event.x,
                                event.y,
                                width=2,
                                tags="deletable")
        self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        pass  # You can add functionality here if needed


if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedCanvasGUI(root)
    root.mainloop()
