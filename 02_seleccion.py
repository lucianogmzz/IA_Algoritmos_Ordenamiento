# Luciano Alejandro Gómez Muñoz 22310214

# Algoritmo de Ordenamiento por Selección (Selection Sort)
# ----------------------------------------------------------
# Este algoritmo divide la lista en dos partes: una sublista ordenada (inicialmente vacía)
# y otra sublista no ordenada. En cada iteración, selecciona el elemento más pequeño de 
# la parte no ordenada y lo intercambia con el primer elemento de esa sección, 
# expandiendo así la sublista ordenada una posición hacia la derecha.
#
# Este proceso se repite hasta que toda la lista esté ordenada.
# La complejidad del algoritmo es O(n²), sin importar el caso, ya que siempre recorre 
# toda la lista restante en cada iteración.

def selection_sort(lista):
    # Obtenemos la longitud de la lista
    n = len(lista)

    # Recorremos toda la lista desde el primer elemento hasta el penúltimo
    for i in range(n - 1):
        # Suponemos que el menor elemento se encuentra en la posición i
        indice_menor = i

        # Buscamos en el resto de la lista un elemento menor al actual
        for j in range(i + 1, n):
            # Si encontramos un elemento menor, actualizamos el índice del menor
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        # Si encontramos un elemento menor al inicial, hacemos un intercambio
        if indice_menor != i:
            # Intercambiamos los valores: el menor va a la posición actual
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

        # Esta línea (opcional) muestra cómo va cambiando la lista tras cada iteración
        # print(f"Iteración {i}: {lista}")

    # Retornamos la lista ordenada (opcional si se desea usar el valor directamente)
    return lista

# Ejemplo de uso:
# Lista desordenada de ejemplo
ejemplo = [7, 3, 1, 9, 5]

# Llamamos a la función de ordenamiento
selection_sort(ejemplo)

# Imprimimos la lista ordenada
print("Lista ordenada:", ejemplo)
