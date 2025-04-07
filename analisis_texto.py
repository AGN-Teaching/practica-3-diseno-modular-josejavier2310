"""
Incluye funciones para contar el número de sílabas,
de palabras y de oraciones contenidas en un texto
que se recibe como entrada.
"""

import re

def contar_oraciones(texto):
    """Cuenta y devuelve el número de oraciones en el texto."""
    # Contamos los signos de puntuación que suelen terminar una oración.
    return len(re.findall(r'[.!?]', texto))

def contar_palabras(texto):
    """Cuenta y devuelve el número de palabras en el texto."""
    # Coincide con secuencias de caracteres alfanuméricos que forman palabras.
    return len(re.findall(r'\b\w+\b', texto, re.UNICODE))

def contar_silabas(texto):
    """Cuenta y devuelve el número de sílabas en el texto."""
    # Contamos vocales incluyendo tildes y diéresis, sin distinguir mayúsculas/minúsculas.
    return len(re.findall(r'[aeiouáéíóúü]', texto, re.IGNORECASE))
