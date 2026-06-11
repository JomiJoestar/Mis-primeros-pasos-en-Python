

print('~~Combinando Listas y Tuplas~~')


# definir una lista que almacena tuplas de productos

productos = [
    ('P001', 'Camiseta', 20.0 ),
    ('P002', 'Jeans', 30.0),
    ('P003', 'Sudadera', 40.0),
]

#imprimir la info de cada producto
# y ademas calculamos el precio total

precio_total = 0

print('Informacion de los productos')
for producto in productos:
    # aplicamos el concepto de unpacking de tuplas
    # llamamos los nombres y lo igualamos a la lista
    # que contiene las tuplas, y asi se ira separando cada
    # elemento de la tupla.
    # como se esta realizando en la siguiente linea

    id, descripcion, precio = producto # este es el unpacking

    print(f'Producto: id = {id}, Descripcion = {descripcion}, Precio: {precio} ')

    #suma iterativa para calcular el precio total
    precio_total += precio #o si no hemos desempaquetado la tupla, podemos acceder al indice
    # producto[0]

print(f'Precio total de los productos: ${precio_total}')


# Esta es otra manera de realizarlo pero mas corto

for id, descripcion, precio in productos:
    print(f'Producto: id = {id}, Descripcion = {descripcion}, Precio: {precio}')
    precio_total += precio

