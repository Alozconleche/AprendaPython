#Se pide al usuario que ingrese un número del 1 al 9, pero realmente pueden ser otros distintos como el 10, 13 etc.
#Estos numeros solo pueden ser de tipo Entero, no de tipo flotante.
numero=input("Dame un número del 1 al 9: ")
numero=int(numero)

for i in range(1,11):
#El for se utiliza para bucles e iterarlas sobre una secuencia, ya sea una lista o una tupla.Y como deseamos realizar una secuencia
#de tablas de multiplicación, la utilizamos para que se repita un "n" cantidad de veces el cual especificamos con el rango.
#La funcion "range() genera el resultado entre el número dado al inicio de la operacion o rango, con el final"
#El "in" sera verdadera si el valor del rango especificado es encontrada en la secuencia
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))
