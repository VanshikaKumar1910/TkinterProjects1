import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import os


class AestheticNotepad:

    def __init__(self, master):
        self.master = master
        self.master.title("Vanshika's Notepad")
        self.master.geometry("800x600")
        self.master.configure(bg="#2E3440")

        self.filename = None

        self.create_widgets()
        self.set_styles()

    def create_widgets(self):
        # Create a frame for the toolbar
        self.toolbar = ttk.Frame(self.master, style="Toolbar.TFrame")
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Create toolbar buttons
        self.new_button = ttk.Button(self.toolbar,
                                     text="New",
                                     command=self.new_file)
        self.new_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.open_button = ttk.Button(self.toolbar,
                                      text="Open",
                                      command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = ttk.Button(self.toolbar,
                                      text="Save",
                                      command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the main text area
        self.text_area = tk.Text(self.master,
                                 wrap=tk.WORD,
                                 bg="#3B4252",
                                 fg="#E5E9F0",
                                 insertbackground="#E5E9F0")
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Create a status bar
        self.status_bar = ttk.Label(self.master,
                                    text="Ready",
                                    style="StatusBar.TLabel")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Configure colors
        style.configure(".", background="#2E3440", foreground="#E5E9F0")
        style.configure("TButton",
                        padding=6,
                        relief="flat",
                        background="#4C566A",
                        foreground="#E5E9F0")
        style.map("TButton", background=[("active", "#5E81AC")])
        style.configure("Toolbar.TFrame", background="#2E3440")
        style.configure("StatusBar.TLabel",
                        background="#4C566A",
                        foreground="#E5E9F0",
                        padding=5)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.status_bar.config(text="New File")

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[
                                                       ("Text Files", "*.txt"),
                                                       ("All Files", "*.*")
                                                   ])
        if self.filename:
            self.text_area.delete(1.0, tk.END)
            with open(self.filename, "r") as file:
                self.text_area.insert(1.0, file.read())
            self.status_bar.config(
                text=f"Opened: {os.path.basename(self.filename)}")

    def save_file(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.status_bar.config(
                text=f"Saved: {os.path.basename(self.filename)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AestheticNotepad(root)
    root.mainloop()
