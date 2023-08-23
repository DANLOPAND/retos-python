# Diccionario de categorías
categorias = [
    {
        "id": 1,
        "name": "Utiles escolares"
    },
    {
        "id": 2,
        "name": "Aseo"
    }
]

# Diccionario de productos
products = [
    {
        "id": 123,
        "name": "Libreta",
        "price": 12.500,
        "id_cat": 1
    },
    {
        "id": 345,
        "name": "Jabón",
        "price": 10.500,
        "id_cat": 2
    }
]

product_category_map = {}
for product in products:
    for category in categorias:
        if product["id_cat"] == category["id"]:
            product_category_map[product["name"]] = category["name"]
            break  

for product_name, category_name in product_category_map.items():
    print(f"Producto: {product_name} - Categoría: {category_name}")