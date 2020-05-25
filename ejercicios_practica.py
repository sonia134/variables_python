#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un calculadora, se ingresará por línea de comando dos números reales
    y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia
    
    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    print('Ingrese 1º numero a calcular:')
    num_1  =  int(input())
    print('Ingrese 2º numero a calcular:')
    num_2  =  int(input())

    suma  = num_1  +  num_2   # Operamos la suma
    # Imprimimos en consola el resultado
    print ( 'El resultado de la suma es' , suma )

    resta  =  num_1  -  num_2  # Operamos la resta
    print ( 'El resultado de la resta es' , resta )

    mult  =  num_1  *  num_2  # Operamos la multiplicacion
    print ( 'El resultado de la multiplicacion es' , mult )

    div  =  num_1  /  num_2  # Operamos la division
    print ( 'El resultado de la division8 es' , div )

    exp= num_1 ^ num_2 # Operamos la potencia
    print ('El resultado de la potencia es:', exp )


def ej2():
    # Ejercicios de práctica numérica y cadenas
    
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea entienda de que se
      está hablando.

    '''
    print('Ingrese Nombre de la Persona:')
    nombre = str(input())

    print('Ingrese Apellido de la Persona:')
    apellido = str(input())

    print('Ingrese D.N.I.:')
    dni = str(input())

    print('Ingrese la Edad:')
    edad = int(input())
    
    print('Ingrese Altura:')
    altura = float(input())

    print('El nombre completo es:', nombre + " " + apellido + " " + 'D.N.I.:', dni)
    print('EL nombre y apellido ingresado corresponde a:', nombre, " ", apellido, 'D.N.I. es:', dni, " ", 'Edad:',edad, " ", 'Altura es:', altura)
  
def ej3():

  
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar el método "split"
    Mostraremos un ejemplo:
    
    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
        
    '''
    #caracter_inicial = pais_objetivo[0] 
    #print(caracter_inicial)
    print('Ingrese Nombre y Apellido completo del Padre:')
    nom_padre= str(input())
    nombre= nom_padre.split(" ")
    ap_padre= nombre[-1]
    print(ap_padre)

    print('Ingrese Nombre y Apellido completo de la Madre:')
    nom_madre= str(input())
    nombre2= nom_madre.split(" ")
    ap_madre= nombre2[-1]
    print(ap_madre)

    print('Ingrese el Nombre del Hijo:')
    nom_hijo= str(input())
    
    print('El nombre completo del Hijo es:', nom_hijo, " ", ap_padre, " ", ap_madre)





def ej4():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine si una persona_2 es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir, primero el nombre y luego
    el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido en el nombre completo
      de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos usar el método "split"
    Mostraremos un ejemplo:
    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    
        
    '''

    print('Ingrese Nombre y Apellido de la Primer Persona:')
    nom_primera= str(input())
    pri_pers= nom_primera.split(" ")
    persona_1= pri_pers[-1]

    print('Ingrese Nombre y Apellido de la Segunda Persona:')
    nom_segunda= str(input())
    seg_pers= nom_segunda.split(" ")
    persona_2= seg_pers[-1]

    es_pariente = persona_2 in persona_1   # es_direccion_argentina es un resultado tipo Bool (True,False)
  
    print(persona_2,'es un pariente?',es_pariente)
   

    
def ej5():
    # Ejercicios de práctica con cadenas
       
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos un el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    

    '''
    print('ingrese su Nombre Completo')

    nombre_min= str(input())

    nombre_may= nombre_min.upper()
    
    prim_mayus= nombre_min.capitalize()
    
    print(nombre_min.lower())
    print(nombre_may.upper())
    print(prim_mayus)


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
