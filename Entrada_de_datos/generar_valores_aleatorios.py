


# Valorea aleatorios con la funcion radint

#'''significa: “Del módulo random, tráeme solamente la función randint para poder usarla en mi programa”.'''
#Python trae muchas funciones guardadas en “módulos”. El módulo se llama random, y dentro de ese módulo existe una función llamada randint()
from random import randint

# Generar un numero aleatorio entre 1 y 10 

numero = randint(1,10)
print(f'numero aleatorio entre 1 y 10: {numero}')

#Simular dado de seis caras
dado = randint(1,6)
print(f'el numero del dado es: {dado}')

