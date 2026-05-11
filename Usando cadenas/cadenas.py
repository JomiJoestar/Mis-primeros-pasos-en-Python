


#CADENAS SIMPLES Y DOBLES
#CADENA SIMPLE
#Podemos usar '' para definir cadenas de texto
#Tambien podemos usar "" para definir cadenas de texto
#Tambien podemos combinar ambos tipos de comillas para resaltar comentarios o citas

cita = 'Ella dijo: "Hola, ¿cómo estás?"'
libro = "Cien años de soledad de 'Gabriel García Márquez'"

#CADENAS MULTILINEAS
#Podemos usar comillas triples para definir cadenas de texto que abarcan varias líneas

carta = """Querido amigo,
Espero que este mensaje te encuentre bien.
Quería compartir contigo algunas reflexiones sobre la vida y la amistad.
Un abrazo,
Tu amigo."""

poema = '''Rosas son rojas,
Violetas son azules,
El lenguaje de la poesía
Es un susurro en la brisa.'''


#CARACTERES ESPECIALES EN PYTHON 
# 1. \ BARRA INVERTIDA: COMILLAS DENTRO DE UNA CADENA
#saludo =  "ella dijo" hola"cuando regreso de vacaciones" #ESTO NO SE PUEDE

saludo_correcto = "ella dijo \"hola como estas\" cuando regreso de vacaciones" #ESTO SI SE PUEDE, USANDO EL CARACTER DE ESCAPE \

saludo_correcto2 = 'ella dijo \'hola como estas\' cuando regreso de vacaciones' #ESTO TAMBIEN SE PUEDE, USANDO COMILLAS SIMPLES PARA DEFINIR LA CADENA Y ASI NO HAY CONFLICTO CON LAS COMILLAS DOBLES DENTRO DE LA CADENA

#el saludo no es correcto porque python interpreta la cadena completa cuando se pone "" y el resto de la cadena se considera fuera de la cadena

# 2. \n SALTO DE LINEA
# FUNCIONA COMO SALTO DE LINEA DENTRO DEL STRING, PUEDES USAR VARIOS
print("Hola, ¿cómo estás?\nEspero que estés teniendo un buen día.")

# 3. \t TABULACION
# FUNCIONA COMO TABULACION DENTRO DEL STRING
print("Nombre:\tJomi\nEdad:\t22\nCiudad:\tCartagena")

# 4. \ BARRA INVERTIDA
mensaje = "La ruta del archivo es C:\\Users\\Jomi\\Documents\\archivo.txt"
#me devolvera esto = C:\Users\Jomi\Documents\archivo.txt
print(mensaje)

# 5. CADENA CRUDA (RAW STRINGS)
mensaje_crudo = r"La ruta del archivo es C:\Users\Jomi\Documents\archivo.txt"
#me devolvera esto = La ruta del archivo es C:\Users\Jomi\Documents\archivo.txt
print(mensaje_crudo)


#ANOTACIONES: ES LO MISMO QUE CON LA BARRA INVERTIDA DOBLE, SOLO QUE CON AGREGARLE r ES MAS EFICIENTE 

a = "Hola"
b = "Mundo"
c = a + " " + b
print(c)

#hola mundo soy jomi 
edad = 22
saludo = f"hola mundo soy jomi y mi edad es: {edad}"

print(saludo)
