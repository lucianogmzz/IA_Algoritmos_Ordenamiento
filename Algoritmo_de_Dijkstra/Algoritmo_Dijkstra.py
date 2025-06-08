# Importamos funciones de heapq para usar una cola de prioridad (heap)
from heapq import heapify, heappop, heappush

# Importamos networkx para manipulación de grafos
import networkx as nx

# Importamos matplotlib para visualización del grafo
import matplotlib.pyplot as plt

# Definimos el grafo como un diccionario de adyacencia
graph = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
}

class Graph:
    # Constructor: guarda el diccionario del grafo
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def shortest_distances(self, source: str):
        # Crea un diccionario para guardar las distancias mínimas desde el nodo fuente
        # Inicializa todas las distancias en infinito
        distances = {node: float("inf") for node in self.graph}

        # La distancia del nodo fuente a sí mismo es 0
        distances[source] = 0

        # Crea una cola de prioridad (heap) e inserta el nodo fuente
        pq = [(0, source)]
        heapify(pq)  # Convierte la lista en un heap válido

        # Conjunto de nodos ya visitados (para evitar ciclos o repetir trabajo)
        visited = set()

        # Mientras haya nodos en la cola de prioridad
        while pq:
            # Extrae el nodo con menor distancia
            current_distance, current_node = heappop(pq)

            # Si ya fue visitado, lo omitimos
            if current_node in visited:
                continue
            # Marcamos el nodo como visitado
            visited.add(current_node)

            # Exploramos los vecinos del nodo actual
            for neighbor, weight in self.graph[current_node].items():
                # Calculamos distancia tentativa: actual + peso de la arista
                tentative_distance = current_distance + weight

                # Si la nueva distancia es mejor que la actual registrada
                if tentative_distance < distances[neighbor]:
                    # Actualizamos la distancia mínima
                    distances[neighbor] = tentative_distance
                    # Añadimos el vecino a la cola con su nueva distancia
                    heappush(pq, (tentative_distance, neighbor))

        # Retornamos el diccionario con las distancias mínimas desde source
        return distances

    def draw(self):
        # Creamos un grafo de NetworkX
        G_nx = nx.Graph()

        # Agregamos las aristas al grafo con sus respectivos pesos
        for node in self.graph:
            for neighbor, weight in self.graph[node].items():
                G_nx.add_edge(node, neighbor, weight=weight)

        # Calculamos posiciones automáticas para los nodos (distribución visual)
        pos = nx.spring_layout(G_nx, seed=42)  # 'seed' asegura resultados consistentes

        # Dibujamos los nodos y aristas con etiquetas
        nx.draw(
            G_nx,
            pos,
            with_labels=True,         # Mostrar nombres de nodos
            node_color='skyblue',     # Color de los nodos
            node_size=1200,           # Tamaño de los nodos
            font_size=12              # Tamaño de texto
        )

        # Extraemos etiquetas de peso de las aristas
        edge_labels = nx.get_edge_attributes(G_nx, 'weight')

        # Dibujamos etiquetas sobre las aristas con su peso
        nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=edge_labels)

        # Título de la figura
        plt.title("Grafo con pesos")

        # Mostramos el gráfico
        plt.show()

# Creamos una instancia de la clase Graph con el diccionario definido
G = Graph(graph)

# Calculamos las distancias mínimas desde el nodo "B"
distances = G.shortest_distances("B")

# Imprimimos el diccionario con todas las distancias
print(distances, "\n")

# Imprimimos específicamente la distancia más corta de B a F
print(f"The shortest distance from B to F is {distances['F']}")

# Llamamos al método para visualizar el grafo
G.draw()
