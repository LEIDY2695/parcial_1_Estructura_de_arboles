import matplotlib.pyplot as plt
import networkx as nx

# 1. Definición del árbol mediante un diccionario (Lista de adyacencia)
# Basado en la estructura del parcial de Estructuras de Datos
arbol = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [9, 10],
    6: [11],
    7: [12],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
}

# 2. Creación del grafo dirigido con NetworkX
G = nx.DiGraph()
for nodo, hijos in arbol.items():
  for hijo in hijos:
    G.add_edge(nodo, hijo)


# 3. Funciones para los recorridos fundamentales
def preorden(nodo, tree, resultado=None):
  if resultado is None:
    resultado = []
  resultado.append(nodo)
  for hijo in tree.get(nodo, []):
    preorden(hijo, tree, resultado)
  return resultado


def inorden(nodo, tree, resultado=None):
  if resultado is None:
    resultado = []
  hijos = tree.get(nodo, [])
  if len(hijos) > 0:
    inorden(hijos[0], tree, resultado)  # Hijo izquierdo
  resultado.append(nodo)  # Raíz
  for hijo in hijos[1:]:
    inorden(hijo, tree, resultado)  # Hijo derecho (si existe)
  return resultado


def postorden(nodo, tree, resultado=None):
  if resultado is None:
    resultado = []
  for hijo in tree.get(nodo, []):
    postorden(hijo, tree, resultado)
  resultado.append(nodo)
  return resultado


# Imprimir resultados en consola
print("--- RESULTADOS DE RECORRIDOS ---")
print("Preorden:  ", preorden(1, arbol))
print("Inorden:   ", inorden(1, arbol))
print("Postorden: ", postorden(1, arbol))

# 4. Visualización gráfica con NetworkX y Matplotlib
plt.figure(figsize=(9, 6))

# Coordenadas personalizadas para mantener la jerarquía visual idéntica al diagrama del parcial
pos = {
    1: (0, 4),
    2: (-2, 2.5),
    3: (2, 2.5),
    4: (-3, 1),
    5: (-1, 1),
    6: (1, 1),
    7: (3, 1),
    8: (-3, -0.5),
    9: (-1.5, -0.5),
    10: (-0.5, -0.5),
    11: (1, -0.5),
    12: (3, -0.5),
}

# Dibujar el grafo
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="#2b8cbe",
    node_size=800,
    edge_color="#bdbdbd",
    linewidths=1.5,
    font_color="white",
    font_size=12,
    font_weight="bold",
    arrows=True,
    arrowsize=20,
)

plt.title(
    "Visualización del Árbol - Estructura de Datos",
    fontsize=14,
    fontweight="bold",
)
plt.axis("off")
plt.show()