
#PROGRAMA REEMPLAZAR TEXTOS EN PYTHON

mensaje = "Hola Mundo, Mundo"


# reemplazar TODAS las apariciones
nuevo = mensaje.replace("Mundo", "Python")
print(nuevo) #Salida: Hola Python, Python

#Esto quiere decir que hemos reemplazado todas las apariciones de "Mundo" por "Python"

# reemplazar SOLO la primera aparicion

uno_solo = mensaje.replace("Mundo", "Dev", 10)
print(uno_solo) #Salida: Hola Dev, Mundo

#Esto quiere decir que hemos reemplazado SOLO la primera aparicion de "Mundo" por "Python"
 