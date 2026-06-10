

# Las tuplas no se pueden alterar como las listas, y estas se usan con paréntesis.

# No podemos hacer esto
# tupla[0] = (10)
# tupla.append(60)

mi_tupla = (1,2,3,4,5,6,)

for elemento in mi_tupla:
    print(elemento, end=" ") # usa la coma para llamar al end

# Accedemos a cada elemento de la tupla
coordenadas = (3, 5)
print(f'\n Coordenada en el eje x: {coordenadas[0]}')
print(f'coordenada en el eje y: {coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10,
print(tupla_un_elemento)

# Tupla anidada
tupla_anidada =(1, (2,3), (4,5))
print(f'Segundo elemento de la tupla anidada {tupla_anidada[1]}')




