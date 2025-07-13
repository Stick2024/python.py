#Solicitar que el usuario ingrese un monto de descuento
total_amount = float(input("ingrese el monto del consumo $"))

#Se calcula el descuento
if total_amount > 50 and total_amount <= 100:
    discount_percentage = 0.1
elif total_amount > 100 and total_amount <= 200:
    discount_percentage = 0.2
elif total_amount > 200:
    discount_percentage = 0.3
else:
    discount_percentage = 0.0

    #se calcula el monto del descuento 
discount_percentage = total_amount * discount_percentage
final_amount = total_amount - discount_percentage

#Mostrar el resumen
print("\n resumen de la cuenta: ")
print(f"monto del consumo: ${total_amount:.2f}")
print(f"Monto final con descuento: $ {final_amount:.2f}")