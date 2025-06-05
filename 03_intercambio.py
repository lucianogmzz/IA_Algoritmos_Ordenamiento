# Luciano Alejandro Gómez Muñoz 22310214

# Algoritmo de Ordenamiento por Intercambio (Bubble Sort)
# ----------------------------------------------------------
# El algoritmo de intercambio o "bubble sort" es uno de los métodos de ordenamiento más 
# simples de entender. Consiste en recorrer repetidamente la lista, comparando elementos 
# adyacentes e intercambiándolos si están en el orden incorrecto (el mayor antes que el menor).
#
# Este proceso se repite hasta que en una pasada completa no se realicen intercambios, 
# lo que indica que la lista ya está ordenada.
#
# Su nombre proviene del efecto que produce al mover los valores grandes hacia el final 
# de la lista, como si "flotaran" como burbujas.
#
# Su complejidad en el peor y promedio de los casos es O(n²), aunque puede optimizarse 
# ligeramente si se detecta que no hubo intercambios.

def bubble_sort(lista):
    # Obtenemos la longitud de la lista
    n = len(lista)

    # Recorremos toda la lista n veces como máximo
    for i in range(n):
        # Variable que usamos para verificar si hubo algún intercambio en esta pasada
        intercambio = False

        # Recorremos desde el primer elemento hasta el elemento antes del final no ordenado
        for j in range(0, n - 1 - i):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[j] > lista[j + 1]:
                # Intercambio de los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                # Indicamos que sí hubo un intercambio
                intercambio = True

        # Si no hubo intercambios en esta pasada, la lista ya está ordenada y se puede salir
        if not intercambio:
            break  # Terminamos el bucle anticipadamente

        # Esta línea (opcional) muestra el estado de la lista en cada iteración
        # print(f"Iteración {i}: {lista}")

    # Retornamos la lista ordenada (opcional)
    return lista

# Ejemplo de uso:
# Lista desordenada de ejemplo
ejemplo = [10, 6, 2, 8, 4]

# Llamamos a la función de ordenamiento
bubble_sort(ejemplo)

print("Lista original:", ejemplo)

# Imprimimos la lista ya ordenada
print("Lista ordenada:", ejemplo)
