def calcular_precio(dia, tiempo):
    if dia == "Lunes" or dia == "Martes" or dia == "Miércoles":
        tarifa = 2.00
    elif dia == "Jueves" or dia == "Viernes":
        tarifa = 2.50
    elif dia == "Sábado" or dia == "Domingo":
        tarifa = 3.00
    else:
        print("Día de la semana incorrecto")
        return

    horas = int(tiempo.split(':')[0])
    minutos = int(tiempo.split(':')[1])

    if minutos > 5:
        horas += 1

    total = tarifa * horas
    print(f"El monto a pagar es: ${total:.2f}")

def main():
    dia = input("Ingrese el día de la semana (Lunes/Martes/Miércoles/Jueves/Viernes/Sábado/Domingo): ")
    tiempo = input("Ingrese el tiempo de estacionamiento (HH:MM): ")

    if len(tiempo.split(':')) != 2:
        print("Formato de tiempo incorrecto")
        return

    calcular_precio(dia, tiempo)

if __name__ == "__main__":
    main()