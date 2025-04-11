"""
Funciones para calcular el índice de Velázquez Gaytán (utilizando el módulo analisis_texto) y para decidir el nivel de legibilidad de un texto.
"""
# Introduccion
print("Practica 3")
print("Jose Javier Perez Ledesma")

# Programa
import analisis_texto as at # Aqui asumimos que tenemos otros archivos como contar_oraciones, palabras y silibas

def indice_legibilidad_VG(texto): # Aqui se obtienen los datos para calcular el indice de legibilidad
    oraciones = at.contar_oraciones(texto) # Llamamos a la funcion contar_oraciones del analisis_texto y por eso tiene at al principio 
    palabras = at.contar_palabras(texto) # Llamamos a la funcion contar_palabras del modulo at
    silabas = at.contar_silabas(texto) # Llamamos a la funcion contar_silabas del modulo at

    if palabras == 0 or oraciones == 0: # Verifica si el numero de palabras o de oraciones es igual a cero
        return oraciones, palabras, silabas, 0 # Si alguno de los dos es cero, detiene el calculo y devuelve directamente los valores contados mas un indice de legibilidad igual a cero 
# Retornamos oraciones, palabras, silabas y el indice de legibilidad 0
    L = 206.84 - 1.02 * (palabras / oraciones) - 60 * (silabas / palabras)  # Aplicamos la formula para calcular la legibilidad del texto
    return oraciones, palabras, silabas, L # Retornamos los valores asignados que son oraciones, palabras, silabas y L osea legibilidad

def nivel_legibilidad_VG(indice): # Calculamos el nivel de legibilidad que esta en la tabla asignada de la practica
    if indice >= 80: # Si el indice es mayor igual a 80 estonces es Muy Facil
        return "Muy fácil" 
    elif indice >= 60: # Si el indice es mayor igual a 60 esntonces es Facil
        return "Fácil" 
    elif indice >= 40: 
        return "Intermedio" # Si el indice es mayor igual a 40 entonces es Intermedio
    elif indice >= 20: 
        return "Difícil" # Si el indice es mayor igual a 20 entonces es Dificil
    else: 
        return "Muy difícil" # Si el indice no es ninguno de los anteriores entonces es Muy Dificil

