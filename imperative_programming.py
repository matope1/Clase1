# Gestión de categorías...
categories = [
    {"name": "Electronics", "description": "Devices and gadgets"},
    {"name": "Office", "description": "Office supplies and equipment"}
]

# Gestión de etiquetas (tags)
tags = [
    {"name": "On Sale"},
    {"name": "New Arrival"},
    {"name": "Best Seller"}
]

# Gestión de productos
products = [
    {"name": "Laptop", "sku": "SKU123", "price": 1200, "current_stock": 10, "categories": [categories[0]], "tags": [tags[1], tags[2]]},
    {"name": "Mouse", "sku": "SKU456", "price": 25, "current_stock": 100, "categories": [categories[0]], "tags": [tags[0]]},
    {"name": "Keyboard", "sku": "SKU789", "price": 50, "current_stock": 50, "categories": [categories[1]], "tags": [tags[2]]},
    {"name": "Monitor", "sku": "SKU101", "price": 300, "current_stock": 20, "categories": [categories[0]], "tags": []}
]

# Gestión del inventario
inventory = {product["sku"]: product for product in products}

inventory = {}
for product in products:
    inventory[product["sku"]] = product

# Ejemplo ejecucion:
# Antes de iniciar:
# {}
# Tras primera vuelta:
# {"SFU123": {"name": "Laptop", "sku": "...,}
# Tras segunda vuelta:
# {"SFU123": {"name": "Laptop", "sku": "...,
# "SKU456": {"name": "Mouse", "sku": "SKU456", "price": 25,...
# }
# Tras tercera
# {"SFU123": "Producto 1, con todos sus datos...",
# "SKU456": "Producto 2..."
# }


# Procesar pedidos
orders = [
    {"order_id": "ORDER001", "items": {"SKU123": 7, "SKU456": 5}},
    {"order_id": "ORDER002", "items": {"SKU123": 5, "SKU789": 3, "SKU101": 1}},
    {"order_id": "ORDER003", "items": {"SKU456": 10, "SKU101": 2}}
]

""" for order in orders:
    order_id = order["order_id"]
    items = order["items"]
    total = 0
    for sku, quantity in items.items():
        product = inventory.get(sku)
        if not product:
            print(f"Error: Product with SKU {sku} not found.")
            continue
        if product["current_stock"] < quantity:
            print(f"Error: Insufficient stock for {product['name']}. Available: {product['current_stock']}, Requested: {quantity}")
            available_before_updating = product["current_stock"]
            product["current_stock"] = 0 # Actualizar el stock quitando lo que se ha llevado en ese pedido.
            total += product["price"] * product["current_stock"]
            print(f"Pero le vendo {available_before_updating}")
            continue
        # Actualizar el stock
        product["current_stock"] -= quantity # Actualizar el stock quitando lo que se ha llevado en ese pedido.
        total += product["price"] * quantity
    print(f"Order ID: {order_id} - Total: ${total:.2f} - Purchase Completed")

 """

def update_stock(product, units_sold):
    current_stock = product["current_stock"]
    final_stock = current_stock - units_sold
    product["current_stock"] = final_stock
    print(f'Your new stock for product {product["name"]} is {final_stock} units')
    return product


# Grupo 4: una función para procesar una lista de orders
def process_orders(orders):

    for order in orders:
        order_id = order["order_id"]
        items = order["items"]
        total = 0

        print(order_id, items, total)

        for sku, requested_units in items.items():
            product = inventory.get(sku)

            stock_available, units_sol = check_stock_for_product(product, requested_units)

            if stock_available:

                update_stock(product, units_sol)

    show_inventory(inventory)

