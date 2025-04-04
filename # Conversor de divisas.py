
# Conversor de divisas 

def mostrar_menu():
    print("\nConversor de Divisas")
    print("1. Convertir a dólares (USD)")
    print("2. Convertir a euros (EUR)")
    print("3. Convertir a yenes (JPY)")
    print("4. Convertir a libras esterlinas (GBP)")
    print("5. Convertir a francos suizos (CHF)")
    print("6. Convertir a rublos rusos (RUB)")
    print("7. Salir")

def convertir_moneda(pesos, tasa_cambio):
    return pesos * tasa_cambio  # Cambié la operación de división a multiplicación

def main():
    # Tasas de cambio (en valores directos para multiplicar)
    tasas = {
        "USD": 1 / 4500,  # 1 USD = 4500 pesos
        "EUR": 1 / 4800,  # 1 EUR = 4800 pesos
        "JPY": 1 / 30,    # 1 JPY = 30 pesos
        "GBP": 1 / 5500,  # 1 GBP = 5500 pesos
        "CHF": 1 / 4600,  # 1 CHF = 4600 pesos
        "RUB": 1 / 60     # 1 RUB = 60 pesos
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "7":
            print("Saliendo del programa. ¡Adiós!")
            break

        if opcion not in map(str, range(1, 7)):
            print("Opción no válida. Intente de nuevo.")
            continue

        pesos = float(input("Ingrese la cantidad de pesos a convertir: "))

        if opcion == "1":
            print(f"{pesos} pesos equivalen a {convertir_moneda(pesos, tasas['USD']):.2f} dólares (USD).")
        elif opcion == "2":
            print(f"{pesos} pesos equivalen a {convertir_moneda(pesos, tasas['EUR']):.2f} euros (EUR).")
        elif opcion == "3":
            print(f"{pesos} pesos equivalen a {convertir_moneda(pesos, tasas['JPY']):.2f} yenes (JPY).")
        elif opcion == "4":
            print(f"{pesos} pesos equivalen a {convertir_moneda(pesos, tasas['GBP']):.2f} libras esterlinas (GBP).")
        elif opcion == "5":
            print(f"{pesos} pesos equivalen a {convertir_moneda(pesos, tasas['CHF']):.2f} francos suizos (CHF).")
        elif opcion == "6":
            print(f"{pesos} pesos equivalen a {convertir_moneda(pesos, tasas['RUB']):.2f} rublos rusos (RUB).")

if __name__ == "__main__":
    main()
