import tkinter as tk
from tkinter import ttk, messagebox
import random


class TravelBookingApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Vanshika Travels Booking Form")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root,
                               text="Welcome to Vanshika Travels",
                               font=("Arial", 18, "bold"),
                               bg="#f0f0f0",
                               fg="#333333")
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Frame for form
        form_frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        form_frame.grid(row=1, column=0, columnspan=2, padx=20, sticky="nsew")

        # Form fields
        fields = [("Name", "name"), ("Phone", "phone"), ("Gender", "gender"),
                  ("Emergency Contact", "emergency"),
                  ("Payment Mode", "paymentmode")]

        for i, (label_text, field_name) in enumerate(fields):
            label = tk.Label(form_frame,
                             text=label_text,
                             bg="#ffffff",
                             font=("Arial", 10, "bold"))
            label.grid(row=i, column=0, sticky="e", pady=10, padx=(0, 10))

            entry = ttk.Entry(form_frame, font=("Arial", 10))
            entry.grid(row=i, column=1, sticky="w")
            setattr(self, f"{field_name}_entry", entry)

        # Checkbutton for meal pre-booking
        self.meal_var = tk.BooleanVar()
        meal_check = ttk.Checkbutton(form_frame,
                                     text="Pre-book meals?",
                                     variable=self.meal_var)
        meal_check.grid(row=len(fields), column=0, columnspan=2, pady=10)

        # Submit button
        submit_button = ttk.Button(self.root,
                                   text="Submit Booking",
                                   command=self.submit_booking)
        submit_button.grid(row=2, column=0, columnspan=2, pady=20)

    def submit_booking(self):
        # Collect form data
        booking_data = {
            "Name": self.name_entry.get(),
            "Phone": self.phone_entry.get(),
            "Gender": self.gender_entry.get(),
            "Emergency Contact": self.emergency_entry.get(),
            "Payment Mode": self.paymentmode_entry.get(),
            "Meal Pre-booked": "Yes" if self.meal_var.get() else "No"
        }

        # Validate data (basic check for empty fields)
        if any(value.strip() == "" for value in booking_data.values()):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Display booking confirmation
        confirmation = "Booking Confirmed!\n\n" + "\n".join(
            f"{k}: {v}" for k, v in booking_data.items())
        messagebox.showinfo("Booking Confirmation", confirmation)

        # Clear form fields
        for entry in [
                self.name_entry, self.phone_entry, self.gender_entry,
                self.emergency_entry, self.paymentmode_entry
        ]:
            entry.delete(0, tk.END)
        self.meal_var.set(False)


if __name__ == "__main__":
    root = tk.Tk()
    app = TravelBookingApp(root)
    root.mainloop()
