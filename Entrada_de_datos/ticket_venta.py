





print('*** Generador de Tickets de venta ***')

precio_leche =  float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio de los platanos: '))
descuento_porcentaje =  int(input('Desea aplicar algun descuento (%)?: '))

# Calculo del subtotal (Sin impuestos)

subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar descuento
descuento = subtotal * (descuento_porcentaje/100)

# Calculo con impuestos (16%)
impuesto = subtotal * 0.16

# Subtotal con descuento 
subtotal_con_descuento =  subtotal - descuento

# Calculo total de la comprar (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto



print(f'''      
subtotal: ${subtotal:.2f}
descuento aplicado: ${descuento} ({descuento_porcentaje}%)
subtotal con descuento: %{subtotal_con_descuento}
impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}''')