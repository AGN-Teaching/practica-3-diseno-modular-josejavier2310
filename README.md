[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zLSmh4bI)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19021392)
# Práctica 3. Diseño modular
Para realizar la practica realizaremos 3 codigos, el primero sera de analisis de texto donde tendra que contar oraciones, palabras y silabas.
Primero agrege un import re para buscar patrones en el texto, en contar_oraciones encontramos todas las oraciones que hay en el texto buscando todos los signos de puntuacion que normalmente terminan en signos de puntuacion o de exclamacion, en contar_palabras encuentra el numero de palabras utilizando \b que indica el limite de palabras y \w+ que busca una o mas letras, numeros o guiones bajos, tambien utilizamos re.Unicode para que el programa puda leer ese tipo de valores ( \b ), en contar_silabas cuenta cuantas silabas tiene el texto tomando en cuenta las vocales, acentuadas y dieresis, utilizamos re.IGNORECASE para que el codigo pueda leer las coincidencias sin importar si son mayusculas o minusculas.
En el segundo codigo llamado Legibilidad calculamos el indice y el nivel de legibilidad que tiene el texto, iniciamos importando analisis_texto que tambien llamaremos at y aqui asumimos que tenemos otros archivos que son los anteriores mencionados contar_oraciones, palabras y silabas, definimos indice_legibilidad que contendra oraciones, palabras y silabas junto con un at al principio, despues con las funciones contar_oraciones, palabras y silabas y esto lo que hara es llamarlas, despues colocamos un if para verificar si el numero de palabras o oraciones es igual a cero y si alguno es 0, detiene el calculo y devuelve los valores contados, lo retornamos y despues ocupamos la formula para calcular la leguibilidad del texto, lo retornamos y definimos nivel_legibilidad para calcular que nivel de legibilidad tiene el texto, si es mayor igual que 80 es muy facil, si es mayor igual que 60 es facil, si es mayor igual que 40 es intermedio, si es mayor igual que 20 es dificil y si no es nunguna de las anteriores es muy dificil.
En el tercer codigo llamado practica4 implementaremos lo que hicimos en ambos codigos a este para que leea el codigo y muestre los resultados
