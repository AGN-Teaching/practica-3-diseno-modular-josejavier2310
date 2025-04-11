"""
Incluye funciones para contar el número de sílabas,
de palabras y de oraciones contenidas en un texto
que se recibe como entrada.
"""
# Introduccion
print("Practica 3")
print("Jose Javier Perez Ledesma")

# Programa
import re # Se importa el modulo re para bucar patrones en el texto

def contar_oraciones(texto): # Cuenta cuantas horaciones hay en el texto
    """Cuenta y devuelve el número de oraciones en el texto."""
    # Contamos los signos de puntuación que suelen terminar una oración.
    return len(re.findall(r'[.!?]', texto)) # Returna len con re.fidall para encontar todas las coincidencias de lo que le estamos pidiendo 

def contar_palabras(texto): # Cuenta cuantas palabras hay en el texto
    """Cuenta y devuelve el número de palabras en el texto."""
    # Coincide con secuencias de caracteres alfanuméricos que forman palabras.
    return len(re.findall(r'\b\w+\b', texto, re.UNICODE)) # Returna len con re.finall para encontrar todas las coincidencias -
                                                          # que se piden y utilizamos re.unicode para que el codigo pueda leer algun -
                                                          # caracter que no sea ASCII como por ejemplo \b o \w.

def contar_silabas(texto): # Cuenta cuantas silabas hey en el texto
    """Cuenta y devuelve el número de sílabas en el texto."""
    # Contamos vocales incluyendo tildes y diéresis, sin distinguir mayúsculas/minúsculas.
    return len(re.findall(r'[aeiouáéíóúü]', texto, re.IGNORECASE)) # retornamos len con re.findall para encontrar las coincidencias -
                                                                   # que se piden y utilizamos re.ignorecase para que permita hacer -
                                                                   # coincidencias sin importar si el texto lleva mayusculas o minusculas.
