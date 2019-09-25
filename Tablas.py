for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))

#Este print() sin nada a la derecha lo que hace es hacer un salto de linea entre el texto "Tabla del {X}" y las tablas de
#multiplicación de cada número dentro del rango
    print()

    for j in range(1,11):

        salida="{} X {} = {}"
        print(salida.format(i,j,i*j))
        #Aqui especificamos que i será el primer numero, y j el segundo a multiplicar
    else:
        print()
        #Y con este último print hacemos lo mismo que al inicio que es hacer un salto de linea al terminar de multiplicar
        # "X" tabla por el 10, esto para evitar que la tabla siguiente esté pegada y tenga una mala estética.