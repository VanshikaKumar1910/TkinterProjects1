import tkinter as tk
from tkinter import ttk, messagebox
import random


class ColorfulTodoList:

    def __init__(self, master):
        self.master = master
        self.master.title("Colorful To-Do List")
        self.master.geometry("400x600")
        self.master.configure(bg="#F0F0F0")

        self.tasks = []
        self.colors = [
            "#FF9AA2", "#FFB7B2", "#FFDAC1", "#E2F0CB", "#B5EAD7", "#C7CEEA"
        ]

        self.create_widgets()
        self.set_styles()

    def create_widgets(self):
        # Title
        self.title_label = ttk.Label(self.master,
                                     text="My Colorful To-Do List",
                                     style="Title.TLabel")
        self.title_label.pack(pady=20)

        # Task entry
        self.task_frame = ttk.Frame(self.master, style="Task.TFrame")
        self.task_frame.pack(pady=10, padx=20, fill=tk.X)

        self.task_entry = ttk.Entry(self.task_frame,
                                    font=("Helvetica", 12),
                                    style="Task.TEntry")
        self.task_entry.pack(side=tk.LEFT,
                             expand=True,
                             fill=tk.X,
                             padx=(0, 10))

        self.add_button = ttk.Button(self.task_frame,
                                     text="Add Task",
                                     command=self.add_task,
                                     style="Add.TButton")
        self.add_button.pack(side=tk.RIGHT)

        # Task list
        self.task_list_frame = ttk.Frame(self.master, style="TaskList.TFrame")
        self.task_list_frame.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)

        self.task_canvas = tk.Canvas(self.task_list_frame,
                                     bg="#F0F0F0",
                                     highlightthickness=0)
        self.task_canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.scrollbar = ttk.Scrollbar(self.task_list_frame,
                                       orient=tk.VERTICAL,
                                       command=self.task_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.task_canvas.bind(
            '<Configure>', lambda e: self.task_canvas.configure(
                scrollregion=self.task_canvas.bbox("all")))

        self.inner_frame = ttk.Frame(self.task_canvas, style="Inner.TFrame")
        self.task_canvas.create_window((0, 0),
                                       window=self.inner_frame,
                                       anchor="nw",
                                       width=360)

    def set_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Title.TLabel",
                        font=("Helvetica", 18, "bold"),
                        foreground="#333333",
                        background="#F0F0F0")
        style.configure("Task.TFrame", background="#F0F0F0")
        style.configure("Task.TEntry",
                        fieldbackground="#FFFFFF",
                        foreground="#333333")
        style.configure("Add.TButton",
                        font=("Helvetica", 10),
                        background="#4CAF50",
                        foreground="#FFFFFF")
        style.map("Add.TButton", background=[("active", "#45a049")])
        style.configure("TaskList.TFrame", background="#F0F0F0")
        style.configure("Inner.TFrame", background="#F0F0F0")
        style.configure("Task.TCheckbutton", background="#F0F0F0")
        style.configure("Delete.TButton",
                        font=("Helvetica", 10),
                        background="#FF5252",
                        foreground="#FFFFFF")
        style.map("Delete.TButton", background=[("active", "#FF1744")])

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            color = random.choice(self.colors)
            task_frame = tk.Frame(self.inner_frame, bg=color)
            task_frame.pack(fill=tk.X, padx=5, pady=5)

            check_var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(
                task_frame,
                variable=check_var,
                command=lambda: self.toggle_task(task_label, check_var),
                style="Task.TCheckbutton")
            checkbox.pack(side=tk.LEFT, padx=5)

            task_label = tk.Label(task_frame,
                                  text=task,
                                  bg=color,
                                  font=("Helvetica", 12))
            task_label.pack(side=tk.LEFT,
                            pady=5,
                            padx=5,
                            fill=tk.X,
                            expand=True)

            delete_button = ttk.Button(
                task_frame,
                text="×",
                command=lambda: self.delete_task(task_frame),
                style="Delete.TButton")
            delete_button.pack(side=tk.RIGHT, padx=5)

            self.tasks.append((task_frame, check_var))
            self.task_entry.delete(0, tk.END)
            self.update_canvas()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task!")

    def toggle_task(self, label, check_var):
        if check_var.get():
            label.configure(font=("Helvetica", 12, "overstrike"))
        else:
            label.configure(font=("Helvetica", 12))

    def delete_task(self, task_frame):
        task_frame.destroy()
        self.tasks = [(frame, var) for frame, var in self.tasks
                      if frame != task_frame]
        self.update_canvas()

    def update_canvas(self):
        self.task_canvas.update_idletasks()
        self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorfulTodoList(root)
    root.mainloop()
