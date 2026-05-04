nombre = input("Nombre del trabajador: ")
horas = int(input("Horas trabajadas: "))
pago_hora = float(input("Pago por hora: "))

if horas <= 40:
    horas_normales = horas
    horas_extra = 0
    salario_total = horas_normales * pago_hora
else:
    horas_normales = 40
    horas_extra = horas - 40
    salario_normal = horas_normales * pago_hora
    salario_extra = horas_extra * pago_hora * 1.5
    salario_total = salario_normal + salario_extra

if salario_total >= 2000000:
    clasificacion = "Salario alto"
elif salario_total >= 1000000:
    clasificacion = "Salario medio"
else:
    clasificacion = "Salario bajo"

print()
print(f"Trabajador: {nombre}")
print(f"Horas normales: {horas_normales}")
print(f"Horas extra: {horas_extra}")
print(f"Salario total: {salario_total:.0f}")
print(f"Clasificación: {clasificacion}")
