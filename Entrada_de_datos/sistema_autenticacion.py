

print('*** Sistema de autenticacion ***')

USUARIO = 'admin'
PASSWORD = '123'

usuario = input('Ingrese su usuario: ')
password = (input('Ingrese su password: '))

validacion = (USUARIO == usuario.strip() and PASSWORD == password.strip())

print(f'''Datos correctos? {validacion}
''') 