


#Ejercicio numero 3
#numero1 = int(input("ingresa un primer numero: "))
#numero2 = int(input("ingresa un segundo numero: "))
#numero3 = int(input("ingresa un tercer numero: "))

""" if numero1 > numero2 and numero1 > numero3:
    print("Tu primer numero es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print("Tu segundo numero es el mayor...")
elif numero3 > numero1 and numero3 > numero2:
    print("Tu tercer numero es el mayor...")
else:
    print("Todos son iguales...") """

#Ejercicio numero 4
nota = int(input("Ingresa tu nota (0 a 100): "))
if nota >= 90 and nota <= 100:
    print("Excelente, keep going...")
elif nota >= 70 and nota <= 89:
    print("Bueno!")
elif nota >= 50 and nota <= 69:
    print("Estas regular... estudia mas!")
elif nota >= 0 and nota <= 49:
    print("Reprobaste, eres bruto")
else:
    print("Ingresa un numero valido, tonto")
    
    

producto_deseado = input("Ingrese el nombre de su producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_producto = int(input("Cantidad desada?:  "))
total = (precio_producto * cantidad_producto)

if total > 100:
    descuento = total * 0.10
    total_final = total - descuento
    print("Obtienes un descuento del 10% ", descuento)
    print("Total a pagar", total_final)
else: 
    print("No aplicas para el descuento")
    print("Total a pagar:", total)
