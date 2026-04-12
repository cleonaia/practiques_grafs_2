"""
LABORATORI 2 - TASCA 1: EL PROBLEMA DE LES CLIQUES + TASCA 2: La loto n<m
"""

import networkx as nx
from itertools import combinations


def trobar_cliques_maximes(graf):
    """
    Trobar totes les cliques de mida màxima en un gràfic.
    
    Una clique és un subgraf complet on tots els vèrtexs estan 
    directament connectats entre si.
    
    Paràmetres:
    -----------
    graf : networkx.Graph
        El gràfic en el qual buscar les cliques màximes
    
    Retorna:
    --------
    list : Llista de cliques de mida màxima
    """
    
    vèrtexs = list(graf.nodes())
    
    if len(vèrtexs) == 0:
        return []
    
    totes_cliques = []
    
    # Generar totes les combinacions possibles de vèrtexs
    for mida in range(2, len(vèrtexs) + 1):
        for subconjunt in combinations(vèrtexs, mida):
            
            # Comprovar si aquest subconjunt forma una clique
            es_clique = True
            
            for u, v in combinations(subconjunt, 2):
                if not graf.has_edge(u, v):
                    es_clique = False
                    break
            
            if es_clique:
                totes_cliques.append(set(subconjunt))
    
    if not totes_cliques:
        return []
    
    # Trobar la mida màxima
    mida_maxima = max(len(clique) for clique in totes_cliques)
    
    # Retornar només les cliques amb mida màxima
    cliques_maximes = [clique for clique in totes_cliques 
                       if len(clique) == mida_maxima]
    
    return cliques_maximes


if __name__ == "__main__":
    # Posem un gràfic d'exemple
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5, 6])
    G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4), (4, 5), (5, 6), (4, 6), (5, 4)])
    
    print("TASCA 1: EL PROBLEMA DE LES CLIQUES\n")
    print(f"Vèrtexs: {list(G.nodes())}")
    print(f"Arestes: {list(G.edges())}\n")
    
    cliques_max = trobar_cliques_maximes(G)
    
    print("Cliques màximes:")
    for i, clique in enumerate(cliques_max, 1):
        print(f"  {i}. {sorted(clique)}")
