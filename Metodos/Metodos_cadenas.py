cadena1 = "Hola soy Jomi"
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
busqueda_find = cadena1.find("J")

#buscamos una cadena en otra cadena, casi igual que el find pero da error si no existe (lanza una excepcion)
busqueda_index = cadena1.index("J")
print(busqueda_index)



