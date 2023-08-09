import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Sample data for the dropdown menu
menu_items = [
    {"name": "Chips and Pillau", "price": 4000},
    {"name": "Chips and Liver", "price": 5000},
    {"name": "chips and Chicken", "price": 7000}
]

def calculate_total():
    total = 0
    for item in items_list:
        total += item["quantity"] * item["price"]
    return total

def generate_receipt():
    # Create the receipt content
    receipt_content = "SSEBANKYAYE RESTAURANT\n"
    receipt_content += "Jjunju Rd, Kampala\n"
    receipt_content += "+256 704 590401\n"
    receipt_content += f"Date & Time: {receipt_date.get()} {receipt_time.get()}\n"
    receipt_content += f"Receipt Number: {receipt_number.get()}\n"
    receipt_content += f"Customer: {customer_name.get()}\n\n"
    receipt_content += "Item\t\tQuantity\tUnit Cost\tItem Cost\n"
    receipt_content += "----------------------------------------------------------------------------\n"
    for item in items_list:
        receipt_content += f"{item['name']}\t\t{item['quantity']}\t\t{item['price']}\t\t{item['quantity'] * item['price']}\n"
    receipt_content += "----------------------------------------------------------------------------\n"
    receipt_content += f"Total:\t\t\t\t\t\t{calculate_total()}\n\n"
    receipt_content += "Signature: ___________________________\n\n"
    receipt_content += "Thank you for dining with us!"

    # Display the receipt in a messagebox
    messagebox.showinfo("Receipt", receipt_content)

def add_item():
    selected_item = menu.get()
    quantity = quantity_entry.get()
    if selected_item and quantity:
        item = next((item for item in menu_items if item["name"] == selected_item), None)
        if item:
            item_data = {
                "name": item["name"],
                "quantity": int(quantity),
                "price": item["price"]
            }
            items_list.append(item_data)
            update_items_list()
        else:
            messagebox.showerror("Error", "Invalid item selected!")
    else:
        messagebox.showerror("Error", "Please select an item and enter the quantity!")

def update_items_list():
    items_text.delete("1.0", tk.END)
    for item in items_list:
        items_text.insert(tk.END, f"{item['name']} - Quantity: {item['quantity']}\n")

# Create the main window
window = tk.Tk()
window.title("Restaurant Receipt Generator")

# Create labels and entry fields for receipt details
receipt_date_label = tk.Label(window, text="Date:")
receipt_date_label.grid(row=0, column=0, sticky="E")
receipt_date = tk.StringVar()
receipt_date_entry = tk.Entry(window, textvariable=receipt_date)
receipt_date_entry.grid(row=0, column=1)
receipt_date.set(datetime.now().date())  # Automatically set the current date

receipt_time_label = tk.Label(window, text="Time:")
receipt_time_label.grid(row=1, column=0, sticky="E")
receipt_time = tk.StringVar()
receipt_time_entry = tk.Entry(window, textvariable=receipt_time)
receipt_time_entry.grid(row=1, column=1)
receipt_time.set(datetime.now().time().strftime('%H:%M:%S'))  # Automatically set the current time

receipt_number_label = tk.Label(window, text="Receipt Number:")
receipt_number_label.grid(row=2, column=0, sticky="E")
receipt_number = tk.StringVar()
receipt_number_entry = tk.Entry(window, textvariable=receipt_number)
receipt_number_entry.grid(row=2, column=1)

customer_name_label = tk.Label(window, text="Customer Name:")
customer_name_label.grid(row=3, column=0, sticky="E")
customer_name = tk.StringVar()
customer_name_entry = tk.Entry(window, textvariable=customer_name)
customer_name_entry.grid(row=3, column=1)

# Create a dropdown menu for item selection
menu_label = tk.Label(window, text="Menu Item:")
menu_label.grid(row=4, column=0, sticky="E")
menu = tk.StringVar(window)
menu.set(menu_items[0]["name"])
menu_dropdown = tk.OptionMenu(window, menu, *[item["name"] for item in menu_items])
menu_dropdown.grid(row=4, column=1, sticky="W")

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.grid(row=5, column=0, sticky="E")
quantity_entry = tk.Entry(window)
quantity_entry.grid(row=5, column=1)

add_button = tk.Button(window, text="Add Item", command=add_item)
add_button.grid(row=6, columnspan=2)

# Create a listbox to display the items added
items_label = tk.Label(window, text="Items:")
items_label.grid(row=7, column=0, sticky="W")
items_text = tk.Text(window, height=5, width=40)
items_text.grid(row=8, columnspan=2)

# Create a button to generate the receipt
generate_button = tk.Button(window, text="Generate Receipt", command=generate_receipt)
generate_button.grid(row=9, columnspan=2, pady=10)

items_list = []

# Start the main GUI loop
window.mainloop()
