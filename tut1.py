from tkinter import *
from tkinter import ttk
import random


class EnhancedGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Tkinter GUI")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")

        self.colors = ["#FFD1DC", "#E0BBE4", "#957DAD", "#D291BC", "#FEC8D8"]
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Left Frame
        self.left_frame = Frame(self.root,
                                bg="#e0e0e0",
                                width=200,
                                relief=RAISED,
                                borderwidth=2)
        self.left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

        Label(self.left_frame,
              text="Project Tkinter-Python",
              bg="#e0e0e0",
              font=("Helvetica", 12, "bold")).pack(pady=20)

        # Task Entry
        self.task_entry = ttk.Entry(self.left_frame, font=("Helvetica", 10))
        self.task_entry.pack(padx=10, fill=X)

        ttk.Button(self.left_frame, text="Add Task",
                   command=self.add_task).pack(pady=10)

        # Right Frame (Task List)
        self.right_frame = Frame(self.root, bg="#f0f0f0")
        self.right_frame.pack(side=RIGHT,
                              fill=BOTH,
                              expand=True,
                              padx=10,
                              pady=10)

        self.task_canvas = Canvas(self.right_frame, bg="#ffffff")
        self.task_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.right_frame,
                                  orient=VERTICAL,
                                  command=self.task_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.task_canvas.configure(yscrollcommand=scrollbar.set)
        self.task_canvas.bind(
            '<Configure>', lambda e: self.task_canvas.configure(
                scrollregion=self.task_canvas.bbox("all")))

        self.inner_frame = Frame(self.task_canvas, bg="#ffffff")
        self.task_canvas.create_window((0, 0),
                                       window=self.inner_frame,
                                       anchor="nw")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            color = random.choice(self.colors)
            task_frame = Frame(self.inner_frame,
                               bg=color,
                               relief=RAISED,
                               borderwidth=1)
            task_frame.pack(fill=X, padx=5, pady=5)

            Label(task_frame, text=task, bg=color,
                  font=("Helvetica", 10)).pack(side=LEFT, padx=5, pady=5)

            ttk.Button(task_frame,
                       text="Done",
                       command=lambda: self.remove_task(task_frame)).pack(
                           side=RIGHT, padx=5, pady=5)

            self.tasks.append(task_frame)
            self.task_entry.delete(0, END)
            self.update_canvas()

    def remove_task(self, task_frame):
        task_frame.destroy()
        self.tasks.remove(task_frame)
        self.update_canvas()

    def update_canvas(self):
        self.task_canvas.update_idletasks()
        self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all"))


if __name__ == "__main__":
    root = Tk()
    app = EnhancedGUI(root)
    root.mainloop()
