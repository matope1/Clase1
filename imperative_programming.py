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
# print(50*'*')
# print(inventory)

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

for order in orders:
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

    
# Mostrar estado final del inventario
print("\nInventory Report:\n")
for product in inventory.values():
    category_names = ", ".join([cat["name"] for cat in product["categories"]]) or "None"
    tag_names = ", ".join([tag["name"] for tag in product["tags"]]) or "None"
    print(f"Product: {product['name']} (SKU: {product['sku']}) - Price: ${product['price']:.2f}, Stock: {product['current_stock']}, Categories: [{category_names}], Tags: [{tag_names}]")




# Grupo 1: Una función que recibe un producto y una cantidad pedida, comprueba si hay suficiente stock y devuelve dos elementos: un boolean indicando si hay suficiente, y la cantidad máxima que se podría vender.

def check_stock_for_product(product, requested_units):
    exist_stock = product["current_stock"] >= requested_units
    product_stock = product["current_stock"]

    if exist_stock : 
        return exist_stock, requested_units
    else:
        return exist_stock , product_stock
    
a , q = check_stock_for_product({"name": "Laptop", "sku": "SKU123", "price": 1200, "current_stock": 10}, 7)
print(a, q)


def show_inventory(inventory):
    for p in inventory.values():
        name = p["name"]
        price = p["price"]
        current_stock = p["current_stock"]
        categories = p["categories"]
        tags = p["tags"]

        #* Mostramos los 3 primeros valores
        print(f'Nombre del producto: {name}')
        print(f'Precio: {price}')
        print(f'Stock actual: {current_stock}')

        #* Mostramos las categorías
        for c in categories:
            print(f'Categoría: {c["name"]}')
            print(f'Descripción: {c["description"]}')

        #* Mostramos los Tags
        tags_str = ', '.join([tag["name"] for tag in tags])
        print(f'Tags: {tags_str}')

        print('---------------------------------------')




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


