items = {}
def menu():
    print("1.Add item")
    print("2.Remove item")
    print("3.View items")
    print("4.Update item")
    print("5.Clear stock")
    print("6.Exit")

def add_item():
    item_name = input("Enter item name: ")
    item_quatity = int(input("Enter item quantity: "))
    item_price = float(input("Enter item price: "))
    
    items[item_name] = [item_quatity, item_price]
    print(f"{item_name} added successfully!")

def remove_item():
    seach_item = input("Enter item name to remove: ")
    if seach_item in items:
        del items[seach_item]
        print(f"{seach_item} removed successfully!")
    else:
        print(f"{seach_item} not found!")   

def view_items():
    if items:
        print("Items in stock:")
        for item, details in items.items():
            print(f"{item}: {details[0]} units at {details[1]} each")
    else:
        print("No items in stock.")        

def update_item():
    item_name = input("Enter item name to update: ")

    if item_name in items:
        item_quatity = int(input("Enter new item quantity: "))
        item_price = float(input("Enter new item price: "))
        items[item_name] = [item_quatity, item_price]
        print(f"{item_name} updated successfully!")

def clear_stock():
    items.clear()
    print("All items cleared from stock.")

def main():
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        view_items()
    elif choice == 4:
        update_item()
    elif choice == 5:
        clear_stock()
    elif choice == 6:
       print("Exiting...")
       exit() 


if __name__ == "__main__":
    while True:
        menu()
        main()
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting...")
            break
    
