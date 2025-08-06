import json
import getpass

data_file = "inventory_data.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def login():
    print("Login")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    return username == "admin" and password == "admin123"

def add_product():
    data = load_data()
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per unit: "))
    data[product_id] = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    save_data(data)
    print("Product added successfully.")

def update_stock():
    data = load_data()
    product_id = input("Enter Product ID to update: ")
    if product_id in data:
        quantity = int(input("Enter quantity to add: "))
        data[product_id]["quantity"] += quantity
        save_data(data)
        print("Stock updated successfully.")
    else:
        print("Product not found.")

def list_products():
    data = load_data()
    print("Product List")
    for pid, info in data.items():
        print(f"ID: {pid}, Name: {info['name']}, Quantity: {info['quantity']}, Price: ₹{info['price']}")

def checkout():
    data = load_data()
    product_id = input("Enter Product ID to buy: ")
    if product_id in data:
        quantity = int(input("Enter quantity to buy: "))
        if quantity <= data[product_id]["quantity"]:
            total = quantity * data[product_id]["price"]
            data[product_id]["quantity"] -= quantity
            save_data(data)
            print(f"Checkout successful. Total: ₹{total}")
        else:
            print("Not enough stock.")
    else:
        print("Product not found.")

def generate_report():
    data = load_data()
    print("Inventory Report")
    total_value = 0
    for pid, info in data.items():
        value = info["quantity"] * info["price"]
        total_value += value
        print(f"{info['name']}: {info['quantity']} units @ ₹{info['price']} = ₹{value}")
    print(f"Total Inventory Value: ₹{total_value}")

def main():
    if login():
        while True:
            print("\nInventory Management System")
            print("1. Add Product")
            print("2. Update Stock")
            print("3. List Products")
            print("4. Checkout")
            print("5. Generate Report")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                add_product()
            elif choice == "2":
                update_stock()
            elif choice == "3":
                list_products()
            elif choice == "4":
                checkout()
            elif choice == "5":
                generate_report()
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
    else:
        print("Login failed.")

main()
