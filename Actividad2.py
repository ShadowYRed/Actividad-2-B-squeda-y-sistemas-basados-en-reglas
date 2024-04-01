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
