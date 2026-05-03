
#creando una lista (se puede mopdificar)
lista = ["Jomi Joestar", "Soy Jomi", True, 1.65]

#Creando una tupla (no se puede modificar)
tupla = ("Jomi Joestar", "Soy Jomi", True, 1.65)

#Esto es valido 
lista[3] = "Jomi Noxus BW"

#Esto no

#tupla[3] = "Jomi Noxus BW"

print(lista[3])

#Creando un conunto, solo se crea con llaves, no se pueden repetir elementos
#No se puede llamar a los elementos por su indice, no alamacena datos duplicados

conjunto = {"Jomi Joestar", "Soy Jomi", True, 1.65}

#print(conjunto[3]) -> no puede acceder al elemento

#Creando un diccionario (dict) (la estructura es key : value y separamos con comas en caso de...)
#que haya mas elementos, es decir si tienes 4 elementos son 3 comas.)
diccionario = {
    'nombre' : "Jomi Joestar",
    'anime_favorito' : "Jojos",
    'esta_emocionada' : True,
    'altura' : 1.65,
    'dato_duplicado': "Jojos",
}

print(diccionario['anime_favorito'])




