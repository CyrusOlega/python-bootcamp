def add(name, price, quantity, cart):
    cart.append({"name": name, "price": price, "quantity": quantity})

def remove(name, cart):
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            return

def show_all(cart):
    print(cart)

def show_total(cart):
    total = 0
    for item in cart:
        total = total + (item["price"]*item["quantity"])

    print(f"Total: {total:,.2f}")

def cart_app():
    cart = []
    finished = False

    while not finished:
        action = input("Enter action: ").lower().strip()

        if action == "add":
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            add(name, price, quantity, cart)
        elif action == "remove":
            name = input("Enter name: ")
            remove(name, cart)
        elif action == "total":
            show_total(cart)
        elif action == "show":
            show_all(cart)
        elif action == "exit":
            finished = True
        else:
            print("Invalid action")

cart_app()