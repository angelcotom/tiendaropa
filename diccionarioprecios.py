almacen = {}
ropa = int(input("Ingrese cuántas prendas desea ingresar: "))

# Contador de categoría
categorias_contador = {"Mujer": 0, "Hombre": 0, "Niño": 0}

for i in range(ropa):
    print(f"\nPrenda {i+1}")
    codigo = input("Ingrese código: ")
    while codigo in almacen:
        print(" Este codigo ya existe verificque el codigo.")
        codigo =input("Ingrese codigo de la prenda ")

    nombre = input("Ingrese nombre de la prenda: ")

    categoria = input("Ingrese categoría (Mujer, Hombre, Niño): ").capitalize()
    categorias_contador[categoria] += 1
    while categoria not in categorias_contador:
        print(" Categoría inválida. Debe ser Mujer, Hombre o Niño.")
        categoria = input("Ingrese categoría (Mujer, Hombre, Niño): ").capitalize()


    talla = input("Ingrese talla (S, M, L, XL): ")

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
#mostrar valor de el invventario
print("\n¿Desea calcular el valor total del inventario?")
confirmacion = input("Sí o no (S/N): ").strip().upper()


if confirmacion == "S":
    total = 0
    for prenda in almacen.values():
        total += prenda["precio_U"] * int(prenda["cantidadStok"])
    print(f"\n Valor total del inventario: Q{total:.2f}")

elif confirmacion == "N":
    print(" No se calculará el valor del inventario.")
else:
    print("Opción no válida. Escriba 'S' o 'N'.")

# Mostrar cuántas prendas hay por categoría
print("\n Prendas por Categoría:")
for cat, cantidad in categorias_contador.items():
    print(f"{cat}: {cantidad} prendas")