cadena1 = "HolasoyJomi"
cadena2 = "Aprendiendo metodos en python"

#lista de herramientas basicas para trabajar con texto en python
#DIR:(funcion) Muestra todo que podemos hacer con un objeto en especifico, sea texto, numero, lista... para cada objeto hay cosas diferentes que podemos utilizar
#print(dir("texto"))
#print(dir(7))
#print(dir(["texto"]))
#print(dir(("texto")))


#Metodos en python
# Dato.ELMETODO() siempre seguido de los parentesis

#convierte a mayusculas
mayusculas = cadena1.upper()

#convierte a minisculas
minusculas = cadena1.lower()

#primera letra en minisculas
primer_letra_mayus = cadena1.capitalize()

#buscamos una cadena en otra cadena 
#busca una letra y devuelve la posicion en la que se encuentra
#es key sensitive, es sensible a mayusculas y minisculas: Sino no hay mayusculas en el texto pondra -1 lo que significa que no esta, o no existe
busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, casi igual que el find pero da error si no existe (lanza una excepcion)
busqueda_index = cadena1.index("H")

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico, devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincide
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

print(mayusculas)
print(minusculas)
print(primer_letra_mayus)
print(busqueda_find)
print(busqueda_index)
print(es_alfanumerico)
print(contar_coincidencias)
print(contar_caracteres)


