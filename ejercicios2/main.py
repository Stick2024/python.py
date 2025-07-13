# Este programa calculara el valor de venta
valor_venta = input("Ingrese el valor de la venta")
valor_venta = float(valor_venta)

#Calcular el IGV (Este calcula el valor de venta del 18%)
igv = valor_venta * 0.18

#Este realiza el valor de vanta final
precio_venta = valor_venta + igv

#mostrar resultados 
print(f"El igv es: {igv:.2f}")
print(f"El precio de venta es: {precio_venta:.2f}")
