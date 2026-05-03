
producto_deseado = input("Nombre del producto?: ")
precio_producto = float(input("Ingrese el precio del producto?: "))
cantidad = int(input("Ingrese cantidad deseada: "))

total = (precio_producto * cantidad)

if total > 100:
    descuento = total * 0.10 
    total_final = total - descuento
    print("Descuento aplicado del 10%",producto_deseado , total_final )

elif total > 50:
    descuento = total * 0.05
    total_final = total - descuento
    print("Descuento aplicado del 5%",producto_deseado ,total_final )
else:
    print("No aplicas para el descuento, sigue comprando... ")
    

