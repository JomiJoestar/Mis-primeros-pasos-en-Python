
print('*** Sistema de empleados ***')
nombre_empleado = input("Ingrese del empleado: ")
edad = int(input("Edad del empleado: "))
salario = float(input("Salario del empleado: "))
es_jefe_departamento = input("Es jede de departamento? (Si/No)")

# vamos a convertir a un tipo bool la variable es_jefe_departamento?
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

print('\n Datos Del Empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad}')
print(f'Su salario es de: {salario}')
print(f'Es jefe de Departamento? {es}')
