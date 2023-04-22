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