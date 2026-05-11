


#Programa multiplicacion de cadenas

# 1. CREAR UN SEPARADOR VISUAL

linea = "=" * 20
print(linea) #Salida: ====================

# 2. IDENTACION SIMPLE

nivel = 10
sangria = "        " * nivel
print(sangria + "Este texto esta indentado") 
#Salida:         Este texto esta indentado

# 3. PATRONES SIMPLES
print("1" * 5)  #Salida: 11111 (texto, no numero)

# 4. ERROR COMUN (COMENTADO PARA EVITAR CRASH)
#print("Hola" * 1.5) #Error: TypeError: can't multiply sequence by non-int of type 'str' 
#SOLO SE PUEDE MULTIPLICAR POR UN NUMERO ENTERO)
