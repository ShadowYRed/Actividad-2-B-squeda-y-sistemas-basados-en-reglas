#Primero debemos instalar networkx para poder realizar el ejercicio
#Para estu usamos el pip install networkx, en nuestra consola
#import networkx as nx: Importa la biblioteca NetworkX, que es una biblioteca de Python utilizada para la creación, manipulación y estudio de estructuras, dinámicas y funciones de redes complejas.
#red_transporte = nx.Graph(): Crea un grafo vacío que representará nuestra red de transporte. nx.Graph() crea un grafo no dirigido sin nodos ni aristas.
#Las líneas del 4 al 21 agregan nodos y conexiones ponderadas (aristas) al grafo red_transporte. Cada llamada a add_edge() agrega una conexión entre dos países (nodos) con un peso específico que representa la distancia entre ellos.
#def encontrar_mejor_ruta(origen, destino):: Define una función llamada encontrar_mejor_ruta que toma dos argumentos: origen y destino.
#try:: Inicia un bloque try-except que manejará cualquier excepción lanzada dentro de él.
#mejor_ruta = nx.shortest_path(red_transporte, origen, destino, weight='weight'): Utiliza la función shortest_path() de NetworkX para encontrar la ruta más corta entre el origen y el destino en el grafo red_transporte. El parámetro weight='weight' indica que la función debe tener en cuenta el peso de las aristas al calcular la ruta más corta.
#distancia = nx.shortest_path_length(red_transporte, origen, destino, weight='weight') * 10: Utiliza la función shortest_path_length() de NetworkX para calcular la distancia total de la ruta más corta encontrada en el paso anterior. Multiplica esta distancia por 10 para convertir cada "unidad" a 10 km, como se especifica en el enunciado.
#except nx.NetworkXNoPath:: Captura la excepción NetworkXNoPath que se produce cuando no hay ninguna ruta entre el origen y el destino en el grafo.
#return mejor_ruta, distancia: Devuelve la mejor ruta encontrada y la distancia total de esa ruta.
#Las líneas del 24 al 33 son el bloque de código principal que se ejecuta cuando el script se ejecuta como un programa independiente (es decir, no se importa como un módulo).
#origen = input("Ingrese el país de origen: "): Solicita al usuario que ingrese el país de origen.
#destino = input("Ingrese el país de destino: "): Solicita al usuario que ingrese el país de destino.
#ruta_optima, distancia = encontrar_mejor_ruta(origen, destino): Llama a la función encontrar_mejor_ruta() con el origen y destino proporcionados por el usuario, y guarda la mejor ruta y la distancia total calculada.
#if ruta_optima:: Comprueba si se encontró una ruta óptima (si no se produce una excepción).
#print("La mejor ruta desde {} hasta {} es: {}".format(origen, destino, ruta_optima)): Muestra la mejor ruta encontrada.
#print("Distancia total: {} km".format(distancia)): Muestra la distancia total de la ruta óptima.
#else:: Maneja el caso en que no se pueda encontrar una ruta entre el origen y el destino.
#print("No hay ruta disponible desde {} hasta {}".format(origen, destino)): Informa al usuario que no hay ruta disponible entre el origen y el destino proporcionados.

import networkx as nx

# Definir la red de transporte como un grafo
red_transporte = nx.Graph()

# Agregar países y conexiones entre ellos
red_transporte.add_edge("USA", "Canada", weight=5)
red_transporte.add_edge("USA", "Mexico", weight=3)
red_transporte.add_edge("USA", "Brazil", weight=7)
red_transporte.add_edge("Canada", "UK", weight=4)
red_transporte.add_edge("Canada", "Germany", weight=2)
red_transporte.add_edge("Mexico", "Spain", weight=6)
red_transporte.add_edge("Brazil", "Argentina", weight=3)
red_transporte.add_edge("UK", "France", weight=5)
red_transporte.add_edge("Germany", "Italy", weight=4)
red_transporte.add_edge("Spain", "Portugal", weight=3)
red_transporte.add_edge("Argentina", "Chile", weight=2)
red_transporte.add_edge("France", "Switzerland", weight=1)
red_transporte.add_edge("Italy", "Greece", weight=5)
red_transporte.add_edge("Portugal", "Netherlands", weight=4)
red_transporte.add_edge("Chile", "Peru", weight=3)
red_transporte.add_edge("Switzerland", "Austria", weight=2)
red_transporte.add_edge("Greece", "Turkey", weight=4)
red_transporte.add_edge("Netherlands", "Belgium", weight=2)

# Función para encontrar la mejor ruta utilizando el algoritmo de Dijkstra
def encontrar_mejor_ruta(origen, destino):
    try:
        mejor_ruta = nx.shortest_path(red_transporte, origen, destino, weight='weight')
        distancia = nx.shortest_path_length(red_transporte, origen, destino, weight='weight') * 10  # Convertir cada "unidad" a 10 km
        return mejor_ruta, distancia
    except nx.NetworkXNoPath:
        return None, float('inf')

# Ejemplo de uso
if __name__ == "__main__":
    origen = input("Ingrese el país de origen: ")
    destino = input("Ingrese el país de destino: ")

    ruta_optima, distancia = encontrar_mejor_ruta(origen, destino)

    if ruta_optima:
        print("La mejor ruta desde {} hasta {} es: {}".format(origen, destino, ruta_optima))
        print("Distancia total: {} km".format(distancia))
    else:
        print("No hay ruta disponible desde {} hasta {}".format(origen, destino))
