import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def carregar_grafo(arquivo_csv):
    df = pd.read_csv(arquivo_csv)
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row["origem"], row["destino"], weight=row["peso"])
    return G

def encontrar_rota(G, origem, destino):
    caminho = nx.astar_path(G, origem, destino, weight="weight")
    custo = nx.path_weight(G, caminho, weight="weight")
    return caminho, custo

def desenhar_grafo(G, caminho=None, salvar_em=None):
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    if caminho:
        edges = list(zip(caminho, caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="red", width=2)
    if salvar_em:
        plt.savefig(salvar_em)
    plt.show()