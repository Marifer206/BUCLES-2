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

```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> n </i> ingresan al ciclo y se ejecuta y hace un listado de numeros pares en forma descendente hasta el 2 999</b></figcaption></figure>
</div>



### :round_pushpin: PUNTO #4 
+ Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial


#### :space_invader: CODIGO DEL PROGRAMA
```ruby

```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> a y b </i> ingresan al ciclo y se ejecuta hasta que la poblacion del pais B (valor de b) supere a la poblacion del pais A (valor de a)</b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #5  
+ Calcular el valor de 2 elevado a la potencia n usando ciclos for.


#### :space_invader: CODIGO DEL PROGRAMA
```ruby

```

:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> n </i> ingresa al ciclo y se ejecuta para hallar su factorial</b></figcaption></figure>
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> numero </i> ingresa a un ciclo donde se llama a la funcion funcion <i> es_primo </i>  previamente definida que toma como argumento a numero</b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #9  
+ Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

#### :space_invader: CODIGO DEL PROGRAMA
```ruby

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> numero </i> ingresa a un ciclo donde se llama a la funcion funcion <i> es_primo </i>  previamente definida que toma como argumento a numero</b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #10 
+ Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

#### :space_invader: CODIGO DEL PROGRAMA
```ruby

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src="h" alt="" width="700" height="auto"/></br>
<figcaption><b>Codigo donde <i> numero </i> ingresa a un ciclo donde se llama a la funcion funcion <i> es_primo </i>  previamente definida que toma como argumento a numero</b></figcaption></figure>
</div>

## :sparkles: Esto es todo hoy amigos :blush:, espero poder haberlos ayudado he inspirado para encontar nuevas solociones para nuevos retos :sparkles: 
