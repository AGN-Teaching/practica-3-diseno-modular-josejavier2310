"""
Funciones para calcular el índice de Velázquez Gaytán (utilizando el módulo analisis_texto) y para decidir el nivel de legibilidad de un texto.
"""

import analisis_texto as at


def indice_legibilidad_VG(texto):
    """Calcula y devuelve el índice de Velázquez Gaytán del texto de entrada."""
    oraciones = contar_oraciones(texto) palabras = contar_palabras(texto) silabas = contar_silabas(texto)

if palabras == 0:
    return oraciones, palabras, silabas, 0

indice = (206.84 - 0.85 * (silabas / palabras) - 1.3 * (palabras / oraciones)) if oraciones > 0 else 0
    return oraciones, palabras, silabas, indice

def nivel_legibilidad_VG(indice):
    """Decide y devuelve el nivel de legibilidad de un texto de acuerdo con el índice de Velázquez Gaytán."""
if indice >= 80: 
    return "Muy fácil" 
elif indice >= 60: 
    return "Fácil" 
elif indice >= 40: 
    return "Intermedio" 
elif indice >= 20: 
    return "Difícil" 
else: 
    return "Muy difícil"
