# Luciano Alejandro Gómez Muñoz 22310214

# Algoritmo de Ordenamiento por Inserción (Insertion Sort)
# ----------------------------------------------------------
# El algoritmo de inserción es un método simple de ordenamiento que construye 
# la lista ordenada de forma gradual. Funciona de forma similar a como muchas 
# personas ordenan cartas en sus manos: toma un elemento y lo inserta en la 
# posición correcta respecto a los elementos anteriores ya ordenados.
# 
# Comienza en el segundo elemento del arreglo (índice 1), lo compara con los 
# anteriores y lo "inserta" en la posición adecuada desplazando los mayores 
# hacia la derecha. Este proceso se repite con todos los elementos hasta que 
# la lista esté completamente ordenada.
#
# Su complejidad en el peor caso es O(n²), aunque es eficiente para listas 
# pequeñas o casi ordenadas.

def insertion_sort(lista):
    # Recorremos toda la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        # Guardamos el valor actual que vamos a comparar e insertar
        valor_actual = lista[i]

        # Inicializamos una variable j que usaremos para recorrer los elementos previos
        j = i - 1

        # Mientras j sea válido (>= 0) y el valor en la posición j sea mayor al valor actual,
        # desplazamos ese valor una posición a la derecha
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]  # Movemos el valor una posición a la derecha
            j -= 1  # Retrocedemos una posición para seguir comparando hacia la izquierda

        # Una vez que encontramos la posición correcta, insertamos el valor actual
        lista[j + 1] = valor_actual

        # Esta línea (opcional) imprime la lista tras cada inserción, útil para ver el proceso paso a paso
        # print(f"Iteración {i}: {lista}")

    # Retornamos la lista ordenada (opcional, útil si se desea obtener el resultado como nuevo valor)
    return lista

# Ejemplo de uso:
# Lista desordenada de ejemplo
ejemplo = [10, 4, 2, 9, 5, 10, 7, 20]

# Llamamos a la función de ordenamiento
insertion_sort(ejemplo)

# Imprimimos la lista ya ordenada
print("Lista ordenada:", ejemplo)
