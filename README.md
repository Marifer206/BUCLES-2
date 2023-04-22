 # :star: BUCLES-2 :star:
## Un dia nuevo, un nuevo reto

REALIZANDO NUESTRO RETO #8

## 1.EJERCICIO DE CLASE
### :round_pushpin: EJERCICIO #1 
+ Ejercicio: Qué se genera con range(-2)?

#### :space_invader: CODIGO DEL PROGRAMA

```ruby
range(-2) # No genera una secuencia
for num in range(-2): print(num) # No imprime el rango
```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/fTq61dvZ/image.png alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde se obtiene un objeto de rango vacío. Esto se debe a que solo se da el primer argumento de la función range() que especifica el valor de inicio del rango, pero no el el segundo argumento que especifica el valor final del rango, lo que significa que el rango es indefinido y no se puede generar ningún número. <i>x</i> no ingresa al ciclo</b></figcaption></figure>
</div>


## PUNTOS DEL RETO
### :round_pushpin: PUNTO #1 
+ Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
range(0,101)  # Coleccion range con intervalo de 0  101
for i in range(0,101):  # Bucle for con la coleccion range
    print("El cuadrado de " + str(i) + " es " + str(i**2)) # Imprime los numeros del 0 al 100 con sus respectivos cuadrados
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/yN5jYr9L/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> Codigo donde ingresa la colección <i> range </i> en un intervalo de semi-abierto de <i> 0 </i> a <i> 101 </i> y se ejecuta hasta hacer un listado de 0 al 100 con sus respectivos cuadrados</b></figcaption></figure>
</div>


### :round_pushpin: PUNTO #2 
+ Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


#### :space_invader: CODIGO DEL PROGRAMA
```ruby
Pares=[] # Crear una lista vacia para los numeros pares
Impares=[] # Crear una lista vacia para los numeros impares
for i in range(1,1001): # Bucle for con la coleccion range
    if i%2==0: # Si el residuo de la divison es cero es par
        Pares.append(i) # Metodo append para ingresar el numero par
    else:
        Impares.append(i) # Metodo append para ingresar el numero impar
print("Los numeros pares en el rango de 0 a 1000 son " + str(Pares)) # Imprimir lita de pares 
print("\n")
print("Los numeros impares en el rango de 0 a 1000 son " + str(Impares))  # Imprimir lita de impares 
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/jSG9MXdn/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> Codigo donde ingresa la colección <i> range </i> en un intervalo de semi-abierto de <i> 1 </i> a <i> 1001 </i> y se ejecuta el bucle for hasta hacer un clasificar los numeros del intervalo en pares e impares por medio de un condicional if-else para que ingresen a sus respectivas listas para finalmente imprimirlas </b></figcaption></figure>
</div>

    
### :round_pushpin: PUNTO #3  
+ Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado


#### :space_invader: CODIGO DEL PROGRAMA
```ruby
n=int(input("Ingresar numero mayor igual que 2 del cual dese saber los numeros pares antes de el : "))  # Se solicita un número entero cualquiera
def pares_hasta_el_numero(n): # Definir unas función  para ir hasta s 
    p = [] # Creas una lista vacia 
    for i in range(1,n+1): # Establecer el rango y lo unimos a la lista 
        if i%2==0: # Si el residuo es igual a cero es par, se inserta a la lista 
            p.insert(0,i) # Se inserta a la lista vacia el número par i que se encuentra en el rango de 1 a n. La posición en la que se inserta el elemento es el índice 0, es decir, al principio de la lista.
    return p 
print("Los numeros pares de " + str(n) + " hasta 2 son: "+ str(pares_hasta_el_numero(n)))  # Imprime los numeros pares que se encuentran en el rango
```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/hPYztQ3D/image.png alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> n </i> ingresan al ciclo donde es el limite del range para el bicle for y hace un listado de numeros pares por medio de la opracion modulo en forma descendente hasta del n hasta 2 con el metodo insert de las listas </b></figcaption></figure>
</div>



### :round_pushpin: PUNTO #4 
+ Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

#### SOLUCION 1
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
def factorial(num): # definir funcion para función calcular el factorial de un número.
    fact = 1
    for i in range(1, num+1): # Bucle for con la coleccion range
        fact *= i # multiplica fact por cada numero del rango en cada iteracion
    return fact # retorna el nuevo valoe de fact

def numeros_con_factorial(n): # funcion para imprimir los numeros desde 1 has n, junto con su respectivo factorial 
    for i in range(1, n+1): # Bucle for con la coleccion range
        print(i, "! =", factorial(i)) # imprimir el numero con su respectivo factorial

n=int(input("Ingresar el numero hasta el cual quiera saber su respectivo factorial: ")) # solicitar al usuario el numero
numeros_con_factorial(n)
```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> n </i> ingresa a dos ciclos for definidos como funciones, la primera para cualular su respectivo factorial y la segunda para poder imprimir el numero con su respectivo factorial llamando a la primera funcion </b></figcaption></figure>
</div>

#### SOLUCION 2
#### :space_invader: CODIGO DEL PROGRAMA
```ruby
import math
n=int(input("Ingresar el numero hasta el cual quiera saber su respectivo factorial: ")) # Declarar n e inicializarla con el valor dado por el usario 
for i in range(1, n+1): # Bucle for con la coleccion range
    print(i, "! =", math.factorial(i)) # imprimir el numero con su respectivo factorial
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde se importa <i> math </i>  y ingresa <i> n </i> ingresa al ciclo for con la coleccion range de un intervalos de 1 hasta n+1 para luego imprimir directamente el numero y su factorial con la funcion factorial </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #5  
+ Calcular el valor de 2 elevado a la potencia n usando ciclos for.


#### :space_invader: CODIGO DEL PROGRAMA
```ruby
n = int(input("Introduce un número entero al que desea elevar 2: ")) # Pedimos al usuario que introduzca el valor de n
resultado = 1 # Valor inicial del resultado

for i in range(n): # Iniciamos un ciclo for que se ejecuta n veces
    resultado *= 2 # En cada iteración, multiplicamos resultado por 2 y lo asignamos a resultado

print("El resultado de 2 elevado a la " + str(n)+ " es " + str(resultado)) # resultado final: 2 elevado a la potencia n
```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/bYgGXt9V/image.png alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> n </i> ingresa al bucle for y se ejecuta para hallar su factorial por medio de la multiplicacion por 2 n veces el resultado </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #6 
+ Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.


#### :space_invader: CODIGO DEL PROGRAMA
```ruby

```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> RANGO ENTRE 1 Y 100 </i> ingresa al ciclo y se ejecuta para adivinar por medio de la reduccion del rango y por medio de ensayo y error </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #7 
+ Diseñe un programa que muestre las tablas de multiplicar del 1 al 9..

#### :space_invader: CODIGO DEL PROGRAMA
```ruby

```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> x </i> ingresa al ciclo y se ejecuta hasta encontrar todos sus divisores por medio de un modulo </b></figcaption></figure>
</div>


### :round_pushpin: PUNTO #8  
+ Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
import math 

def approx_exp(x, n):
    approx = 0.0  # Inicializa la variable approx a cero
    for i in range(n):  # Bucle for que itera n veces para sumar los primeros n términos de la serie de Maclaurin
        approx += x**i / math.factorial(i) # Calcula el término actual de la serie de Maclaurin y lo suma a approx
    real = math.exp(x)  # Calcula el valor real de la función exponencial en x
    error = abs(real - approx) # Calcula el error absoluto entre la aproximación y el valor real de la función exponencia
    p_error = error / real * 100 

    print(f"Aproximación: {approx:.6f}") # Imprime la aproximación
    print(f"Valor real: {real:.6f}") # Imprime  el valor real 
    print(f"Diferencia: {error:.6f}")  # Imprime la diferencia entre ambos
    print(f"Porciento de error: {p_error:.6f}%")  # Imprime la diferencia entre ambos

# Condicion para determinar si el porcentaje de error es mayor o menor a 0.1%
    if p_error <= 0.1:
        print (f"el porcentaje de error es menor a 0.1%: {p_error:.6f}") 
    else:
        print (f"el porcentaje de error es mayor a 0.1%: {p_error:.6f}") 

x = float(input("Ingrese el valor de x: ")) # Solicitar al usuario que ingrese el valor de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin a utilizar: "))  # Solicitar al usuario el número de términos de la serie de Maclaurin a utilizar

approx_exp(x, n) # llamar a la funcion para que el usuario pueda ingresar los datos 
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> x y n </i> ingresa a un bucle for para calcular la aproximacion y se define una funcion para poder imprimir la aproximacion, valor real, error, y el porcentaje de error y por ultimo de solicita que ingresen los datos y se llama a la funcion <i> approx_exp </i>  previamente definida que toma como argumento a x y n </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #9  
+ Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
import math

def sin_approx(x, n):# Definimos la función sin_approx que toma dos argumentos: x y n
    approx = 0# Inicializamos la variable approx en 0
    for i in range(n):# Iteramos n veces, sumando cada término de la serie de Maclaurin para el seno
        term = ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)# Calculamos cada término de la serie de Maclaurin utilizando la fórmula correspondiente
        approx += term # Sumamos el término actual a la aproximación acumulada
    error = abs(math.sin(x) - approx)# Calculamos el error absoluto entre la aproximación y el valor real de la función seno
    real = math.sin(x)
    p_error = error / real * 100
    
    print(f"Aproximación: {approx:.6f}")# Imprir la aproximación
    print(f"Valor real: {math.sin(x):.6f}")# Imprimimos  el valor real 
    print(f"Error: {error:.6f}")# Imprimimos el error 
    print(f"Porciento de error: {p_error:.6f}%")  # Imprime la diferencia entre ambos

    # Condiciones para que el porcentaje de error sea mayor o menor a 0.1 %
    if p_error <= 0.1:
        print (f"el porcentaje de error es menor a 0.1%: {p_error:.6f}") 
    else:
        print (f"el porcentaje de error es mayor a 0.1%: {p_error:.6f}") 


x = float(input("Ingrese el valor de x para aproximar la función seno: ")) #Solicitar valor de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin que desea utilizar: ")) #solicitar valor de n 

sin_approx(x, n) # Llamar a la función sin_approx con los valores dados
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="https://i.postimg.cc/BvHMg01F/image.png alt="" width="700" height="auto"/></br>
<figcaption><b> Codigo donde <i> x y n </i> ingresa a un bucle for para calcular la aproximacion y se define una funcion para poder imprimir la aproximacion, valor real, error, y el porcentaje de error y por ultimo de solicita que ingresen los datos y se llama a la funcion <i> sin_approx </i>  previamente definida que toma como argumento a x y n </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #10 
+ Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
import math

def arctan_approx(x, n): # Definr la función arctan_approx que toma dos argumentos: x y n
    if x < -1 or x > 1: # Asegurse que el valor de x está en el rango [-1, 1]
        print("Error: el valor de x debe estar en el rango [-1, 1].")
        return

    approx = 0  # Inicializa la variable approx en 0
    for i in range(n): # Itera n veces, sumando cada término de la serie de Maclaurin para la arcotangente
        term = ((-1)**i * x**(2*i + 1)) / (2*i + 1) # Calcula cada término de la serie de Maclaurin utilizando la fórmula correspondiente
        approx += term # Suma el término actual a la aproximación acumulada

    error = abs(math.atan(x) - approx)# Calcula el error absoluto entre la aproximación y el valor real de la función arcotangente
    real = math.atan(x) # Calcula el valor real
    p_error = error / real * 100 # Calcula el porcentaje de error

    print(f"Aproximación: {approx:.6f}")  # Imprimime la aproximación
    print(f"Valor real: {math.atan(x):.6f}")  # Imprimime el valor real
    print(f"Error: {error:.6f}")  # Imprimime el error
    print(f"Porciento de error: {p_error:.6f}%")  # Imprime la diferencia entre ambos


    # Condicion para que el porcentaje de error sea mayor o menor a 0.1 %
    if p_error <= 0.1:
        print (f"El porcentaje de error es menor a 0.1%: {p_error:.6f}") 
    else:
        print (f"El porcentaje de error es mayor a 0.1%: {p_error:.6f}") 


x = float(input("Ingrese el valor de x para aproximar la función arcotangente: ")) #Solicitar el valor x
n = int(input("Ingrese el número de términos de la serie de Maclaurin que desea utilizar: ")) #solicitar el valor de n 


arctan_approx(x, n) # Llamar a la función arctan_approx para utilizarla con los valores dados por el usuario
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> x y n </i> ingresa a un bucle for para calcular la aproximacion pero antes se asegura con un condicional de que x este dentro del rango y se una funcion para poder imprimir la aproximacion, valor real, error, y el porcentaje de error y por ultimo de solicita que ingresen los datos y se llama a la funcion <i> arctan_approx </i>  previamente definida que toma como argumento a x y n </b></figcaption></figure>
</div>

## :sparkles: Esto es todo hoy amigos :blush:, espero poder haberlos ayudado he inspirado para encontar nuevas solociones para nuevos retos :sparkles: 
