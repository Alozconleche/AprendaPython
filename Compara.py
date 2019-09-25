#Se le pide al usuario que ingrese dos números en distintas ocasiones
numero1=input("Numero 1: ")
numero2=input("Numero 2: ")
salida="Numeros proporcionados: {} y {}. {}."
#Despues se detalla que el formato de nuestra variable de salida tendra 3 espacios para guardar distintos valores o datos

#Con este if especificamos si el primer numero ingresado es igual al 2, se imprimira en la pantalla que son iguales mediante
#el formato de salida, el cuales los primeros dos datos seran los numeros, y el tercero el texto ya previamente escrito.
if (numero1==numero2):
    print(salida.format(numero1,numero2, "Los números son iguales"))
#Si no se cumple esta razón, se busca otra condición en el cual si el primer número es mayor que el segundo, se
#notificara esto al usuario
else:
    if numero1>numero2:
        print(salida.format(numero1,numero2, "El mayor es el primero"))
    #Si tampoco se cumple esa condición, se corrabora si el primero número es menor que el segundo, y si lo es, se
    #se imprimira su texto correspondiente.
    else:
        if numero1<numero2:
            print(salida.format(numero1,numero2, "El mayor es el segundo"))
