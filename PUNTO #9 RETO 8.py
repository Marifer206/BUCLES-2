import math 

def sin_approx(x, n):# Definir la función sin_approx que toma dos argumentos: x y n
    approx = 0# Iniciali la variable approx en 0
    for i in range(n):# Itera n veces, sumando cada término de la serie de Maclaurin para el seno
        term = ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)# Calcula cada término de la serie de Maclaurin utilizando la fórmula correspondiente
        approx += term # Suma el término actual a la aproximación acumulada
    error = abs(math.sin(x) - approx)# Calcula el error absoluto entre la aproximación y el valor real de la función seno
    real = math.sin(x)
    p_error = error / real * 100
    
    print(f"Aproximación: {approx:.6f}")# Imprime la aproximación
    print(f"Valor real: {math.sin(x):.6f}")# Imprimime el valor real 
    print(f"Error: {error:.6f}")# Imprime el error 
    print(f"Porciento de error: {p_error:.6f}%")  # Imprime la diferencia entre ambos

    # Condicion para que el porcentaje de error sea mayor o menor a 0.1 %
    if p_error <= 0.1:
        print (f"El porcentaje de error es menor a 0.1%: {p_error:.6f}") 
    else:
        print (f"El porcentaje de error es mayor a 0.1%: {p_error:.6f}") 


x = float(input("Ingrese el valor de x para aproximar la función seno: ")) #Solicitar valor de x
n = int(input("Ingrese el número de términos de la serie de Maclaurin que desea utilizar: ")) #solicitar valor de n 

sin_approx(x, n) # Llamar a la función sin_approx con los valores dados  