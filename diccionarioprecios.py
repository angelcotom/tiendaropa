almacen = {}
ropa = int(input("Ingrese cuántas prendas desea ingresar: "))

for i in range(ropa):
    print(f"\nPrenda {i+1}")
    codigo = input("Ingrese código: ")
    while codigo in almacen:
        print(" Este codigo ya existe verificque el codigo.")
        codigo =input("Ingrese codigo de la prenda ")

    nombre = input("Ingrese nombre de la prenda: ")
    categoria = input("Ingrese categoría: ")
    talla = input("Ingrese talla: ")

    precio_U = float(input("Ingrese precio U = Q "))
    while precio_U <= 0:
        print(" El precio debe ser mayor a 0.")
        precio_U = float(input("Ingrese precio U = Q "))

    cantidadStok = input("Ingrese cantidad en stock: ")

    almacen[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio_U": precio_U,
        "cantidadStok": cantidadStok,
        "talla": talla,
    }

# Mostrar productos
print("\nLista de Productos:")
for codigo, aux in almacen.items():
    print(f"\nCódigo: {codigo}")
    print(f"Nombre: {aux['nombre']}")
    print(f"Categoría: {aux['categoria']}")
    print(f"Precio U: Q{aux['precio_U']}")
    print(f"Cantidad en Stock: {aux['cantidadStok']}")
    print(f"Talla: {aux['talla']}")

# Buscar producto
print("\n ¿Qué prenda desea buscar?")
buscar = input("Ingrese código de la prenda: ")
if buscar in almacen:
    print(f"\n✔ Producto encontrado:")
    print(f"Nombre: {almacen[buscar]['nombre']}")
    print(f"Categoría: {almacen[buscar]['categoria']}")
    print(f"Precio U: Q{almacen[buscar]['precio_U']}")
    print(f"Cantidad en Stock: {almacen[buscar]['cantidadStok']}")
    print(f"Talla: {almacen[buscar]['talla']}")
else:
    print("Producto no existe.")
