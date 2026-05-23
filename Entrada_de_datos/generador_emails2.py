

#SISTEMA DE GENERADOR DE EMAILS 2

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
empresa = input("Ingrese el nombre de la empresa: ")
extension_dominio = input("Ingrese el dominio EJ(.com.co): ")

nombre_final = nombre.strip().replace(" ",".").lower()
apellido_final = apellido.strip().replace(" ", ".").lower()
empresa_final = empresa.strip().lower()
extension_dominio_final = extension_dominio.strip()

print(f'''Hola, {nombre}... Su email generado es:  
            {nombre_final}.{apellido_final}@{empresa_final}{extension_dominio_final}
            Felicidades!!!''')


