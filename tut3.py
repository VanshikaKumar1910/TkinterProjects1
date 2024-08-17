from tkinter import *
from tkinter import messagebox
import random


class EnhancedGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Button GUI")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Frame
        self.frame = Frame(self.root,
                           borderwidth=6,
                           bg="lightgrey",
                           relief=SUNKEN)
        self.frame.pack(side=LEFT, anchor="nw", padx=10, pady=10, fill=Y)

        # Buttons
        self.create_button("Print Hello", self.print_hello, "#FF6B6B")
        self.create_button("Show Message", self.show_message, "#4ECDC4")
        self.create_button("Change Color", self.change_color, "#45B7D1")
        self.create_button("Count Clicks", self.count_clicks, "#F7B801")
        self.create_button("Exit", self.exit_app, "#FF6B6B")

        # Label for click count
        self.click_count = 0
        self.count_label = Label(self.root,
                                 text="Clicks: 0",
                                 bg="#f0f0f0",
                                 font=("Helvetica", 12))
        self.count_label.pack(pady=20)

    def create_button(self, text, command, color):
        button = Button(self.frame,
                        text=text,
                        command=command,
                        bg=color,
                        fg="white",
                        font=("Helvetica", 10, "bold"),
                        padx=10,
                        pady=5)
        button.pack(fill=X, padx=5, pady=5)

    def print_hello(self):
        print("Hello Tkinter buttons")

    def show_message(self):
        messagebox.showinfo("Greetings", "Hello! This is a custom message.")

    def change_color(self):
        colors = [
            "#FF6B6B", "#4ECDC4", "#45B7D1", "#F7B801", "#96CEB4", "#FFEEAD"
        ]
        self.root.configure(bg=random.choice(colors))

    def count_clicks(self):
        self.click_count += 1
        self.count_label.config(text=f"Clicks: {self.click_count}")

    def exit_app(self):
        if messagebox.askokcancel("Exit",
                                  "Do you want to exit the application?"):
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = EnhancedGUI(root)
    root.mainloop()
