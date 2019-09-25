#A veces es necesario interactuar con usuarios, ya sea para recolectar datos o para proveer cierto tipo de resultados.
#Es por esto que definimos la funcion "Input" como Entrada para mandarla a llamar cuando la escribamos
#La funcion "Input lo que realiza es solicitar al usuario un numero o dato"
entrada=input("Ingresa un valor cualquiera: ")
print(type(entrada))
#Despues mandamos a imprimir a la pantalla el tipo de valor que es nuestro dato que ingresamos con la funcion.

esEntero=(entrada.isdigit() and entrada.find(".")==-1)
#Aqui con el metodo "isdigit()" lo que hacemos es checar si el string ingresado consiste solamente en digitos, verifica que todos los datos ingresados
#sean digitos, si alguno de los valores ingresados tiene al menos un caracter, entonces el valor es falso"
#El metodo ".find()" encuentra la primera aparición del valor especificado, este metodo regresa un "-1" si el valor no es encontrado.


#Aquí realizamos una condicional en el cual el dato ingresado al principio es un digito entero, entonces es verdadero.
if (esEntero):
    print("Dato entero. ¡Muy bien!")
else:
    print("Dato no es entero. Intentar nuevamente.")
#Si el dato ingresado no es entero o es de tipo Character o al menos tiene un cáracter entonces es falso y mandara a pantalla esta opción.