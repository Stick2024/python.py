
number = int(input("Ingrese un número: "))

if number > 0:
    if number % 2 == 0:
        print(f"El número {number} es par positivo.")
    else: 
        print(f"El número {number} es impar positivo.")
elif number < 0:
    if number % 2 == 0:
        print(f"El número {number} es par negativo.")
    else:
        print(f"El núnmero {number} es impar negativo.")
else:
    print("El numero es cero. ")
