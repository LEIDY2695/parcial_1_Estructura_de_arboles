import matplotlib.pyplot as plt
import networkx as nx

# 1. Definición de vértices y aristas
V = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
A = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (3, 7),
    (4, 8),
    (5, 9),
    (5, 10),
    (6, 11),
    (7, 12),
]

print("Vertices:", V)
print("Aristas:", A)

Nodo_raiz = 1
Nodo_hoja = {8, 9, 10, 11, 12}
nodos_internos = {2, 3, 4, 5, 6, 7}

print("Nodo raiz:", Nodo_raiz)
print("Nodos hoja:", Nodo_hoja)
print("Nodos internos:", nodos_internos)

# 2. Diccionario del árbol
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

print("\nÁrbol:")
for nodo, hijos in arbol.items():
  print(f"{nodo}: {hijos}")

# 3. Recorridos del árbol
preorden = [1, 2, 4, 8, 5, 9, 10, 3, 6, 11, 7, 12]
inorden = [8, 4, 2, 9, 5, 10, 1, 6, 11, 3, 12, 7]
postorden = [8, 4, 9, 10, 5, 2, 11, 6, 12, 7, 3, 1]

print("\nRecorrido en preorden:", preorden)
print("Recorrido en inorden:", inorden)
print("Recorrido en postorden:", postorden)

# ====================================================
# 4. Creación y visualización gráfica con NetworkX
# ====================================================

G = nx.DiGraph()
G.add_nodes_from(V)
G.add_edges_from(A)

# Coordenadas manuales para mantener la estructura jerárquica
pos = {
    1: (0, 0),
    2: (-2, -1),
    3: (2, -1),
    4: (-2.7, -2),
    5: (-1.3, -2),
    6: (1.3, -2),
    7: (2.7, -2),
    8: (-2.7, -3),
    9: (-1.7, -3),
    10: (-0.9, -3),
    11: (1.3, -3),
    12: (2.7, -3),
}

plt.figure(figsize=(10, 7))
plt.title(
    "Visualización del Árbol", fontsize=14, fontweight="bold", color="#1F4E79"
)

node_colors = [
    "#27AE60" if node in Nodo_hoja else "#85C1E9" for node in G.nodes()
]

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=700,
    font_size=11,
    font_weight="bold",
    font_color="black",
    edge_color="gray",
    width=1.5,
    arrows=True,
    arrowsize=15,
)

texto_recorridos = (
    f"Recorrido Preorden: {preorden}\n"
    f"Recorrido Inorden: {inorden}\n"
    f"Recorrido Postorden: {postorden}"
)

plt.figtext(
    0.5,
    0.02,
    texto_recorridos,
    ha="center",
    fontsize=9,
    family="monospace",
    bbox=dict(boxstyle="round,pad=0.5", fc="#F8F9F9", ec="#BDC3C7", lw=1),
)

plt.tight_layout(rect=[0, 0.08, 1, 1])

# Guarda la imagen automáticamente en la misma carpeta donde está tu script
plt.savefig("arbol_visualizacion.png", dpi=300)
print(
    "\n[Éxito] La imagen del árbol ha sido guardada como 'arbol_visualizacion.png'"
    " en tu carpeta."
)

plt.show()