acumulado=int(0)
numero=str("")

#While es otro tipo de bucle como el For, con While podemos ejecutar un conjunto de declaraciones
#tan largo hasta como la condición sea Verdadera. Y la única forma para romper este bucle es con
#el comando "break" el cual solo se cumplirá en nuestro código si no se ingresa ningún número.
while True:
    numero=input("Dame un número entero: ")
    if numero=="":
        print("Vacío. Salida del programa.")
        break
    else:
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))