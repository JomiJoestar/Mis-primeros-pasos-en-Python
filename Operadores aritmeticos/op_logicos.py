

#AND
#Ambos valores deben ser verdaderos para que el and nos devuelva true

resultado = True & True #devolver true
resultado2 = False & False #devolver false
resultado3 = True & False #devolver false
resultado4 = False & False #devolver false

#OR
#Al menos uno de los valores debe ser verdadero para que el or nos devuelva true
#Si ambos valores son falsos nos devolverá false

resultado5 = True | False #devolver true
resultado6 = False | True #devolver true
resultado7 = True | False #devolver true
resultado8 = False | False #devolver false

#NOT
#Invierte el valor de verdad
#Es decir, si era true se convierte en false y viceversa

resultado9 = not True #devolver false
resultado10 = not False #devolver true

print(resultado)

#Jugando con los operadores logicos
#AND

edad = int(input("ingresa tu edad: "))
tiene_entrada = input("tienes entrada? (si o no): ") == "si"

if edad >= 18 and tiene_entrada:
    print("Puedes entrar a la party")
else:
    print("No puedes entrar")

#OR

es_vip = False
tiene_entrada = True

if es_vip or tiene_entrada:
    print("Puedes pasar")
else:
    print("No puedes pasar...")






