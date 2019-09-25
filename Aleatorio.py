#Se manda a traer una libreria llamada "random" el cual proporciona un generador de diferentes números aleatorios
#Asi mismo para utilizar alguna función de un modulo, se tiene que importar con anterioridad
#Es por esto mismo que importamos la libreria en nuestra cabecera de nuestro código como regla
import random

numero1=float(10.5)
#Se define una variable de tipo Float con un valor de 10.5 el cual regresa un numero tipo float o con decimales de un numero entero o un string
#Cabe destacar que esta variable con nombre "numero1" siempre va a tener un valor de 10.5


#Se define una funcion con su prefijo "def" el cual será llamada cada vez que sea llamada el nombre de la función.
def miFuncion():
    numero2=float(random.randrange(1,10))
    #Definimos que el numero generado aleatoriamente pase a hacer de tipo float
    #Y que se encuentre dentro de un rango del 1 al 9
    #El método "randrange" devuelve un elemento seleccionado al azar, el número aleatorio que nos
    #va a devolver tiene que estar dentro de un rago ingresado por nosotros como señalamos con un valor de "1,10"
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))
    #La funcion "str.format()" encontrada como "mensaje.format" en nuestro código, lo que realiza es permitir múltiples
    #sustituciones y formateo de valores. Basicamente este metodo nos permite cocatenar elementos
    #de un string de forma posicional.

miFuncion()