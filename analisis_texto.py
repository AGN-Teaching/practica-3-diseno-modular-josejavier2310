"""
Incluye funciones para contar el número de sílabas,
de palabras y de oraciones contenidas en un texto
que se recibe como entrada.
"""

def contar_oraciones(texto):
    """Cuenta y devuelve el número de oraciones en texto."""
    return len(re.findall(r'[.!?;:]', texto))    

def contar_palabras(texto):
    """Cuenta y devuelve el número de palabras en texto."""
    return len(re.findall(r'\b\w+\b', texto))

def contar_silabas(texto):
    """Cuenta y devuelve el número de sílabas en texto."""
    return len(re.findall(r'[aeiouáéíóúü]', texto, re.IGNORECASE))
