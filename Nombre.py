#Se pide al usuario que ingrese su nombre(s) y apellidos
nombre=input("Ingrese su nombre: ")
apellidos=input("Ingrese sus Apellidos: ")

nombreCompleto=nombre+" "+apellidos
#Nos piden juntar el nombre con el apellido, para esto se necesita combinar ambos datos de tipo String en una sola, a este tipo de proceso
#se le conoce como "Concatenacion" y esto se realiza al crear una nueva variable, en el cual sumamos ambos Strings y que son separados por comillas" " con un espacio entre ellas.

nombreCompleto=nombreCompleto.upper()
print(nombreCompleto)

#Y despues mandamos a llamar la misma funcion pero lo cambiamos a mayúsculas con el método ".upper"