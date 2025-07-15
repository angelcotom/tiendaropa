almacen={}
ropa=int(input(f"ingrese cuantas prendas desea ingresar: "))
for i in range(ropa):
    print(f"Prenda{i+1} ")
    codigo=input("ingrese codigo : ")
    nombre=input("ingrese nombre de la prenda : ")
    categoria=input("ingrese categoria :")
    talla=input("ingrese talla : ")
    precio_U=input("ingrese precio U =Q ")
    cantidadStok=input("ingrese cantidad en stock :")
    almacen[codigo]={
        "nombre":nombre,
        "categoria":categoria,
        "precio_U":precio_U,
        "cantidadStok":cantidadStok,
        "talla":talla,
    }
print("\nLista de Productos: ")
for codigo,aux in almacen.items():
    print(f"codigo: {codigo}")
    print(f"nombre: {aux}")
    print(f"categoria: {aux['categoria']}")
    print(f"precio_U: {aux['precio_U']}")
    print(f"cantidadStok: {aux['cantidadStok']}")
    print(f"talla: {aux['talla']}")
print("Que prenda desea buscar")
buscar=input("ingrese codigo de la prenda: ")
if buscar in almacen:
    print(f"nombre: {almacen[buscar]['nombre']}")
    print(f"categoria: {almacen[buscar]['categoria']}")
    print(f"precio_U: {almacen[buscar]['precio_U']}")
    print(f"cantidadesStok: {almacen[buscar]['cantidadStok']}")
    print(f"talla: {almacen[buscar]['talla']}")
else:
    print(f"producto no existe")






