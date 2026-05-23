


print("*** Valor dentro del rango ***")

valor_minimo = 0
valor_maximo = 5

valor_solicitado = int(input(f"Ingrese su valor entre {valor_minimo} y {valor_maximo}: "))

valor = valor_solicitado >= valor_minimo and valor_solicitado <= valor_maximo

print(f"Su valor se encuentra dentro del rango: {valor}")
